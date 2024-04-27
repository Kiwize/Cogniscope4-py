from tkinter import *

class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.create_menu_bar()

        self.geometry("1280x800")
        self.title("Cogniscope 4")

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", command=self.do_something)
        menu_file.add_command(label="Open", command=self.open_file)
        menu_file.add_command(label="Save", command=self.do_something)
        menu_file.add_command(label="Save as", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)

        menu_bar.add_cascade(label="File", menu=menu_file)

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="Project", command=self.do_something)
        menu_edit.add_separator()
        menu_edit.add_command(label="Dialogue", command=self.do_something)
        menu_edit.add_command(label="Cluster Questions", command=self.do_something)
        menu_edit.add_command(label="Mapping Questions", command=self.do_something)
        menu_bar.add_cascade(label="Edit", menu=menu_edit)

        menu_navigation = Menu(menu_bar, tearoff=0)
        menu_navigation.add_command(label="Triggering Question")
        menu_navigation.add_command(label="Generation")
        menu_navigation.add_command(label="Clarification")
        menu_navigation.add_command(label="First Voting")
        menu_navigation.add_command(label="Clustering")
        menu_navigation.add_command(label="Second Voting")
        menu_navigation.add_command(label="Mapping")
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
        menu_help.add_command(label="Version")
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.config(menu=menu_bar)

    def open_file(self):
        print("TODO")

    def do_something(self):
        print("TODO")

    def do_about(self):
        print("TODO")


window = Window()
window.mainloop()