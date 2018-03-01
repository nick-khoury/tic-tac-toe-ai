##IMPORTS
import random


rps = ['R', 'P', 'S']##VALID ROCK-PAPER-SCISSORS MOVES
rpsdic = {'R':'P', 'P':'S', 'S':'R'}##DICTIONARY TO LOOK UP WINNING MOVE


def patmat(playhist, defaultact):##RPS PATTERN BEATING ALGORITHM FUNCTION
    for i in range(  len(playhist)//2, 4, -1 ):
        seg = playhist[ :i]
        rest = playhist[i: ]
        #print(seg,rest)
        if str(seg)[1:-1] in str(rest)[1:-1]:
            #print(i)
            cur = len(rest)%len(seg)#current index in pattern
            seg = seg[cur: ]
            #print(seg)
            return rpsdic[seg[0]]
    return defaultact


class RPSai:
    
    def __init__(self):
        self.history = []

    def opponentMove(self, amove):
        if amove in rps:
            self.history.append(amove)
        else:
            print('ERROR')

    def beatMove(self, expectopmove):
        return rpsdic[expectopmove]

    def predictMove(self):
        countdic = {}
        for move in self.history:
            countdic[move] = countdic.get(move, 0) + 1
        maxcount = max(list(countdic.values()))
        movemode = []
        for move in self.history:
            if countdic[move] == maxcount:
                movemode.append(move)
        return movemode[random.randint(0, len(movemode) - 1)]

    def playMove(self):
        if len(self.history) == 0:
            return rps[random.randint(0, 2)]
        else:
            return rpsdic[self.predictMove()]

    def playMovePro(self):
        if 0 == len(self.history):
            return rps[random.randint(0,2)]
        elif 1 == len(self.history):
            return self.beatMove(self.history[0])
        elif 2 == len(self.history):
            return self.beatMove(self.history[0])
        elif 3 <= len(self.history) and len(self.history) <= 7:
            ago_3 = self.history[-3]
            ago_2 = self.history[-2]
            ago_1 = self.history[-1]
            if ago_1 == ago_2 and ago_1 == ago_3:
                return self.beatMove(ago_1)
            else: #ago_1 != ago_2 and ago_1 != ago_3:
                return self.beatMove(ago_3)
        ##ONLY USE PATTERN BEATING ALGORITHM IF MORE THAN 7 MOVES IN HISTORY
        elif 8 <= len(self.history) and len(self.history) <= 20:
            #print('patmat')
            return patmat(self.history, self.playMove())
        ##IF MORE THAN 20 MOVES, USE PATTERN BEATING ALGORITH ON PAST 20 MOVES
        else:
            return patmat(self.history[-20: ], self.playMove())
