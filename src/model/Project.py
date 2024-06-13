from src.model.Idea import Idea

class Project :
    def __init__(self, dict = {}):
            
        self.projectTagsDataDict = dict
        self.ideas = []
        self.matrix = []
        self.indices = []

    def addIdea(self, idea: Idea):
        for a in self.ideas:
            if a.getNum() is idea.getNum():
                return
            
        self.ideas.append(idea)

    def setDataDict(self, dict : dict):
        self.projectTagsDataDict = dict

    def setMatrix(self, matrix, indices):
        self.matrix = matrix
        self.indices = indices

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                print(matrix[row][col], end=" ")
            print()

        for i in indices:
            print(i, end=" ")
        print()

    def getIdeas(self) -> list[Idea]:
        return self.ideas
    
    def getMatrix(self):
        return self.matrix
    
    def getIndices(self):
        return self.indices
    
    def deleteIdeaFromNum(self, num):
        for idea in self.ideas:
            print(idea.getNum())
            if str(idea.getNum()) == str(num):
                idea.delete()
                print("Deleting idea " + str(num))

    def getProjectTagsDataDict(self):
        return self.projectTagsDataDict

    def getName(self):
        return self.name
    
    def getEventName(self):
        return self.eventName
    
    def getEventLoc(self):
        return self.eventLoc
    
    def getEventDates(self):
        return self.eventDates
    
    def getIdeaNameSingular(self):
        return self.ideaNameSingular
    
    def getIdeaNamePlural(self):
        return self.ideaNamePlural
    
    def getSessType(self):
        return self.sessType
    
    def getTriggeringQuestion(self):
        return self.projectTagsDataDict["data.trigQ.Name"]
    
    def getGenericQuestion(self):
        return self.genericQuestion
    
    def getClusters(self):
        return self.clusters