from tkinter import Tk
from src.ui.Window import Window
from src.cfg.Config import ConfigReader


if __name__ == "__main__" :
    configReader = ConfigReader()
    configReader.readConfig("Cogniscope4Pref")

    window = Window(configReader)

    print("Default language is " + configReader.getUserPreferences()["PR_defaultLanguage"])

    window.mainloop()
