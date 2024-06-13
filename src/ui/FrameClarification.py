from tkinter import Frame, Label, Button, messagebox
from tkinter.simpledialog import askstring
from src.ui.components.RoundedButton import RoundedButton
from src.ui.components.TextManager import TextManager
from src.model.Idea import Idea

class FrameClarification(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.ideas = []
        self.selectedIdea = None
        self.project = None

        self.frame_bg_color = "#dae8fc"

        self.grid_columnconfigure([0, 1, 3, 4, 5], weight=0)
        self.grid_columnconfigure([2], weight=5)

        self.grid_rowconfigure([2], weight=5)

        self.title = Label(self, text="...", font="Helvetica 18 bold")
        self.title.grid(column=0, row=0, columnspan=3)

        self.currentSelectedideaClarification = Label(self, text="...", font="Helvetica 15")
        self.currentSelectedideaClarification.grid(column=0, row=1, sticky="w", pady=5, padx=10)

        self.navigationButtons = Frame(self)
        self.navigationButtons.grid(column=0, row=5, columnspan=3)

        self.previousButton = RoundedButton(self.navigationButtons, text="| <", font="Helvetica 12 bold", minwidth=20, outline_color="#f0f0f0", fill_color="#f0f0f0", command=lambda: self.previousIdea())
        self.previousButton.grid(column=0, row=0, sticky="e")
        self.previousButton.configure(bg="#f0f0f0")

        self.nextButton = RoundedButton(self.navigationButtons, text="> |", font="Helvetica 12 bold",minwidth=20, outline_color="#f0f0f0", fill_color="#f0f0f0", command=lambda: self.nextIdea())
        self.nextButton.grid(column=1, row=0, sticky="w")
        self.nextButton.configure(bg="#f0f0f0")

        self.actionButtonsFrame = Frame(self, bg="#f0f0f0")
        self.actionButtonsFrame.grid(column=0, row=3,columnspan=3, sticky="news")

        self.deleteButton = RoundedButton(self.actionButtonsFrame, corner_radius=0, text="Delete", text_color="white", outline_color="#dd0000", fill_color="#dd0000", hover_color="#bb0000", command=lambda: self.deleteIdea())
        self.deleteButton.grid(column=1, row=0, sticky="w")
        self.deleteButton.configure(bg="#f0f0f0")

        self.saveButton = RoundedButton(self.actionButtonsFrame, text="Save",corner_radius=0, text_color="white", outline_color="#4898e8", fill_color="#4898e8", hover_color="#30659b", command=lambda: self.saveIdeaToPDF())
        self.saveButton.grid(column=0, row=0, sticky="w")

        self.authorLabel = Label(self.actionButtonsFrame, text="...", font="Helvetica 12")
        self.authorLabel.grid(column=2, row=0, sticky="news")

        self.addAuthorButton = RoundedButton(self.actionButtonsFrame, text="Add Author", corner_radius=0, text_color="white", outline_color="#4898e8", fill_color="#4898e8", hover_color="#30659b", command=lambda: self.addAuthor())

        self.actionButtonsFrame.grid_columnconfigure([0, 1, 3], weight=0)
        self.actionButtonsFrame.grid_columnconfigure(2, weight=5)

        self.addNewButton = RoundedButton(self.actionButtonsFrame, text="Add New",corner_radius=0, text_color="white", outline_color="#4898e8", fill_color="#4898e8", hover_color="#30659b", command=lambda: self.saveIdeaToPDF())
        self.addNewButton.grid(column=3, row=0, sticky="e")
        self.addNewButton.configure(bg="#f0f0f0")

        self.ideaClarification = Label(self, text="No project opened...", highlightbackground="gray", highlightthickness=2, bg="white", font="Helvetica 17")
        self.ideaClarification.grid(column=0, row=2, sticky="news", columnspan=3, padx=8)

        self.ideaNavigationBar = Frame(self)
        self.ideaNavigationBar.configure(bg="white", background="white")
        self.ideaNavigationBar.grid(column=0, row=4, pady=6, columnspan=3)

    def loadProjectIdeas(self, ideas: list[Idea]) -> None:
        self.ideas = ideas
        firstIdea = ideas[0]
        self.selectedIdea = firstIdea
        self.currentSelectedideaClarification.configure(text="Characteristic " + str(self.selectedIdea.getNum()))

        self.ideaNavigationBar.grid_rowconfigure(0, minsize=30)
        self.drawButtons()

        self.showIdea(firstIdea)

    def loadProjectData(self, project):
        self.project = project
        self.loadProjectIdeas(project.getIdeas())
        TextManager.adjust_label_font(self.title, self.selectedIdea.getText(), max_font_size=25)

    def drawButtons(self):
        i = 0
        for w in self.ideaNavigationBar.grid_slaves():
            w.grid_remove()
            w.destroy()

        self.grid_columnconfigure([0, 2], weight=0)
        self.grid_columnconfigure([1], weight=5)

        self.grid_rowconfigure([2], weight=5)

        for idea in self.ideas:
            if not idea.isDeleted():
                self.ideaNavigationBar.grid_columnconfigure(i, minsize=30)
                RoundedButton(self.ideaNavigationBar, text=str(idea.getNum()), command=lambda a=idea: self.showIdea(a), text_color="#a1caf3", outline_color="#f0f0f0", minwidth=40, fill_color="#f0f0f0", hover_color="#f0f0f0", font="Helvetica 21 bold" if self.selectedIdea.getNum() is idea.getNum() else "Helvetica 13").grid(column=i, row=0, sticky="news")
                i += 1

    def previousIdea(self):
        self.showIdea(self.findPreviousIdeaInList())
    
    def nextIdea(self):
        self.showIdea(self.findNextIdeaInList())
    
    def findNextIdeaInList(self) -> Idea:
        found = False

        for a in self.ideas:
            if found: 
                break

            found = True if a.getNum() is self.selectedIdea.getNum() else False

        return a

    def findPreviousIdeaInList(self) -> Idea:
        lastIdea = None

        for a in self.ideas:
            if not a is None:
                if a.getNum() is self.selectedIdea.getNum():
                    return lastIdea if not lastIdea is None else a

            lastIdea = a

    
    def showIdea(self, idea : Idea):
        self.selectedIdea = idea

        TextManager.adjust_label_font(self.title, idea.getText(), max_font_size=25, availablewidth=1100)
        TextManager.adjust_label_font(self.ideaClarification, idea.getClarification(), max_font_size=30, availablewidth=1100)
        self.currentSelectedideaClarification.configure(text="Characteristic " + str(self.selectedIdea.getNum()))
        if idea.getAuthor() is None:
            self.authorLabel.grid_remove()
            self.addAuthorButton.grid(column=2, row=0)
        else:
            if isinstance(self.actionButtonsFrame.grid_slaves(column=2, row=0)[0], RoundedButton):
                self.addAuthorButton.grid_remove()
                self.authorLabel.grid(column=2, row=0)
            self.authorLabel.configure(text="Author : " + str(self.selectedIdea.getAuthor()))
        self.drawButtons()
        #print(self.selectedIdea.getText() + "   " + str(self.selectedIdea.getNum()))


