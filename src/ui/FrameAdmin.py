from tkinter import Frame, Label
from src.xml.XMLFileParser import XMLFileParser

class FrameAdmin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.xmlparser = None

        label = Label(self, text="Admin")
        label.grid(column=0, row=0)
        
        self.projectData = Label(self, text="No project opened...", anchor="e", justify="left")
        self.projectData.grid(column=0, row=1)

    def setXMLFileParser(self, xmlparser: XMLFileParser):
        self.xmlparser = xmlparser
        
    def updateData(self):
        if self.xmlparser.getProject() != None :
            self.projectData.config(text="")
            project = self.xmlparser.getProject()
            
            for key, val in project.getProjectTagsDataDict().items() :
                self.projectData.config(text=self.projectData.cget("text") + "\r" + key + " : " + val)
                
            
        else :
            self.projectData = Label(self, text="No project opened...")
