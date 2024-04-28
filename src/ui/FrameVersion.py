from tkinter import Frame, Label

class FrameVersion(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        nameLabel = Label(self, text="Cogniscope 4 py")
        nameLabel.pack(side="top", fill="x", pady="5")

        versionLabel = Label(self, text="Version 0.1")
        versionLabel.pack(side="top", fill="x", pady="5")

        copyrightLabel = Label(self, text="Copyrights Ekkotek Ltd. 2024")
        copyrightLabel.pack(side="top", fill="x", pady="5")


