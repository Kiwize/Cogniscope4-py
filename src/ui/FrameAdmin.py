from tkinter import Frame, Label
from src.xml.XMLFileParser import XMLFileParser
import customtkinter

class FrameAdmin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.xmlparser = None

        label = Label(self, text="Admin")
        label.grid(column=0, row=0, sticky="nesw")
        
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid(column=0, row=1, sticky="news")  
        
        self.projectData = Label(self.scrollable_frame, text="No project opened...")
        self.projectData.grid(column=0, row=0, sticky="nesw")    
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def setXMLFileParser(self, xmlparser: XMLFileParser):
        self.xmlparser = xmlparser
        
    def updateData(self):
        if self.xmlparser.getProject() != None :
            self.projectData.config(text="")
            project = self.xmlparser.getProject()
            
            print("Displaying file content into admin page...")
            i = 0

            #self.iterate_values(project.getProjectTagsDataDict(), i)    
            for key, val in project.getProjectTagsDataDict().items():
                print("Key : " + str(key) + "     Val : " + str(val))
                i = i + 1
                if i % 2 == 0:
                    Label(self.scrollable_frame, text=key, anchor="w", justify="left", bg="#575757").grid(column=0, row=i, sticky="nswe")
                    Label(self.scrollable_frame, text=val, anchor="w", justify="left", bg="#575757").grid(column=1, row=i, sticky="nswe")
                else :
                    Label(self.scrollable_frame, text=key, anchor="w", justify="left").grid(column=0, row=i, sticky="nswe")
                    Label(self.scrollable_frame, text=val, anchor="w", justify="left").grid(column=1, row=i, sticky="nswe")
                
        else :
            self.projectData = Label(self, text="No project opened...")

