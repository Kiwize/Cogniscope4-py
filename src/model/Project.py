from src.model.Cluster import Cluster
from src.model.Idea import Idea

class Project :
    def __init__(self, dict):
            
        self.projectTagsDataDict = dict
            
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
        return self.triggerQuestion
    
    def getGenericQuestion(self):
        return self.genericQuestion
    
    def getClusters(self):
        return self.clusters
    
    def getIdeas(self):
        return self.ideas