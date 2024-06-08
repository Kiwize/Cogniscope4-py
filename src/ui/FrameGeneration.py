from tkinter import Frame, Label
from src.ui.components.RoundedButton import RoundedButton

class FrameGeneration(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.grid_columnconfigure([0, 2], weight=0)
        self.grid_columnconfigure([1], weight=5)

        self.grid_rowconfigure([1], weight=5)

        self.title = Label(self, text="Generation")

        self.previousButton = RoundedButton(self, text="<", command=lambda: self.previousIdea())
        self.previousButton.grid(column=0, row=2)

        self.nextButton = RoundedButton(self, text=">", command=lambda: self.nextIdea())
        self.nextButton.grid(column=2, row=2)

        self.ideaLabel = Label(self, text="Placeholder")
        self.ideaLabel.grid(column=1, row=1)

        self.title.grid(column=1, row=0)

    def previousIdea(self):
        return
    
    def nextIdea(self):
        return




