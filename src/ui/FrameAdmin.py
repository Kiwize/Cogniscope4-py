from tkinter import Frame, Label, Button
from src.xml.XMLFileParser import XMLFileParser
from src.ui.components.RoundedButton import RoundedButton
import customtkinter

class FrameAdmin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.xmlparser = None

        self.rowconfigure([0], weight=0)
        self.rowconfigure([1, 3], weight=2)
        self.rowconfigure([2], weight=0)

        self.columnconfigure([0, 1], weight=0)
        self.columnconfigure([2], weight=10)

        self.topButtonGrid = Frame(self)
        self.topButtonGrid.grid(column=2, row=0, sticky="news")

        frame_bg_color = "#dae8fc"
        
        self.rawButton = RoundedButton(self.topButtonGrid, text="Raw", command=lambda:self.displayTabIdeas("raw"))
        self.rawButton.grid(column=0, row=0)
        self.configure(bg=frame_bg_color)

        self.byIdeaNumButton = RoundedButton(self.topButtonGrid, text="By Idea Num", command=lambda:self.displayTabIdeas("byideanum"))
        self.byIdeaNumButton.grid(column=1, row=0)
        self.byVotesButton = RoundedButton(self.topButtonGrid, text="By Votes", command=lambda:self.displayTabIdeas("byvotes"))
        self.byVotesButton.grid(column=2, row=0)

        #============= Project DATA ================

        self.projectDataFrame = Frame(self, highlightthickness=3, highlightbackground="white", bg=frame_bg_color)
        self.projectDataFrame.grid(column=0, row=1, columnspan=2, sticky="news")
        self.projectDataFrame.columnconfigure(1, minsize=60)

        Label(self.projectDataFrame, text="prjName", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=0, sticky="news")
        Label(self.projectDataFrame, text="eventName", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=1, sticky="news")
        Label(self.projectDataFrame, text="eventLoc", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=2, sticky="news")

        self.prjName = Label(self.projectDataFrame, anchor="w", justify="left", bg="white", highlightbackground="black", highlightthickness=2)
        self.prjName.grid(column=1, row=0, sticky="news", pady=4)
        self.eventName = Label(self.projectDataFrame, anchor="w", justify="left", bg="white", highlightbackground="black", highlightthickness=2)
        self.eventName.grid(column=1, row=1, sticky="news", pady=4)
        self.eventLoc = Label(self.projectDataFrame, anchor="w", justify="left", bg="white", highlightbackground="black", highlightthickness=2)
        self.eventLoc.grid(column=1, row=2, sticky="news", pady=4)

        #==================== Project STATS ==========================

        Label(self, text="Project Stats", bg=frame_bg_color, font="Helvetica 10 bold").grid(column=0, row=2, sticky="news")

        self.projectStatsFrame = Frame(self, highlightthickness=3, highlightbackground="white", bg=frame_bg_color)
        self.projectStatsFrame.grid(column=0, row=3, sticky="news")

        self.projectStatsFrame.columnconfigure(1, minsize=35)

        Label(self.projectStatsFrame, text="Num of Participants", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=0, sticky="news")
        Label(self.projectStatsFrame, text="Num of Ideas", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=1, sticky="news")
        Label(self.projectStatsFrame, text="ST1", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=2, sticky="news")
        Label(self.projectStatsFrame, text="ST2", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=3, sticky="news")
        Label(self.projectStatsFrame, text="Num of Clusters", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=4, sticky="news")
        Label(self.projectStatsFrame, text="Num of Ideas Mapped", anchor="w", justify="left", bg=frame_bg_color).grid(column=0, row=5, sticky="news")

        self.numOfPartifipants = Label(self.projectStatsFrame, bg="white", highlightbackground="black", highlightthickness=2)
        self.numOfPartifipants.grid(column=1, row=0, sticky="news", pady=4)
        self.numOfIdeas = Label(self.projectStatsFrame, bg="white", highlightbackground="black", highlightthickness=2)
        self.numOfIdeas.grid(column=1, row=1, sticky="news", pady=4)
        self.ST1 = Label(self.projectStatsFrame, bg="white", highlightbackground="black", highlightthickness=2)
        self.ST1.grid(column=1, row=2, sticky="news", pady=4)
        self.ST2 = Label(self.projectStatsFrame, bg="white", highlightbackground="black", highlightthickness=2)
        self.ST2.grid(column=1, row=3, sticky="news", pady=4)
        self.numOfClusters = Label(self.projectStatsFrame, bg="white", highlightbackground="black", highlightthickness=2)
        self.numOfClusters.grid(column=1, row=4, sticky="news", pady=4)
        self.numOfIdeasMapped = Label(self.projectStatsFrame, bg="white", highlightbackground="black", highlightthickness=2)
        self.numOfIdeasMapped.grid(column=1, row=5, sticky="news", pady=4)


        #==================== Project CLUSTERS ===================

        Label(self, text="Project Clusters", bg=frame_bg_color, font="Helvetica 10 bold").grid(column=1, row=2, sticky="news")

        self.projectClustersFrame = Frame(self, highlightthickness=3, highlightbackground="white", bg=frame_bg_color)
        self.projectClustersFrame.grid(column=1, row=3, sticky="news")

        Label(self.projectClustersFrame, text="Cluster Num", anchor="w", justify="left", bg="#dae8fc").grid(column=0, row=0, sticky="news")
        Label(self.projectClustersFrame, text="Cluster Name", anchor="w", justify="left", bg="#dae8fc").grid(column=1, row=0, sticky="news")

        #==================== Project MATRICE ========================

        self.projectMatriceFrame = Frame(self, highlightthickness=3, highlightbackground="white", bg=frame_bg_color)
        self.projectMatriceFrame.grid(column=2, row=3, sticky="news")

        Label(self, text="Project Matrix", bg=frame_bg_color, font="Helvetica 10 bold").grid(column=2, row=2, sticky="news")

        for i in range(0, 50):
            self.projectMatriceFrame.grid_rowconfigure(i, weight=0)
            self.projectMatriceFrame.grid_columnconfigure(i, weight=0)

        Label(self.projectMatriceFrame, text="Project Matrix", bg=frame_bg_color).grid(column=0, row=0)
        self.ISMMatrix = Label(self.projectMatriceFrame, text="No matrix opened...", bg=frame_bg_color)
        self.ISMMatrix.grid(column=0, row=1)
        self.matrix = {}

        
        #==================== Tabular SCROLLABLE ==================

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, bg_color=frame_bg_color, corner_radius=0, fg_color=frame_bg_color, border_color="white", border_width=3)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid(column=2, row=1, sticky="news")  
        
        self.projectData = Label(self.scrollable_frame, text="No project opened...", bg=frame_bg_color)
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
                self.projectMatriceFrame.columnconfigure(matrixLineCount, minsize=20)
                self.projectMatriceFrame.rowconfigure(matrixLineCount, minsize=20)
                if "line.values.value" in key:
                    try:
                        if int(key.split(".")[5]) != lastMatrixId:
                            lastMatrixId = int(key.split(".")[5])

                            print("LINE ID : " + str(key))
                            matrixLineCount += 1
                            Label(self.projectMatriceFrame, text=str(matrixLineCount), bg="white", highlightbackground="#accb4d", highlightthickness=1).grid(column=matrixLineCount, row=0, sticky="news")
                            Label(self.projectMatriceFrame, text=str(matrixLineCount), bg="white", highlightbackground="#accb4d", highlightthickness=1).grid(column=0, row=matrixLineCount, sticky="news")

                            Label(self.projectMatriceFrame, text=self.matrix[key], bg="white" if matrixLineCount % 2 == 0 else "#eaf2d3", highlightbackground="#accb4d", highlightthickness=1).grid(column=1, row=matrixLineCount, sticky="news")
                        else:
                            Label(self.projectMatriceFrame, text=self.matrix[key], bg="white" if matrixLineCount % 2 == 0 else "#eaf2d3", highlightbackground="#accb4d", highlightthickness=1).grid(column=(int(key.split(".")[6]) + 1), row=matrixLineCount, sticky="news")

                    except IndexError:
                        print("ERR")

            #self.iterate_values(project.getProjectTagsDataDict(), i)    
            c = 0
            Label(self.projectClustersFrame, text="Cluster Num", anchor="w", justify="left", bg="#dae8fc").grid(column=0, row=0, sticky="news")
            Label(self.projectClustersFrame, text="Cluster Name", anchor="w", justify="left", bg="#dae8fc").grid(column=1, row=0, sticky="news")
            for key, val in self.project.getProjectTagsDataDict().items():
                if "cluster.Name" in str(key) : clusterCount += 1

                for k, widget in key_mapping.items():
                    if k in str(key):
                        widget.config(text=str(val))
                        break

                #print("Key : " + str(key) + "     Val : " + str(val))
                if "cluster.Num" in str(key):
                    c +=1
                    Label(self.projectClustersFrame, text=str(val), anchor="w", justify="left", bg="white" if c % 2 == 0 else "#eaf2d3", highlightbackground="#a7c842", highlightthickness=1).grid(column=0, row=c, sticky="news")
                    lastSelectedCluster = int(val)       
                elif "cluster.Name" in str(key):
                    Label(self.projectClustersFrame, text=str(val), anchor="w", justify="left", bg="white" if c % 2 == 0 else "#eaf2d3", highlightbackground="#a7c842", highlightthickness=1).grid(column=1, row=c, sticky="news")
                
        else :
            self.projectData = Label(self, text="No project opened...")

        self.displayTabIdeas("raw")

        self.numOfIdeas.config(text=str(len(self.project.getIdeas())))
        self.numOfClusters.config(text=str(clusterCount))
        self.numOfIdeasMapped.config(text=str(len(self.project.getIdeas())))

        lastSelectedCluster += 2

        Label(self.projectClustersFrame, text="Ideas Selected\rfor Mapping", anchor="w", justify="left", bg="#dae8fc").grid(column=0, row=lastSelectedCluster, sticky="news", pady=5)
        Label(self.projectClustersFrame, text="Ideas Mapped", anchor="w", justify="left", bg="#dae8fc").grid(column=0, row=lastSelectedCluster + 1, sticky="news", pady=4)

        Label(self.projectClustersFrame, text=" ", anchor="w", justify="left", bg="white", highlightbackground="black", highlightthickness=2).grid(column=1, row=lastSelectedCluster, sticky="news", pady=5, padx=2)
        Label(self.projectClustersFrame, text=" ", anchor="w", justify="left", bg="white", highlightbackground="black", highlightthickness=2).grid(column=1, row=lastSelectedCluster + 1, sticky="news", pady=4, padx=2)

    def displayTabIdeas(self, method):
        self.clearScrollableFrame()

        hg_color = "#accb4d"
        bg_color = "#a7c942"
        odd_bg_color = "#eaf2d3"

        Label(self.scrollable_frame, text="Idea Number", highlightthickness=1, highlightbackground=hg_color, bg=bg_color).grid(column=0, row=0, sticky="news")
        Label(self.scrollable_frame, text="Number of Votes", highlightthickness=1, highlightbackground=hg_color, bg=bg_color).grid(column=1, row=0, sticky="news")
        Label(self.scrollable_frame, text="Text", highlightthickness=1, highlightbackground=hg_color, bg="#99ccff").grid(column=2, row=0, sticky="news")

        #Modify this part to sort rows by votes / idea num or raw display
        self.ideasDict = {} #Contains array which represents ideas (num, text, votes)
        try :
            match method:
                case "byvotes":
                    ideaCount = 1

                    self.iterateOverIdeas()
                    self.scrollable_frame.columnconfigure([0, 1], weight=0)
                    self.scrollable_frame.columnconfigure([2], weight=2)

                    ideaList = list(self.ideasDict.values())
                    ideaList.sort(key=lambda x: x[3], reverse=True)

                    for idea in ideaList:
                        Label(self.scrollable_frame, text=str(idea[0]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=0, row=ideaCount, sticky="news")     
                        Label(self.scrollable_frame, text=str(idea[1]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color, anchor="w", justify="left").grid(column=2, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[3]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=1, row=ideaCount, sticky="news")
                        ideaCount += 1

                case "byideanum":
                    ideaCount = 1

                    self.iterateOverIdeas()
                    self.scrollable_frame.columnconfigure([0, 1], weight=0)
                    self.scrollable_frame.columnconfigure([2], weight=2)

                    ideaList = list(self.ideasDict.values())
                    ideaList.sort(key=lambda x: x[0], reverse=True)

                    for idea in ideaList:
                        Label(self.scrollable_frame, text=str(idea[0]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=0, row=ideaCount, sticky="news")     
                        Label(self.scrollable_frame, text=str(idea[1]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color, anchor="w", justify="left").grid(column=2, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[3]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=1, row=ideaCount, sticky="news")
                        ideaCount += 1
                    
                case _:
                    ideaCount = 1
                    self.clearScrollableFrame()
                    self.scrollable_frame.columnconfigure([0, 1, 2, 3], weight=0)
                    self.scrollable_frame.columnconfigure([4, 5], weight=3)

                    Label(self.scrollable_frame, text="Idea Number", highlightthickness=1, highlightbackground=hg_color, bg=bg_color).grid(column=0, row=0, sticky="news")
                    Label(self.scrollable_frame, text="Number of Votes", highlightthickness=1, highlightbackground=hg_color, bg=bg_color).grid(column=1, row=0, sticky="news")
                    Label(self.scrollable_frame, text="State", highlightthickness=1, highlightbackground=hg_color, bg="#99ccff").grid(column=2, row=0, sticky="news")
                    Label(self.scrollable_frame, text="Cluster", highlightthickness=1, highlightbackground=hg_color, bg="#99ccff").grid(column=3, row=0, sticky="news")
                    Label(self.scrollable_frame, text="Text", highlightthickness=1, highlightbackground=hg_color, bg="#99ccff").grid(column=4, row=0, sticky="news")
                    Label(self.scrollable_frame, text="Clarification", highlightthickness=1, highlightbackground=hg_color, bg="#99ccff").grid(column=5, row=0, sticky="news")

                    self.iterateOverIdeas()

                    ideaList = list(self.ideasDict.values())
                    ideaList.sort(key=lambda x: x[0], reverse=False)

                    for idea in ideaList:               
                        Label(self.scrollable_frame, text=str(idea[0]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=0, row=ideaCount, sticky="news")     
                        Label(self.scrollable_frame, text=str(idea[3]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=1, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[4]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=2, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[2]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color).grid(column=3, row=ideaCount, sticky="news")
                        Label(self.scrollable_frame, text=str(idea[1]), highlightthickness=1, highlightbackground=hg_color, bg="white" if ideaCount % 2 == 0 else odd_bg_color, justify="left", anchor="w").grid(column=4, row=ideaCount, sticky="news")
                        ideaCount += 1
                        

        except AttributeError :
            print("No project opened !")

    def iterateOverIdeas(self):
        self.ideasDict = {}
        for idea in self.project.getIdeas():
            self.ideasDict[idea.getNum()] = [idea.getNum(), idea.getText(), idea.getClassNo(), idea.getVotes(), idea.getStat()]

    def clearScrollableFrame(self):
        for label in self.scrollable_frame.grid_slaves():
            label.grid_forget() 


