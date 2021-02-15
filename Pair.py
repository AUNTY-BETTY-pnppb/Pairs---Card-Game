from tkinter import *
import random
import time

class Counter(object):
    def __init__(self):
        self._counter = 0

    def getCounter(self):
        return self._counter

    def setCounter(self):
        raise NotImplementedError("Not implemented")

    def increment(self):
        self._counter = self._counter + 1

    counter = property(getCounter)

root = Tk()

counter = Counter()


root.minsize(height=450, width=450)
root.configure(bg='SlateGray4')

def choose():
    l.pack_forget()
    but.pack_forget()
    
    global counter2
    counter2 = 0

    global didPick
    didPick = False

    global last_pick
    last_pick = None

    global paired
    paired = []

    global rules
    rules = Label(root, text="Enter how many cards you want: 6, 12, 18, 24. ", bg="SlateGray3") 
    rules.pack()
    global entry
    entry = Entry(root)
    entry.pack()
    global button
    button = Button(root, text="Update deck", command=updateDeck)
    button.pack()

def updateDeck():
    global entry
    text = entry.get()
    if text in ["6", "12", "18", "24"]:
        global num
        num = int(text)
        global col_list
        global card_list
        col_list = colors[:num]
        card_list = deck[:num]
        cb1()
    else:
        global rules
        rules['text'] = "PLease pick a number from: 6, 12, 18, 24"


def cb1():
    rules.pack_forget()
    entry.pack_forget()
    button.pack_forget()

    random.shuffle(col_list)

    for card in card_list:
        w.itemconfig(card, fill=col_list[card_list.index(card)])

    points.configure(text="Points: " + str(0))
    points.pack()
    w.pack()
    w.after(1000, blank)
    but.pack()
    but.configure(text="FINISH", command=cb2)

def cb2():
    w.pack_forget()
    for card in deck:
        w.itemconfig(card, fill="white")
    global counter2
    l.configure(text="WOW THANKS FOR PLAYING! YOU GOT " + str(counter2) + " PAIRS")
    l.pack(side="top")
    but.configure(text="AGAIN?", command=choose)

def blank():
    for card in card_list:
        w.tag_bind(card, "<ButtonPress-1>", check)
        w.itemconfig(card, fill="SlateGray3")

def check(event):
    global counter2 
    global didPick
    global last_pick
    global num
    global paired

    eventX = int(event.x)
    eventY = int(event.y)

    for card in card_list:
        if clicked(eventX, eventY, card):
            w.itemconfig(card, fill=col_list[card_list.index(card)])
            if not didPick:
                last_pick = card
                didPick = True
            elif didPick:
                if last_pick != card:
                    if w.itemcget(last_pick, "fill") == w.itemcget(card, "fill"):
                        w.tag_unbind(last_pick, "<Button-1>")
                        w.tag_unbind(card, "<Button-1>")

                        paired.append(card)
                        paired.append(last_pick)

                        counter2 += 1
                        points.configure(text="Points: " + str(counter2))
                    else:
                        for i in card_list:
                            if i not in paired:
                                w.tag_unbind(i, "<Button-1>")
                        w.after(700, reset, last_pick, card)
                    didPick = False  
    if counter2 == num//2:
        w.after(700, cb2)

def reset(bef, aft):
    w.itemconfig(bef, fill="SlateGray3")
    w.itemconfig(aft, fill="SlateGray3")
    for i in card_list:
        if i not in paired:
            w.tag_bind(i, "<Button-1>", check)

def clicked(x, y, picked):
    cords = w.coords(picked)

    if x in range(int(cords[0]), int(cords[2])):
        if y in range(int(cords[1]), int(cords[3])):
            return True
    return False

w = Canvas(root, height=450, width=430, bg="SlateGray2") 

#--------------DECK OF CARDS-----------------------------
deck = []

card  = w.create_rectangle(10, 10, 70, 100, fill="white")
deck.append(card)
card1 = w.create_rectangle(80, 10, 140, 100, fill="white")
deck.append(card1)
card2 = w.create_rectangle(150, 10, 210, 100, fill="white")
deck.append(card2)
card3 = w.create_rectangle(220, 10, 280, 100, fill="white")
deck.append(card3)
card4 = w.create_rectangle(290, 10, 350, 100, fill="white")
deck.append(card4)
card5= w.create_rectangle(360, 10, 420, 100, fill="white")
deck.append(card5)

card6  = w.create_rectangle(10, 110, 70, 210, fill="white")
deck.append(card6)
card7 = w.create_rectangle(80, 110, 140, 210, fill="white")
deck.append(card7)
card8 = w.create_rectangle(150, 110, 210, 210, fill="white")
deck.append(card8)
card9 = w.create_rectangle(220, 110, 280, 210, fill="white")
deck.append(card9)
card10 = w.create_rectangle(290, 110, 350, 210, fill="white")
deck.append(card10)
card11 = w.create_rectangle(360, 110, 420, 210, fill="white")
deck.append(card11)

card12  = w.create_rectangle(10, 320, 70, 220, fill="white")
deck.append(card12)
card13 = w.create_rectangle(80, 320, 140, 220, fill="white")
deck.append(card13)
card14 = w.create_rectangle(150, 320, 210, 220, fill="white")
deck.append(card14)
card15 = w.create_rectangle(220, 320, 280, 220, fill="white")
deck.append(card15)
card16 = w.create_rectangle(290, 320, 350, 220, fill="white")
deck.append(card16)
card17 = w.create_rectangle(360, 320, 420, 220, fill="white")
deck.append(card17)

card18  = w.create_rectangle(10, 430, 70, 330, fill="white")
deck.append(card18)
card19 = w.create_rectangle(80, 430, 140, 330, fill="white")
deck.append(card19)
card20 = w.create_rectangle(150, 430, 210, 330, fill="white")
deck.append(card20)
card21 = w.create_rectangle(220, 430, 280, 330, fill="white")
deck.append(card21)
card22 = w.create_rectangle(290, 430, 350, 330, fill="white")
deck.append(card22)
card23 = w.create_rectangle(360, 430, 420, 330, fill="white")
deck.append(card23)

colors = ["yellow", "yellow", "blue", "blue", "red", "red",
          "green", "green", "orange", "orange", "gold", "gold",
          "purple", "purple", "violet", "violet", "black", "black",
          "brown", "brown", "pink", "pink", "navy", "navy"]

global counter2
counter2 = 0
points = Label(root, text="Points: " + str(counter2), bg="SlateGray3") 
l = Label(root, text="wow" + str(counter2), bg="SlateGray3")

title = Label(root, text="Pairs - Card Game", bg="SlateGray2", font=1, relief=RAISED)
title.pack()

but = Button(root, text="START", command=choose, bg="SlateGray3")  
but.pack()

root.mainloop()