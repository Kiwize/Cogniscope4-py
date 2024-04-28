from tkinter import Frame, Label

class FrameTriggeringQuestion(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="Triggering Question")
        label.pack(side="top", fill="x", pady="10")


