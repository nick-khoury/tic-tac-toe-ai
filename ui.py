from tkinter import Tk, Button, Label
from rps import RPSai


win = Tk()
win.wm_title('Rock, Paper, Scissors')
win.geometry('400x400')

def winner(p1, p2):
    if p1 + p2 in ['RS', 'SP', 'PR']:
        return 1
    elif p1 == p2:
        return 0
    else:
        return -1

class UI:
    def __init__(self):
        self.myAI = RPSai()
        self.wins = 0
        self.games = 0

        self.rockB = Button(win, text='Rock', command = self.rockPressed, font=('Comic Sans MS', 12))
        self.paperB = Button(win, text='Paper', command = self.paperPressed, font=('Comic Sans MS', 12))
        self.scissorsB = Button(win, text='Scissors', command = self.scissorsPressed, font=('Comic Sans MS', 12))
        self.rockB.place(x=90, y=300)
        self.paperB.place(x=160, y=300)
        self.scissorsB.place(x=240, y=300)

        self.status = Label(win, text='Choose!', font=('Comic Sans MS', 16))
        self.status.place(x=20, y=150)

        if self.games == 0:
            wr = 0
        else:
            wr = self.wins/self.games
        self.winRate = Label(win, text=wr, font=('Comic Sans MS', 16))
        self.winRate.place(x=20, y=50)

        self.gameCount = Label(win, text=self.games, font=('Comic Sans MS', 16))
        self.gameCount.place(x=320, y=50)

    def rockPressed(self):
        self.playRound('R')

    def paperPressed(self):
        self.playRound('P')

    def scissorsPressed(self):
        self.playRound('S')

    def playRound(self, move):
        cpuMove = self.myAI.playMovePro()#use playMovePro()
        self.myAI.opponentMove(move)
        print(move + str(cpuMove))
        win = winner(str(move)[0], str(cpuMove)[0])
        self.games += 1
        if win == 1:
            result = 'Win'
            self.wins += 1
        elif win == -1:
            result = 'Lose'
        else:
            result = 'Tie'
            self.wins += 0.5

        self.gameCount['text'] = '%d'%(self.games)
        self.status['text'] = '%s vs %s - You: %s'%(move, cpuMove, result)
        self.winRate['text'] = '%f'%(self.wins / self.games)


myUI = UI()
win.mainloop()
