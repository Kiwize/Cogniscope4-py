from tkinter import Frame, Label

class FrameGeneration(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="Generation")
        label.pack(side="top", fill="x", pady="10")


