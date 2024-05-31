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

            ignoreElems = ['displayNameKey', 'displayName']

            for md in self.matrixDetection:
                self.matrixDetectionCountsElem[md] = 0

            self.printRecur(self.root, ignoreElems)

            self.dedupMatrixTagKey = []

            for i in self.matrixTagKey:
                if i not in self.dedupMatrixTagKey:
                     self.dedupMatrixTagKey.append(i)

            print("====== MATRICES =======")

            for elem in self.dedupMatrixTagKey:
                print(elem)

            print("==============")

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
                                print("Displaying matrix " + str(matx) + " X " + str(maty) + "   " + md)
                                self.projectDataDict[md + ".matrix"] = self.projectDataDict[md + ".matrix"] + mat.split(".")[3]
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


    def printRecur(self, root, ignoreElems):
        """Recursively prints the tree."""
        if root.tag in ignoreElems:
            return
        
        if root.text:
            #print (' ' *self.indent + '%s: %s' % (root.tag.title(), root.attrib.get('name', root.text)))

            if not root.text.isspace():
                for md in self.matrixDetection:
                    if not md in self.get_parents(root):
                        if not "matrix" in self.get_parents(root) or not "Matrix" in self.get_parents(root):
                            self.projectDataDict[self.get_parents(root)] =  root.attrib.get('name', root.text)
                    else :
                        if not md in self.get_parents(root).split('.'):
                            return

                        if "rows" in self.get_parents(root) :
                            self.matrixTagKey.append(md + ".rows." + root.attrib.get('name', root.text)) 
                        elif "columns" in self.get_parents(root):
                            self.matrixTagKey.append(md + ".columns." + root.attrib.get('name', root.text))
                        elif "element" in self.get_parents(root):
                            self.matrixTagKey.append(md + ".element." + str(self.matrixDetectionCountsElem[md])  + "." + root.attrib.get('name', root.text))
                            self.matrixDetectionCountsElem[md] += 1


        self.indent += 4
        for elem in root:
            self.printRecur(elem, ignoreElems)

        self.indent -= 4

    

                
        


    