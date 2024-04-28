from tkinter import Frame, Label

class FrameClarification(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="Clarification")
        label.pack(side="top", fill="x", pady="10")


