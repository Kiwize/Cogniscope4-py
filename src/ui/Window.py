from tkinter import Tk, Menu, Frame
from src.cfg.Config import ConfigReader
from src.ui.FrameVersion import FrameVersion
from src.ui.FrameClarification import FrameClarification
from src.ui.FrameClustering import FrameClustering
from src.ui.FrameFirstVoting import FrameFirstVoting
from src.ui.FrameGeneration import FrameGeneration
from src.ui.FrameMapping import FrameMapping
from src.ui.FrameSecondVoting import FrameSecondVoting
from src.ui.FrameTriggeringQuestion import FrameTriggeringQuestion
from src.ui.FrameUserPreferences import FrameUserPreferences
from src.ui.FrameAdmin import FrameAdmin
from tkinter.filedialog import askopenfilename
from datetime import date, datetime
import platform

import webbrowser
from src.xml.XMLFileParser import XMLFileParser

class Window(Tk):

    def __init__(self, configReader: ConfigReader):
        Tk.__init__(self)
        self.openedProject = None
        self.configReader = configReader
        self.configReader.setWindow(self)
        self.xmlfileparser = XMLFileParser()


        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FrameVersion, FrameClarification, FrameClustering, FrameFirstVoting, FrameGeneration, FrameMapping, FrameSecondVoting, FrameTriggeringQuestion, FrameUserPreferences, FrameAdmin) :
            page_name = F.__name__
            frame = F(parent=container)
            self.frames[page_name] = frame
            
            if page_name == "FrameUserPreferences":
                frame.setUserPreference(self.configReader)
            elif page_name == "FrameAdmin":
                frame.setXMLFileParser(self.xmlfileparser)

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
            
        #Display the default frame    
        self.show_frame("FrameVersion")

        self.create_menu_bar()

        self.geometry("1280x800")
        self.title("Cogniscope 4")

    def show_frame(self, page_name):
        if page_name == "FrameAdmin":
            self.adminFrame.updateData()

        frame = self.frames[page_name]
        frame.tkraise()

    def create_menu_bar(self):
        self.menu_bar = Menu(self)

        self.menu_file = Menu(self.menu_bar, tearoff=0)
        self.menu_file.add_command(accelerator="Cmd+N")
        self.menu_file.add_command(accelerator="Cmd+O", command=self.open_file)
        self.menu_file.add_command(accelerator="Cmd+S", command=self.saveProject)
        self.menu_file.add_command(accelerator="Shift+Cmd+S")
        self.menu_file.add_separator()
        self.menu_file.add_command(accelerator="Cmd+X", command=self.quit)

        self.menu_bar.add_cascade(label="File", menu=self.menu_file)

        menu_edit = Menu(self.menu_bar, tearoff=0)
        menu_edit.add_command(label="Project")
        menu_edit.add_separator()
        menu_edit.add_command(label="Dialogue")
        menu_edit.add_command(label="Cluster Questions")
        menu_edit.add_command(label="Mapping Questions")
        menu_edit.add_separator()
        menu_edit.add_command(label="Preferences", command=lambda: self.show_frame("FrameUserPreferences"))
        menu_edit.add_command(label="Dialogue Admin", command=lambda: self.show_frame("FrameAdmin"))
        self.menu_bar.add_cascade(menu=menu_edit)

        self.menu_navigation = Menu(self.menu_bar, tearoff=0)
        self.menu_navigation.add_command(accelerator="Cmd+T", command=lambda: self.show_frame("FrameTriggeringQuestion"))
        self.menu_navigation.add_command(accelerator="Cmd+G", command=lambda: self.show_frame("FrameGeneration"))
        self.menu_navigation.add_command(accelerator="Cmd+L", command=lambda: self.show_frame("FrameClarification"))
        self.menu_navigation.add_command(accelerator="Cmd+V", command=lambda: self.show_frame("FrameFirstVoting"))
        self.menu_navigation.add_command(accelerator="Shift+Cmd+C", command=lambda: self.show_frame("FrameClustering"))
        self.menu_navigation.add_command(accelerator="Shift+Cmd+N", command=lambda: self.show_frame("FrameSecondVoting"))
        self.menu_navigation.add_command(accelerator="Cmd+M", command=lambda: self.show_frame("FrameMapping"))
        self.menu_bar.add_cascade(menu=self.menu_navigation)

        self.menu_reports = Menu(self.menu_bar, tearoff=0)
        self.menu_reports.add_command()
        self.menu_reports.add_command(label="Clarification")
        self.menu_reports.add_command(label="Clusters Table")
        self.menu_reports.add_command(label="First Voting")
        self.menu_reports.add_command(label="Second Voting")
        self.menu_reports.add_command(label="Voting Analysis")
        self.menu_reports.add_command(label="Map")
        self.menu_reports.add_command(label="Map Analysis")
        self.menu_bar.add_cascade(menu=self.menu_reports)

        self.menu_export = Menu(self.menu_bar, tearoff=0)
        self.menu_export.add_command(label="List of Ideas", command=lambda: self.exportListOfIdeas())
        self.menu_export.add_command(label="Clarifications")
        self.menu_export.add_command(label="Clusters Table")
        self.menu_export.add_command(label="First Voting")
        self.menu_export.add_command(label="Second Voting")
        self.menu_export.add_command(label="Map Data")
        self.menu_export.add_command(label="Matrix")
        self.menu_bar.add_cascade(menu=self.menu_export)

        self.menu_utilities = Menu(self.menu_bar, tearoff=0)
        self.menu_utilities.add_command(label="Print ideas")
        self.menu_utilities.add_command(label="Print Headings")
        self.menu_utilities.add_command(label="Print Timestamps")
        self.menu_bar.add_cascade(menu=self.menu_utilities)

        self.menu_help = Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(label="Visit Dialog Design Wiki", command=lambda: webbrowser.open("https://www.dialogicdesignscience.info/", new=0, autoraise=True))
        self.menu_help.add_command(label="Frequently Asked Questions", command=lambda: webbrowser.open("https://www.ekkotek.com/index.php/products/wisdom-tools/Cogniscope3", new=0, autoraise=True))
        self.menu_help.add_command(label="Download Manual", command=lambda: webbrowser.open("https://www.ekkotek.com/index.php/products/wisdom-tools/Cogniscope3", new=0, autoraise=True))
        self.menu_help.add_command(label="Version", command=lambda: self.show_frame("FrameVersion"))
        self.menu_bar.add_cascade(menu=self.menu_help)

        self.config(menu=self.menu_bar)
        
        self.updateTranslations()
        
    def updateTranslations(self):
        self.menu_bar.entryconfigure(1 if platform.system() == "Windows" else 0, label=self.configReader.getTranslation("MN_File"))
        
        self.menu_file.entryconfigure(0, label=self.configReader.getTranslation("MN_New"))
        self.menu_file.entryconfigure(1, label=self.configReader.getTranslation("MN_Open"))
        self.menu_file.entryconfigure(2, label=self.configReader.getTranslation("MN_Save"))
        self.menu_file.entryconfigure(3, label=self.configReader.getTranslation("MN_SaveAs"))
        self.menu_file.entryconfigure(5, label=self.configReader.getTranslation("MN_Exit"))
        
        self.menu_bar.entryconfigure(2 if platform.system() == "Windows" else 1, label=self.configReader.getTranslation("MN_Edit"))
        
        self.menu_bar.entryconfigure(3 if platform.system() == "Windows" else 2, label=self.configReader.getTranslation("MN_Navigation"))
        
        self.menu_navigation.entryconfigure(0, label=self.configReader.getTranslation("MN_TriggeringQuestion"))
        self.menu_navigation.entryconfigure(1, label=self.configReader.getTranslation("MN_Generation"))
        self.menu_navigation.entryconfigure(2, label=self.configReader.getTranslation("MN_Clarification"))
        self.menu_navigation.entryconfigure(3, label=self.configReader.getTranslation("MN_FirstVoting"))
        self.menu_navigation.entryconfigure(4, label=self.configReader.getTranslation("MN_Clustering"))
        self.menu_navigation.entryconfigure(5, label=self.configReader.getTranslation("MN_SecondVoting"))
        self.menu_navigation.entryconfigure(6, label=self.configReader.getTranslation("MN_Mapping"))
        
        self.menu_bar.entryconfigure(4 if platform.system() == "Windows" else 3, label=self.configReader.getTranslation("MN_Reports"))
        self.menu_reports.entryconfigure(0, label=self.configReader.getTranslation("MN_ListOfIdeas"))
        self.menu_reports.entryconfigure(1, label=self.configReader.getTranslation("MN_Clarifications"))
        self.menu_reports.entryconfigure(2, label=self.configReader.getTranslation("MN_ClustersTable"))
        self.menu_reports.entryconfigure(3, label=self.configReader.getTranslation("MN_FirstVoting"))
        self.menu_reports.entryconfigure(4, label=self.configReader.getTranslation("MN_SecondVoting"))
        self.menu_reports.entryconfigure(5, label=self.configReader.getTranslation("MN_VotingAnalysis"))
        self.menu_reports.entryconfigure(6, label=self.configReader.getTranslation("MN_Map"))
        self.menu_reports.entryconfigure(7, label=self.configReader.getTranslation("MN_MapAnalysis"))
        
        self.menu_bar.entryconfigure(5 if platform.system() == "Windows" else 4, label=self.configReader.getTranslation("MN_Export"))
        
        self.menu_export.entryconfigure(0, label=self.configReader.getTranslation("MN_ListOfIdeas"))
        self.menu_export.entryconfigure(1, label=self.configReader.getTranslation("MN_Clarifications"))
        self.menu_export.entryconfigure(2, label=self.configReader.getTranslation("MN_ClustersTable"))
        self.menu_export.entryconfigure(3, label=self.configReader.getTranslation("MN_FirstVoting"))
        self.menu_export.entryconfigure(4, label=self.configReader.getTranslation("MN_SecondVoting"))
        self.menu_export.entryconfigure(5, label=self.configReader.getTranslation("MN_MapData"))
        self.menu_export.entryconfigure(6, label=self.configReader.getTranslation("MN_Matrix"))
        
        self.menu_bar.entryconfigure(6 if platform.system() == "Windows" else 5, label=self.configReader.getTranslation("MN_Utilities"))
        
        self.menu_utilities.entryconfigure(0, label=self.configReader.getTranslation("MN_PrintIdeas"))
        self.menu_utilities.entryconfigure(1, label=self.configReader.getTranslation("MN_PrintHeadings"))
        self.menu_utilities.entryconfigure(2, label=self.configReader.getTranslation("MN_ExportTimestamps"))
        
        self.menu_bar.entryconfigure(7 if platform.system() == "Windows" else 6 , label=self.configReader.getTranslation("MN_Help"))
        
        self.menu_help.entryconfigure(0, label=self.configReader.getTranslation("MN_Wiki"))
        self.menu_help.entryconfigure(1, label=self.configReader.getTranslation("MN_FAQ"))
        self.menu_help.entryconfigure(2, label=self.configReader.getTranslation("MN_Manual"))
        self.menu_help.entryconfigure(3, label=self.configReader.getTranslation("MN_Version"))

    def quit(self):
        exit(1)

    def saveProject(self):
        self.xmlfileparser.saveContentToXML()

    def open_file(self):
        fn = askopenfilename()
        self.xmlfileparser = XMLFileParser()
        self.xmlfileparser.openFile(fn)
        self.openedProject = self.xmlfileparser.getProject()

        self.adminFrame = self.frames["FrameAdmin"]
        self.adminFrame.setXMLFileParser(self.xmlfileparser)
        self.adminFrame.updateData()

        self.generationIdeaFrame = self.frames["FrameGeneration"]
        self.generationIdeaFrame.loadProjectData(self.xmlfileparser.getProject())

        self.clarificationIdeaFrame = self.frames["FrameClarification"]
        self.clarificationIdeaFrame.loadProjectData(self.xmlfileparser.getProject())
        
    def exportListOfIdeas(self):
        if self.openedProject == None:
            print('ERR: Must open project first !')
            return
        
        filePrjName = self.openedProject.getName().replace(" ", "_")
        
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        
        with open('./exports/ListOfIdeas_' + filePrjName + "_" + str(date.today()) + "_" + str(current_time) + '.txt', 'a', encoding='utf8') as f :
            f.write("Project Title : " + self.openedProject.getName() + "\r")
            f.write("Dialog Title : " + self.openedProject.getEventName()+ "\r")
            f.write("Event Location : " + self.openedProject.getEventLoc()+ "\r")
            f.write("Date Created : TO ADD"+ "\r")
            f.write("Event Dates : " + self.openedProject.getEventDates()+ "\r"+ "\r")
            
            f.write('Triggering Question : ' + self.openedProject.getTriggeringQuestion()+ "\r"+ "\r")
            
            f.write('Clustering Questions :'+ "\r")
            
            for clusteringQuestion in self.openedProject.getClusters() :
                f.write(clusteringQuestion.getNum() + ". " + clusteringQuestion.getName()+ "\r")
                
            f.write("\r")
                
            f.write(self.getExportFooter())
                
            
            
    def getExportFooter(self):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        
        exportFooter = "Generated by the participants of " + self.openedProject.getEventName() + ": " + self.openedProject.getName() + " which took place at " + self.openedProject.getEventLoc() + " on " + self.openedProject.getEventDates()
        exportFooter = exportFooter + "\r"
        exportFooter = exportFooter + "Exported from Cogniscope4py on " + str(date.today()) + " at " + str(current_time)
        
        return exportFooter        


