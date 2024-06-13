from src.model.Idea import Idea

class Project :
    def __init__(self, dict = {}):
            
        self.projectTagsDataDict = dict
        self.ideas = []

    def addIdea(self, idea: Idea):
        for a in self.ideas:
            if a.getNum() is idea.getNum():
                return
            
        self.ideas.append(idea)

    def setDataDict(self, dict : dict):
        self.projectTagsDataDict = dict

    def getIdeas(self) -> list[Idea]:
        return self.ideas
    
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