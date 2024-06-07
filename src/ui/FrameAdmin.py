from tkinter import Frame, Label, Button
from src.xml.XMLFileParser import XMLFileParser
import customtkinter

class FrameAdmin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.xmlparser = None

        self.rowconfigure([0], weight=0)
        self.rowconfigure([1, 2], weight=2)
        self.columnconfigure([0, 1], weight=0)
        self.columnconfigure([2], weight=10)

        self.topButtonGrid = Frame(self)
        self.topButtonGrid.grid(column=2, row=0, sticky="news")

        
        self.rawButton = Button(self.topButtonGrid, text="Raw", command=lambda:self.displayTabIdeas("raw"))
        self.rawButton.grid(column=0, row=0)
        self.byIdeaNumButton = Button(self.topButtonGrid, text="By Idea Num", command=lambda:self.displayTabIdeas("byideanum"))
        self.byIdeaNumButton.grid(column=1, row=0)
        self.byVotesButton = Button(self.topButtonGrid, text="By Votes", command=lambda:self.displayTabIdeas("byvotes"))
        self.byVotesButton.grid(column=2, row=0)

        #============= Project DATA ================

        self.projectDataFrame = Frame(self, highlightthickness=1, highlightbackground="black")
        self.projectDataFrame.grid(column=0, row=1, columnspan=2, sticky="news")

        Label(self.projectDataFrame, text="prjName", anchor="w", justify="left").grid(column=0, row=0, sticky="news")
        Label(self.projectDataFrame, text="eventName", anchor="w", justify="left").grid(column=0, row=1, sticky="news")
        Label(self.projectDataFrame, text="eventLoc", anchor="w", justify="left").grid(column=0, row=2, sticky="news")

        self.prjName = Label(self.projectDataFrame, anchor="w", justify="left")
        self.prjName.grid(column=1, row=0, sticky="news")
        self.eventName = Label(self.projectDataFrame, anchor="w", justify="left")
        self.eventName.grid(column=1, row=1, sticky="news")
        self.eventLoc = Label(self.projectDataFrame, anchor="w", justify="left")
        self.eventLoc.grid(column=1, row=2, sticky="news")

        #==================== Project STATS ==========================

        self.projectStatsFrame = Frame(self, highlightthickness=1, highlightbackground="black")
        self.projectStatsFrame.grid(column=0, row=2, sticky="news")

        Label(self.projectStatsFrame, text="Num of Participants", anchor="w", justify="left").grid(column=0, row=0, sticky="news")
        Label(self.projectStatsFrame, text="Num of Ideas", anchor="w", justify="left").grid(column=0, row=1, sticky="news")
        Label(self.projectStatsFrame, text="ST1", anchor="w", justify="left").grid(column=0, row=2, sticky="news")
        Label(self.projectStatsFrame, text="ST2", anchor="w", justify="left").grid(column=0, row=3, sticky="news")
        Label(self.projectStatsFrame, text="Num of Clusters", anchor="w", justify="left").grid(column=0, row=4, sticky="news")
        Label(self.projectStatsFrame, text="Num of Ideas Mapped", anchor="w", justify="left").grid(column=0, row=5, sticky="news")

        self.numOfPartifipants = Label(self.projectStatsFrame, anchor="w", justify="left")
        self.numOfPartifipants.grid(column=1, row=0, sticky="news")
        self.numOfIdeas = Label(self.projectStatsFrame, anchor="w", justify="left")
        self.numOfIdeas.grid(column=1, row=1, sticky="news")
        self.ST1 = Label(self.projectStatsFrame, anchor="w", justify="left")
        self.ST1.grid(column=1, row=2, sticky="news")
        self.ST2 = Label(self.projectStatsFrame, anchor="w", justify="left")
        self.ST2.grid(column=1, row=3, sticky="news")
        self.numOfClusters = Label(self.projectStatsFrame, anchor="w", justify="left")
        self.numOfClusters.grid(column=1, row=4, sticky="news")
        self.numOfIdeasMapped = Label(self.projectStatsFrame, anchor="w", justify="left")
        self.numOfIdeasMapped.grid(column=1, row=5, sticky="news")


        #==================== Project CLUSTERS ===================

        self.projectClustersFrame = Frame(self, highlightthickness=1, highlightbackground="black")
        self.projectClustersFrame.grid(column=1, row=2, sticky="news")

        Label(self.projectClustersFrame, text="Cluster Num", anchor="w", justify="left").grid(column=0, row=0, sticky="news")
        Label(self.projectClustersFrame, text="Cluster Name", anchor="w", justify="left").grid(column=1, row=0, sticky="news")


        #==================== Project MATRICE ========================

        self.projectMatriceFrame = Frame(self, highlightthickness=1, highlightbackground="black")
        self.projectMatriceFrame.grid(column=2, row=2, sticky="news")

        for i in range(0, 50):
            self.projectMatriceFrame.grid_rowconfigure(i, weight=0)
            self.projectMatriceFrame.grid_columnconfigure(i, weight=0)

        Label(self.projectMatriceFrame, text="Project Matrix").grid(column=0, row=0)
        self.ISMMatrix = Label(self.projectMatriceFrame, text="No matrix opened...")
        self.ISMMatrix.grid(column=0, row=1)
        self.matrix = {}

        
        #==================== Tabular SCROLLABLE ==================

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid(column=2, row=1, sticky="news")  
        
        self.projectData = Label(self.scrollable_frame, text="No project opened...")
        self.projectData.grid(column=0, row=0, sticky="nesw")    
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def setXMLFileParser(self, xmlparser: XMLFileParser):
        self.xmlparser = xmlparser
        
    def updateData(self):
        #Clear previous data if any
        self.clearScrollableFrame()
        self.matrix.clear()

        for w in self.projectMatriceFrame.grid_slaves():
            w.grid_remove()
            w.destroy()

        for w in self.projectClustersFrame.grid_slaves():
            w.grid_remove()
            w.destroy()

        if self.xmlparser.getProject() != None :
            self.projectData.config(text="")
            self.project = self.xmlparser.getProject()
            self.dataDict = self.project.getProjectTagsDataDict()

            lastSelectedCluster = -1
            ideaCount = 0
            ideaMappedCount = 0
            clusterCount = 0

            key_mapping = {
                "PrjName": self.prjName,
                "eventLoc": self.eventLoc,
                "EventName": self.eventName
            }


            for key in self.dataDict:
                if "data.matrix.line" in str(key):
                    self.matrix[str(key)] = str(self.dataDict[key])

            lastMatrixId = -1
            matrixLineCount = 0

            for key in self.matrix:
                if "line.values.value" in key:
                    try:
                        if int(key.split(".")[5]) != lastMatrixId:
                            lastMatrixId = int(key.split(".")[5])

                            print("LINE ID : " + str(key))
                            matrixLineCount += 1
                            Label(self.projectMatriceFrame, text=str(matrixLineCount)).grid(column=matrixLineCount, row=0, sticky="news")
                            Label(self.projectMatriceFrame, text=str(matrixLineCount)).grid(column=0, row=matrixLineCount, sticky="news")

                            Label(self.projectMatriceFrame, text=self.matrix[key]).grid(column=1, row=matrixLineCount)
                        else:
                            Label(self.projectMatriceFrame, text=self.matrix[key]).grid(column=(int(key.split(".")[6]) + 1), row=matrixLineCount)

                    except IndexError:
                        print("ERR")

            #self.iterate_values(project.getProjectTagsDataDict(), i)    
            for key, val in self.project.getProjectTagsDataDict().items():
                if "IdeaText" in str(key) : ideaCount += 1
                elif "cluster.Name" in str(key) : clusterCount += 1

                if "idea.classNo" in str(key) :
                    ideaMappedCount += 1

                for k, widget in key_mapping.items():
                    if k in str(key):
                        widget.config(text=str(val))
                        break

                #print("Key : " + str(key) + "     Val : " + str(val))
                if "cluster.Num" in str(key):
                    Label(self.projectClustersFrame, text=str(val), anchor="w", justify="left").grid(column=0, row=int(val), sticky="news")
                    lastSelectedCluster = int(val)
                elif "cluster.Name" in str(key):
                    Label(self.projectClustersFrame, text=str(val), anchor="w", justify="left").grid(column=1, row=lastSelectedCluster, sticky="news")
                
        else :
            self.projectData = Label(self, text="No project opened...")

        self.displayTabIdeas("raw")

        self.numOfIdeas.config(text=str(ideaCount))
        self.numOfClusters.config(text=str(clusterCount))
        self.numOfIdeasMapped.config(text=str(ideaMappedCount))

        lastSelectedCluster += 2

        Label(self.projectClustersFrame, text="Ideas Selected for Mapping", anchor="w", justify="left").grid(column=0, row=lastSelectedCluster, sticky="news")
        Label(self.projectClustersFrame, text="Ideas Mapped", anchor="w", justify="left").grid(column=0, row=lastSelectedCluster + 1, sticky="news")

    def displayTabIdeas(self, method):
        self.clearScrollableFrame()

        Label(self.scrollable_frame, text="Idea Number").grid(column=0, row=0)
        Label(self.scrollable_frame, text="Number of Votes").grid(column=1, row=0)
        Label(self.scrollable_frame, text="Text").grid(column=2, row=0)

        #Modify this part to sort rows by votes / idea num or raw display
        i = 0
        self.ideasDict = {} #Contains array which represents ideas (num, text, votes)
        try :
            match method:
                case "byvotes":
                    ideaCount = 1

                    self.iterateOverIdeas()

                    ideaList = list(self.ideasDict.values())
                    ideaList.sort(key=lambda x: x[2], reverse=True)

                    for idea in ideaList:
                        Label(self.scrollable_frame, text=str(idea[0])).grid(column=0, row=ideaCount)     
                        Label(self.scrollable_frame, text=str(idea[1]), anchor="w", justify="left").grid(column=2, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[2])).grid(column=1, row=ideaCount)
                        ideaCount += 1

                case "byideanum":
                    ideaCount = 1

                    self.iterateOverIdeas()

                    ideaList = list(self.ideasDict.values())
                    ideaList.sort(key=lambda x: x[0], reverse=True)

                    for idea in ideaList:
                        Label(self.scrollable_frame, text=str(idea[0])).grid(column=0, row=ideaCount)     
                        Label(self.scrollable_frame, text=str(idea[1]), anchor="w", justify="left").grid(column=2, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[2])).grid(column=1, row=ideaCount)
                        ideaCount += 1
                    
                case _:
                    self.clearScrollableFrame()
                    for key, val in self.project.getProjectTagsDataDict().items():
                        if "idea" in str(key):
                            i = i + 1
                            if i % 2 == 0:
                                Label(self.scrollable_frame, text=key.replace("classNo", "clusterID"), anchor="w", justify="left", bg="#b5b5b5").grid(column=0, row=i, sticky="nswe")
                                Label(self.scrollable_frame, text=val, anchor="w", justify="left", bg="#b5b5b5").grid(column=1, row=i, sticky="nswe")
                            else :
                                Label(self.scrollable_frame, text=key.replace("classNo", "clusterID"), anchor="w", justify="left").grid(column=0, row=i, sticky="nswe")
                                Label(self.scrollable_frame, text=val, anchor="w", justify="left").grid(column=1, row=i, sticky="nswe")

        except AttributeError :
            print("No project opened !")

    def iterateOverIdeas(self):
        lastIdeaNum = -1
        self.ideasDict = {}
        for key, val in self.project.getProjectTagsDataDict().items():
            if "idea" in key:
                if "Num" in key and int(key.split(".")[4]) != lastIdeaNum:
                    lastIdeaNum = int(key.split(".")[4])
                    self.ideasDict[lastIdeaNum] = [lastIdeaNum]
                elif "IdeaText" in key:
                    self.ideasDict[lastIdeaNum].append(str(val))
                elif "votes" in key:
                    self.ideasDict[lastIdeaNum].append(str(val))

    def clearScrollableFrame(self):
        for label in self.scrollable_frame.grid_slaves():
            label.grid_forget() 


