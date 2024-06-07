#This file opens XMLs files from Concertina and Cognisope 3 to import them in Cogniscope 4
from bs4 import BeautifulSoup
from src.model.Project import Project
import xml.etree.ElementTree as ET
from lxml import etree
import pprint

class XMLFileParser :

    indent = 0
    ignoreElems = ['displayNameKey', 'displayName']
    

    def __init__(self):
        self.project = None
        self.projectDataDict = {}
        self.matrixTagKey = []
        self.matrixDetection = ["prevOpportunityMatrix", "opportunityMatrix", "prevISMmatrix", "ISMmatrix"]
        self.matrixDetectionCountsElem = {}
        self.matrixElemCounter = 0

    def openFile(self, filePath):
        self.currentFile = filePath
        
        with open(filePath, 'r+', encoding='utf8') as f:
            # Conversion du fichier XML en dictionnaire
            tree = etree.parse(self.currentFile)
            self.root = tree.getroot()

            for md in self.matrixDetection:
                self.matrixDetectionCountsElem[md] = 0

            self.printRecur(self.root)

            self.dedupMatrixTagKey = []

            for i in self.matrixTagKey:
                if i not in self.dedupMatrixTagKey:
                     self.dedupMatrixTagKey.append(i)

            matx = 0
            maty = 0
        
            for md in self.matrixDetection:
                self.projectDataDict[md + ".matrix"] = ""
                for mat in self.dedupMatrixTagKey:
                    if md in mat:
                        if "rows" in mat:
                            matx = int(mat.split(".")[2])
                            self.matrixElemCounter = 0
                        elif "columns" in mat:
                            maty = int(mat.split(".")[2])
                            self.matrixElemCounter = 0
                       

                for mat in self.dedupMatrixTagKey:
                    if md == mat.split(".")[0]:
                        if "element" in mat :
                            if not matx == 0 and not maty == 0:
                                #print("Displaying matrix " + str(matx) + " X " + str(maty) + "   " + md)
                                self.projectDataDict[md + ".matrix"] = self.projectDataDict[md + ".matrix"] + mat.split(".")[3] + "  "
                                self.matrixElemCounter += 1

                                if self.matrixElemCounter >= maty:
                                    self.projectDataDict[md + ".matrix"] = self.projectDataDict[md + ".matrix"] + "\r"
                                    self.matrixElemCounter = 0
            

            self.project = Project(self.projectDataDict)
            
    def getProject(self) -> Project:
        return self.project
    
    
    def getProjectDataDict(self) :
        return self.projectDataDict

    def get_parents(self, element):
        parents = []
        parent = element.getparent()
        while parent is not None:
            parents.append(parent.tag)
            parent = parent.getparent()
        parents.reverse()
        path = ".".join(parents) + "." + element.tag
        return path


    def printRecur(self, root):
        parents = self.get_parents(root)
        
        if root.text:
            #print (' ' *self.indent + '%s: %s' % (root.tag.title(), root.attrib.get('name', root.text)))

            if not root.text.isspace():
                for md in self.matrixDetection:
                    if not md in parents:
                        if not "matrix" in parents or not "Matrix" in parents:
                            if not parents in self.projectDataDict:
                                if "ideas" in parents:
                                    if "Num" in parents:
                                        self.currentIdeaNum = int(root.attrib.get('name', root.text))

                                    self.projectDataDict[parents + "." +  str(self.currentIdeaNum)] = root.attrib.get('name', root.text)
                                elif "cluster" in parents:
                                    if "Num" in parents:
                                        self.currentClusterNum = int(root.attrib.get('name', root.text))

                                    self.projectDataDict[parents + "." +  str(self.currentClusterNum)] = root.attrib.get('name', root.text)      
                                else :
                                    self.projectDataDict[parents] = root.attrib.get('name', root.text)

                        if "data.matrix" in parents:
                            if "id" in parents :
                                self.valueCounter = 1
                                self.lastMatriceID = str(root.attrib.get('name', root.text))
                            elif "values.value" in parents :
                                if self.valueCounter == 1 or self.valueCounter % 4 == 1: 
                                    self.projectDataDict[parents + "." + self.lastMatriceID + "." + str(int((self.valueCounter - 1) / 4))] = str(root.attrib.get('name', root.text))
                                self.valueCounter += 1
                    else :
                        if not md in parents.split('.'):
                            return

                        if "rows" in parents :
                            self.matrixTagKey.append(md + ".rows." + root.attrib.get('name', root.text)) 
                        elif "columns" in parents:
                            self.matrixTagKey.append(md + ".columns." + root.attrib.get('name', root.text))
                        elif "element" in parents:
                            self.matrixTagKey.append(md + ".element." + str(self.matrixDetectionCountsElem[md])  + "." + root.attrib.get('name', root.text))
                            self.matrixDetectionCountsElem[md] += 1

        for elem in root:
            self.printRecur(elem)

    

                
        


    