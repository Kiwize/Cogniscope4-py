from tkinter import Frame, Label, OptionMenu, StringVar
import webbrowser

class FrameUserPreferences(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)

        frameTitle = Label(self, text="Preferences")
        frameTitle.pack(side="top", fill="x", pady="5")
        
        self.userLangageSelected = StringVar() 
        self.availableLangages = [
            "EN",
            "EL",
            "TR"
        ]
        
        self.userLangageSelected.set(self.availableLangages[0])
        
        userLangage = OptionMenu(self, self.userLangageSelected, *self.availableLangages)
        userLangage.pack(side="top", fill="x", pady="5")
        self.userLangageLabel = userLangage
        
    def setUserPreference(self, preferences):
        self.userPreferences = preferences.getUserPreferences()
        
        self.userLangageSelected.set(self.userPreferences["PR_defaultLanguage"])
        
        
        
        