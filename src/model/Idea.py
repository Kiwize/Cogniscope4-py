

class Idea:

    def __init__(self, num, text, classNo, votes, stat, clarification):
        self.num = num
        self.text = text
        self.classNo = classNo
        self.votes = votes
        self.stat = stat
        self.clarification = clarification


    def getNum(self):
        return self.num
    
    def getText(self):
        return self.text
    
    def getClassNo(self):
        return self.classNo
    
    def getVotes(self):
        return self.votes
    
    def getStat(self):
        return self.stat
    
    def getClarification(self):
        return self.clarification