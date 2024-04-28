from tkinter import Frame, Label

class FrameSecondVoting(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="Second Voting")
        label.pack(side="top", fill="x", pady="10")


