from tkinter import Frame, Label

class FrameAdmin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.xmlparser = None

        label = Label(self, text="Admin")
        label.pack(side="top", fill="x", pady="10")
        
        self.projectNameLabel = Label(self, text="No project opened...")
        self.projectNameLabel.pack(side="top", fill="x", pady="10")

    def setXMLFileParser(self, xmlparser):
        self.xmlparser = xmlparser
        
    def updateData(self):
        if self.xmlparser.getProject() != None :
            print("OK !")
            
            self.projectNameLabel.config(text="ProjectName : " + self.xmlparser.getProject().getName())
        else :
            self.projectNameLabel = Label(self, text="No project opened...")
