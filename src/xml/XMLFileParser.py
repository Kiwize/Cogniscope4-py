#This file opens XMLs files from Concertina and Cognisope 3 to import them in Cogniscope 4
from src.model.Project import Project
from lxml import etree
import xml.etree.ElementTree as ET
from src.model.Idea import Idea

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

        self.currentIdeaObj = None
        self.currentIdeaNum = -100

    def openFile(self, filePath):
        self.project = Project()
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
            

        self.project.setDataDict(self.projectDataDict)
            
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
                                        if not int(root.attrib.get('name', root.text)) is self.currentIdeaNum:
                                            self.currentIdeaNum = int(root.attrib.get('name', root.text))
                                            self.currentIdeaObj = Idea(self.currentIdeaNum)
                                       
                                    if "IdeaText" in parents:
                                        self.currentIdeaObj.setText(root.attrib.get('name', root.text))
                                    elif "classNo" in parents:
                                        self.currentIdeaObj.setClusterNum(root.attrib.get('name', root.text))
                                    elif "votes" in parents:
                                        self.currentIdeaObj.setVotes(root.attrib.get('name', root.text))
                                    elif "stat" in parents:
                                        self.currentIdeaObj.setStat(root.attrib.get('name', root.text))
                                    elif "clarification" in parents:
                                        self.currentIdeaObj.setClarification(root.attrib.get('name', root.text))
                                    elif "author" in parents:
                                        self.currentIdeaObj.setAuthor(root.attrib.get('name', root.text))             
                                        
                                    if not self.currentIdeaObj is None and self.currentIdeaObj.isComplete():
                                        self.project.addIdea(self.currentIdeaObj)    

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

    def saveContentToXML(self):
        tree = ET.parse(self.currentFile)
        print("Current file : " + str(self.currentFile))
        root = tree.getroot()
        ideasTag = root.find('ideas')

        #save ideas
        for ideas in self.project.getIdeas():
            for idea in ideasTag.findall('idea'):
                if str(idea.find('Num').text) == str(ideas.getNum()):
                    print("Saving idea " + str(ideas.getNum()))
                    if not ideas.isDeleted():
                        idea.find('IdeaText').text = ideas.getText()       
                        idea.find('classNo').text = ideas.getClassNo()
                        idea.find('votes').text = ideas.getVotes()
                        idea.find('stat').text = ideas.getStat()
                        idea.find('clarification').text = ideas.getClarification()
                        idea.find('author').text = ideas.getAuthor()
                    else :
                        print("Deleting idea " + str(ideas.getNum()))
                        ideasTag.remove(idea)
                    break


        tree.write(self.currentFile, encoding='utf-8', xml_declaration=True)




    

                
        


    