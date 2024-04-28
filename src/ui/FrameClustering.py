from tkinter import Frame, Label

class FrameClustering(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        label = Label(self, text="Clustering")
        label.pack(side="top", fill="x", pady="10")


