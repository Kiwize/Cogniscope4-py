#This file opens XMLs files from Concertina and Cognisope 3 to import them in Cogniscope 4
from bs4 import BeautifulSoup
from src.model.Project import Project

class XMLFileParser :

    def __init__(self) -> None:
        pass

    def openFile(self, filePath):
        self.currentFile = filePath
        
        with open(filePath, 'r+', encoding='utf8') as f:
            data = f.read()

            Bs_data = BeautifulSoup(data, "xml")

            projectData = Bs_data.findChild('projectData')
            triggeringQuestion = Bs_data.find('trigQ')
            genericQuestion = Bs_data.find('genericQ')

            self.project = Project(projectData, triggeringQuestion, genericQuestion)
            
            



    