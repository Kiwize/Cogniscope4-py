#This file opens XMLs files from Concertina and Cognisope 3 to import them in Cogniscope 4
from bs4 import BeautifulSoup

class XMLFileParser :

    def __init__(self) -> None:
        pass

    def openFile(self, filePath):
        self.currentFile = filePath
        
        with open(filePath, 'r+', encoding='utf8') as f:
            data = f.read()

            Bs_data = BeautifulSoup(data, "xml")
 
            b_unique = Bs_data.find_all('projectData')
            
            print(b_unique)



    