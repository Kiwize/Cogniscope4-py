from tkinter import Frame, Label
import webbrowser

class FrameUserPreferences(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        nameLabel = Label(self, text="Preferences")
        nameLabel.pack(side="top", fill="x", pady="5")