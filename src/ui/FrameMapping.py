from tkinter import Frame, Label

class FrameMapping(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="Mapping")
        label.pack(side="top", fill="x", pady="10")


