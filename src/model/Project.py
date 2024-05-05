from src.model.Cluster import Cluster
from src.model.Idea import Idea

class Project :
    def __init__(self, projectData, triggerQuestion, genericQuestion, clustersTags, ideasTags):
        self.projectTagsDataDict = {}
        self.name = projectData.findChild('PrjName').getText()
        self.eventName = projectData.findChild('EventName').getText()
        self.eventLoc = projectData.findChild('eventLoc').getText()
        self.eventDates = projectData.findChild('eventDates').getText()
        self.ideaNameSingular = projectData.findChild('ideaNameSingular').getText()
        self.ideaNamePlural = projectData.findChild('ideaNamePlural').getText()
        self.sessType = projectData.findChild('sessType').getText()
        
        self.projectTagsDataDict['PrjName'] = self.name
        self.projectTagsDataDict['EventName'] = self.eventName
        self.projectTagsDataDict['eventLoc'] = self.eventLoc
        self.projectTagsDataDict['eventDates'] = self.eventDates
        self.projectTagsDataDict['ideaNameSingular'] = self.ideaNameSingular
        self.projectTagsDataDict['ideaNamePlural'] = self.ideaNamePlural
        self.projectTagsDataDict['sessType'] = self.sessType

        self.triggerQuestion = triggerQuestion.findChild('Name').getText()
        self.genericQuestion = genericQuestion.findChild('Name').getText()
        
        self.projectTagsDataDict['triggerQuestionName'] = self.triggerQuestion
        self.projectTagsDataDict['genericQuestionName'] = self.genericQuestion
        
        self.clusters = []
        
        for clusterTag in clustersTags:
            cluster = Cluster(clusterTag.find('Num').getText(), clusterTag.find('Name').getText())
            self.clusters.append(cluster)
            self.projectTagsDataDict['Cluster' + str(cluster.getNum()) + 'Num'] = cluster.getNum()
            self.projectTagsDataDict['Cluster' + str(cluster.getNum()) + 'Name'] = cluster.getName()
          
        self.ideas = []
        
        for ideaTag in ideasTags:
            idea = Idea(ideaTag.find('Num').getText(), ideaTag.find('IdeaText').getText(), ideaTag.find('classNo').getText(), ideaTag.find('votes').getText(), ideaTag.find('stat').getText(), ideaTag.find('clarification').getText())
            self.ideas.append(idea)
            self.projectTagsDataDict['Idea' + str(idea.getNum()) + 'Num'] = idea.getNum()
            self.projectTagsDataDict['Idea' + str(idea.getNum()) + 'Text'] = idea.getText()
            self.projectTagsDataDict['Idea' + str(idea.getNum()) + 'classNo'] = idea.getClassNo()
            self.projectTagsDataDict['Idea' + str(idea.getNum()) + 'votes'] = idea.getVotes()
            self.projectTagsDataDict['Idea' + str(idea.getNum()) + 'stat'] = idea.getStat()
            self.projectTagsDataDict['Idea' + str(idea.getNum()) + 'clarification'] = idea.getClarification()
            
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