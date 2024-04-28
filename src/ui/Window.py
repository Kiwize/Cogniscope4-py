from tkinter import Tk, Menu, Frame
from src.ui.FrameVersion import FrameVersion
from src.ui.FrameClarification import FrameClarification
from src.ui.FrameClustering import FrameClustering
from src.ui.FrameFirstVoting import FrameFirstVoting
from src.ui.FrameGeneration import FrameGeneration
from src.ui.FrameMapping import FrameMapping
from src.ui.FrameSecondVoting import FrameSecondVoting
from src.ui.FrameTriggeringQuestion import FrameTriggeringQuestion

class Window(Tk):

    def __init__(self, configReader):
        Tk.__init__(self)
        self.configReader = configReader


        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FrameVersion, FrameClarification, FrameClustering, FrameFirstVoting, FrameGeneration, FrameMapping, FrameSecondVoting, FrameTriggeringQuestion) :
            page_name = F.__name__
            frame = F(parent=container)
            self.frames[page_name] = frame

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
        frame = self.frames[page_name]
        frame.tkraise()

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", accelerator="⌘N", command=self.do_something)
        menu_file.add_command(label="Open", accelerator="⌘O", command=self.open_file)
        menu_file.add_command(label="Save", accelerator="⌘S", command=self.do_something)
        menu_file.add_command(label="Save as", accelerator="⇧⌘S", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", accelerator="⌘X", command=self.quit)

        menu_bar.add_cascade(label=self.configReader.getTranslation("MN_File"), menu=menu_file)

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Project", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Dialogue", command=self.do_something)
        menu_edit.add_command(label="Cluster Questions", command=self.do_something)
        menu_edit.add_command(label="Mapping Questions", command=self.do_something)
        menu_bar.add_cascade(label="Edit", menu=menu_edit)

        menu_navigation = Menu(menu_bar, tearoff=0)
        menu_navigation.add_command(label="Triggering Question", accelerator="⌘T", command=lambda: self.show_frame("FrameTriggeringQuestion"))
        menu_navigation.add_command(label="Generation", accelerator="⌘G", command=lambda: self.show_frame("FrameGeneration"))
        menu_navigation.add_command(label="Clarification", accelerator="⌘L", command=lambda: self.show_frame("FrameClarification"))
        menu_navigation.add_command(label="First Voting", accelerator="⌘V", command=lambda: self.show_frame("FrameFirstVoting"))
        menu_navigation.add_command(label="Clustering", accelerator="⇧⌘C", command=lambda: self.show_frame("FrameClustering"))
        menu_navigation.add_command(label="Second Voting", accelerator="⇧⌘N", command=lambda: self.show_frame("FrameSecondVoting"))
        menu_navigation.add_command(label="Mapping", accelerator="⌘M", command=lambda: self.show_frame("FrameMapping"))
        menu_bar.add_cascade(label="Navigation", menu=menu_navigation)

        menu_reports = Menu(menu_bar, tearoff=0)
        menu_reports.add_command(label="List of Ideas")
        menu_reports.add_command(label="Clarification")
        menu_reports.add_command(label="Clusters Table")
        menu_reports.add_command(label="First Voting")
        menu_reports.add_command(label="Second Voting")
        menu_reports.add_command(label="Voting Analysis")
        menu_reports.add_command(label="Map")
        menu_reports.add_command(label="Map Analysis")
        menu_bar.add_cascade(label="Reports", menu=menu_reports)

        menu_export = Menu(menu_bar, tearoff=0)
        menu_export.add_command(label="List of Ideas")
        menu_export.add_command(label="Clarifications")
        menu_export.add_command(label="Clusters Table")
        menu_export.add_command(label="First Voting")
        menu_export.add_command(label="Second Voting")
        menu_export.add_command(label="Map Data")
        menu_export.add_command(label="Matrix")
        menu_bar.add_cascade(label="Export", menu=menu_export)

        menu_utilities = Menu(menu_bar, tearoff=0)
        menu_utilities.add_command(label="Print ideas")
        menu_utilities.add_command(label="Print Headings")
        menu_utilities.add_command(label="Print Timestamps")
        menu_bar.add_cascade(label="Utilities", menu=menu_utilities)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="Visit Dialog Design Wiki")
        menu_help.add_command(label="Frequently Asked Questions")
        menu_help.add_command(label="Download Manual")
        menu_help.add_command(label="Version", command=lambda: self.show_frame("FrameVersion"))
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.config(menu=menu_bar)

    def quit(self):
        exit(1)

    def open_file(self):
        print("TODO")

    def do_something(self):
        print("TODO")

    def do_about(self):
        print("TODO")

