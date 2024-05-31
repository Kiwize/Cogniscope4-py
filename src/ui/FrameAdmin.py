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
            self.iterate_values(project.getProjectTagsDataDict(), i)    
                
                
            
        else :
            self.projectData = Label(self, text="No project opened...")

    def iterate_values(self, d, parent_key='', i=0): 
            
        if isinstance(d, dict):
            for key, value in d.items():
                current_key = f"{parent_key}.{key}" if parent_key else key
                
                if not "[" in value:
                    
                    if isinstance(value, list):
                        print('HERE ===========> ' + str(type(value)) + "     " + str(value))
                        self.iterate_values(value, current_key, i)
                    
                    i = i + 1
                    if i % 2 == 0:
                        Label(self.scrollable_frame, text=current_key, anchor="w", justify="left", bg="#575757").grid(column=0, row=i, sticky="nswe")
                        Label(self.scrollable_frame, text=value, anchor="w", justify="left", bg="#575757").grid(column=1, row=i, sticky="nswe")
                    else :
                        Label(self.scrollable_frame, text=current_key, anchor="w", justify="left").grid(column=0, row=i, sticky="nswe")
                        Label(self.scrollable_frame, text=value, anchor="w", justify="left").grid(column=1, row=i, sticky="nswe")
                        
                self.iterate_values(value, current_key, i)
                    
        elif isinstance(d, list):
            for a, item in enumerate(d):
                current_key = f"{parent_key}[{a}]"
                if not "[" in item:
                    if isinstance(item, dict):
                        print('HERE ===========> ' + str(type(item)) + "     " + str(item))
                        self.iterate_values(item, current_key, i)

                    i = i + 1
                    if current_key == "data.projectData":
                        print(type(value))
                    if i % 2 == 0:
                        Label(self.scrollable_frame, text=current_key, anchor="w", justify="left", bg="#575757").grid(column=0, row=i, sticky="nswe")
                        Label(self.scrollable_frame, text=item, anchor="w", justify="left", bg="#575757").grid(column=1, row=i, sticky="nswe")
                    else :
                        Label(self.scrollable_frame, text=current_key, anchor="w", justify="left").grid(column=0, row=i, sticky="nswe")
                        Label(self.scrollable_frame, text=item, anchor="w", justify="left").grid(column=1, row=i, sticky="nswe")
                self.iterate_values(item, current_key, i)
