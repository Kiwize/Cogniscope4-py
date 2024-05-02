from tkinter import Frame, Label
import webbrowser

class FrameVersion(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        nameLabel = Label(self, text="Cogniscope 4 py")
        nameLabel.pack(side="top", fill="x", pady="5")

        versionLabel = Label(self, text="Version 0.1")
        versionLabel.pack(side="top", fill="x", pady="5")

        checkVerLabel = Label(self, text="Check for updates")
        checkVerLabel.bind("<Button-1>", lambda e: webbrowser.open("https://www.ekkotek.com/index.php/products/wisdom-tools/Cogniscope3", new=0, autoraise=True))
        checkVerLabel.pack(side="top", fill="x", pady="5")

        copyrightLabel = Label(self, text="Copyrights Ekkotek Ltd. 2024")
        copyrightLabel.pack(side="top", fill="x", pady="5")

        


