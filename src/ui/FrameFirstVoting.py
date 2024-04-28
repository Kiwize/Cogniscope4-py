from tkinter import Frame, Label

class FrameFirstVoting(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="First Voting")
        label.pack(side="top", fill="x", pady="10")


