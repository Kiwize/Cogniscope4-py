#This file opens XMLs files from Concertina and Cognisope 3 to import them in Cogniscope 4
from bs4 import BeautifulSoup
from src.model.Project import Project
import xml.etree.ElementTree as ET
import pprint

class XMLFileParser :

    def __init__(self):
        self.project = None
        self.projectDataDict = {}

    def openFile(self, filePath):
        self.currentFile = filePath
        
        with open(filePath, 'r+', encoding='utf8') as f:
            data = f.read()

            Bs_data = BeautifulSoup(data, "xml")

            projectData = Bs_data.findChild('projectData')
            triggeringQuestion = Bs_data.find('trigQ')
            genericQuestion = Bs_data.find('genericQ')

            clusters = Bs_data.findAll('cluster')
            ideas = Bs_data.findAll('idea')

            # Conversion du fichier XML en dictionnaire
            self.projectDataDict = self.parse_xml_to_dict(self.currentFile)
            print(self.projectDataDict)

            self.project = Project(self.projectDataDict)
            
            

            
    def getProject(self) -> Project:
        return self.project
    
    
    def getProjectDataDict(self) :
        return self.projectDataDict

    def xml_to_dict(self, element):
        # Initialiser le dictionnaire pour cet élément
        result = {}

        # Si l'élément a des enfants, traiter chaque enfant
        if list(element):
            for child in element:
                child_result = self.xml_to_dict(child)
                if child.tag in result:
                    # Si le tag est déjà présent, nous devons convertir la valeur en liste ou l'ajouter à la liste existante
                    if isinstance(result[child.tag], list):
                        result[child.tag].append(child_result)
                    else:
                        result[child.tag] = [result[child.tag], child_result]
                else:
                    result[child.tag] = child_result
        else:
            # Si l'élément n'a pas d'enfants, utiliser son texte
            result = element.text if element.text is not None else ""

        # Ajouter les attributs de l'élément au dictionnaire
        if element.attrib:
            result.update({f'@{k}': v for k, v in element.attrib.items()})

        return result

    def parse_xml_to_dict(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        return {root.tag: self.xml_to_dict(root)}



                
        


    