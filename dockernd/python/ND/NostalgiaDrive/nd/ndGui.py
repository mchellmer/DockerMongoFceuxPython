#!/usr/bin/python3
from tkinter import *
from random import randint
import os
import datetime


class NdGui:
    """Generates an interface for the user to make selections"""
    # Constructor

    def __init__(self):
        print("GUI Constructed")

        self.genGui()

    # Attributes
    key = 1
    ndMain = Tk()
    pad = 3
    _geom = '200x200+0+0'
    sWidth = ndMain.winfo_screenwidth()
    sHeight = ndMain.winfo_screenheight()
    ndMain.geometry("{0}x{1}+0+0".format(sWidth - pad, sHeight - pad))

    selections = {}

    # Methods
    # Generate opening screen
    def genGui(self):
        print("GUI Building")
        options = ["Just Play!", "Prepare to Die", "Choose Something", "Something New"]
        rows = [1, 0, 1, 2]
        cols = [1, 2, 3, 2]

        # TODO: DRY because can't figure out how to dynamically set command
        simH = self.sHeight/3 - 20
        shift = 0.25 * (self.sWidth - simH*3)
        basep = os.path.join('..', 'python', 'NostalgiaDrive', 'NostalgiaDrive')

        label = Label(self.ndMain, text = '')
        label.grid(column = 0, row = 0, padx=shift)

        rFile = os.path.join(basep, "docs","images","rsz_mario_coin_block_by_mattkrocks_224_224.gif")
        randphoto=PhotoImage(file=rFile)
        randPlay = Button(self.ndMain, text=options[0], command=lambda: self.optionInterpret(0))
        randPlay.config(image=randphoto,width=simH,height=simH)
        randPlay.grid(row=rows[0], column=cols[0])

        hFile = os.path.join(basep, "docs","images","tombstone_pixel_art_by_megalomaniacaly-dakxo4m_224_224.gif")
        hardphoto=PhotoImage(file=hFile)
        hardPlay = Button(self.ndMain, text=options[1], command=lambda: self.optionInterpret(1))
        hardPlay.config(image=hardphoto,width=simH,height=simH)
        hardPlay.grid(row=rows[1], column=cols[1])

        sFile = os.path.join(basep, "docs","images","playerselect_225x225.gif")
        selphoto=PhotoImage(file=sFile)
        selectPlay = Button(self.ndMain, text=options[2], command=lambda: self.optionInterpret(2))
        selectPlay.config(image=selphoto,width=simH,height=simH)
        selectPlay.grid(row=rows[2], column=cols[2])

        nFile = os.path.join(basep, "docs","images","bino_190x183.gif")
        newphoto=PhotoImage(file=nFile)
        newPlay = Button(self.ndMain, text=options[3], command=lambda: self.optionInterpret(3))
        newPlay.config(image=newphoto,width=simH,height=simH)
        newPlay.grid(row=rows[3], column=cols[3])
        # TODO: Dynamic command select
        # dOptions = {'buttons': {}}

        # for i in range(0, 4):
        # dOptions['buttons'][i] = {}
        # dOptions['buttons'][i]['row'] = rows[i]
        # dOptions['buttons'][i]['col'] = cols[i]
        # dOptions['buttons'][i]['option'] = options[i]
        # dOptions['buttons'][i]['button'] = Button(self.ndMain, text=options[i], command=lambda: self.optionInterpret(i))

        # for i in range(0, 4):
        # dOptions['buttons'][i]['button'].grid(row=dOptions['buttons'][i]['row'], column=dOptions['buttons'][i]['col'])

        self.ndMain.mainloop()

    def optionInterpret(self, index):
        print("Interpretting Selection")
        if index == 0:
            self.genRandomGame()
        elif index == 1:
            self.genHardGame()
        elif index == 2:
            self.goSelect()
        elif index == 3:
            self.genNewGame()

    def genRandomGame(self):
        print("Returning a random Game")
        result = self.getTextOptions("all")
        rnd = randint(0, len(result) - 1)
        self.goPlay(result[rnd])

    # TODO: chain most difficult parts of games
    def genHardGame(self):
        print("Returning a Difficult Game")
        result = self.getTextOptions("hard")
        rnd = randint(0, len(result) - 1)
        self.goPlay(result[rnd])

    # TODO: log past selections as ignore list
    def genNewGame(self):
        print("Returning a New Game")
        result = self.getTextOptions("all")
        rnd = randint(0, len(result) - 1)
        self.goPlay(result[rnd])

    # Generate selection screen (number of players, genre, rating, popularity)
    def genSelect(self):
        print("Selection Screen Building")
        b = Button(self.ndMain, text="PLAY!", command=self.goPlay)
        b.grid(row=0, column=0)
        b = Button(self.ndMain, text="BACK!", command=self.goBack)
        b.grid(row=1, column=0)

        genres = self.getTextOptions('genres')
        labels = ["Players", "Genres", "Ratings", "", "Popular In"]
        players = self.getTextOptions('players')
        popularity = ["USA", "JAPAN", "EUROPE", "ELSEWHERE", "...NOWHERE"]

        for i in range(len(labels)):
            Label(self.ndMain, text=labels[i]).grid(row=0, column=i + 1)

        self.genChecks(0, 'players', players)
        self.genChecks(1, 'genres', genres)
        self.genRating(2)
        self.genChecks(4, 'popularity', popularity)

        self.ndMain.mainloop()

    def genChecks(self, col, type, entries=[]):
        print("Building Check Widgets")
        for i in range(0, len(entries)):
            CheckVar = BooleanVar()
            cButton = Checkbutton(self.ndMain, text=entries[i], variable=CheckVar, height=5, width=20)
            cButton.grid(row=i + 1, column=col + 1)

            entry = {'entry': {'type': 'check', 'data': type, 'text': cButton['text'], 'val': CheckVar}}
            self.selections[self.key] = entry
            self.key += 1

    # TODO: dynamic selection as MIN/MAX can clash, DRY
    def genRating(self, col):
        print("Building Dropdown Widgets")
        minLabel = Label(self.ndMain, text="Min").grid(row=1, column=col + 1)
        maxLabel = Label(self.ndMain, text="Max").grid(row=2, column=col + 1)

        a = list(range(11))
        varMin = IntVar(self.ndMain)
        varMin.set(0)
        varMax = IntVar(self.ndMain)
        varMax.set(10)
        oMenuMin = OptionMenu(self.ndMain, varMin, *a)
        oMenuMin.grid(row=1, column=col + 2)

        oMenuMax = OptionMenu(self.ndMain, varMax, *a)
        oMenuMax.grid(row=2, column=col + 2)

        entry = {'entry': {'type': 'Option', 'data': 'rating', 'text': 'Min', 'val': varMin}}
        self.selections[self.key] = entry
        self.key += 1
        entry = {'entry': {'type': 'Option', 'data': 'rating', 'text': 'Max', 'val': varMax}}
        self.selections[self.key] = entry
        self.key += 1

    def goSelect(self):
        print("Going to Selection Screen")
        widgets = self.ndMain.grid_slaves()
        for widget in widgets:
            widget.grid_forget()

        self.genSelect()

    def goBack(self):
        print("Returning to Main Screen")
        widgets = self.ndMain.grid_slaves()
        for widget in widgets:
            widget.grid_forget()

        self.genGui()

    def goPlay(self, *args):
        print("Selection Entered")

        outpath = os.path.join('..', 'python', 'NostalgiaDrive', 'NostalgiaDrive', 'docs', 'log.txt')
        file = open(outpath, 'w')
        now = datetime.datetime.now()
        file.write('\n' + str(now) + ': Start Selections' + '\n')
        if args:
            file.write(args[0] + '\n')
        else:
            for i in range(1, len(self.selections) + 1):
                col = self.selections[i]['entry']['data']
                item = self.selections[i]['entry']['text']
                val = self.selections[i]['entry']['val'].get()
                file.write(col + ' ' + item + ' ' + str(val) + '\n')

        file.write('End Selections' + '\n')
        self.ndMain.destroy()

    def getTextOptions(self, item):
        print("Grabbing Options from File")
        filename = item + '.txt'
        gPath = os.path.join('..', 'python', 'NostalgiaDrive', 'NostalgiaDrive', 'docs', 'selections', filename)
        f = open(gPath, 'r')
        lines = f.readlines()[:-1]
        lines.sort()
        return [x.strip() for x in lines]
