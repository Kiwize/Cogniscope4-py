


class Project :
    def __init__(self, projectData, triggerQuestion, genericQuestion):
        self.name = projectData.findChild('PrjName').getText()
        self.eventName = projectData.findChild('EventName').getText()
        self.eventLoc = projectData.findChild('eventLoc').getText()
        self.eventDates = projectData.findChild('eventDates').getText()
        self.ideaNameSingular = projectData.findChild('ideaNameSingular').getText()
        self.ideaNamePlural = projectData.findChild('ideaNamePlural').getText()
        self.sessType = projectData.findChild('sessType').getText()

        self.triggerQuestion = triggerQuestion.findChild('Name').getText()
        self.genericQuestion = genericQuestion.findChild('Name').getText()
        
        self.clusters = []
        self.ideas = []

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