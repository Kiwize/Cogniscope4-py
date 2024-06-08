from tkinter import Frame, Label, Button
from src.ui.components.RoundedButton import RoundedButton
from src.model.Idea import Idea

class FrameGeneration(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.ideas = []
        self.selectedIdea = None

        self.frame_bg_color = "#dae8fc"
        self.configure(bg=self.frame_bg_color)

        self.grid_columnconfigure([0, 2], weight=0)
        self.grid_columnconfigure([1], weight=5)

        self.grid_rowconfigure([1], weight=5)

        self.title = Label(self, text="Idea Generation", font="Helvetica 18 bold", bg=self.frame_bg_color)

        self.previousButton = RoundedButton(self, text="<", command=lambda: self.previousIdea())
        self.previousButton.grid(column=0, row=2)
        self.previousButton.configure(bg=self.frame_bg_color)

        self.nextButton = RoundedButton(self, text=">", command=lambda: self.nextIdea())
        self.nextButton.grid(column=2, row=2)
        self.nextButton.configure(bg=self.frame_bg_color)

        self.ideaLabel = Label(self, text="No project opened...", highlightbackground="black", highlightthickness=2, bg=self.frame_bg_color, font="Helvetica 12")
        self.ideaLabel.grid(column=1, row=1)

        self.ideaNavigationBar = Frame(self)
        self.ideaNavigationBar.grid(column=1, row=3, pady=6)

        self.title.grid(column=1, row=0)

    def loadProjectIdeas(self, ideas: list[Idea]) -> None:
        self.ideas = ideas
        firstIdea = ideas[0]
        self.selectedIdea = firstIdea

        self.ideaNavigationBar.grid_rowconfigure(0, minsize=30)
        self.drawButtons()

        self.showIdea(firstIdea)

    def drawButtons(self):
        i = 0
        for idea in self.ideas:
            self.ideaNavigationBar.grid_columnconfigure(i, minsize=30)
            RoundedButton(self.ideaNavigationBar, text=str(idea.getNum()), command=lambda a=idea: self.showIdea(a), background=self.frame_bg_color, minwidth=40, fill_color="red" if self.selectedIdea.getNum() is idea.getNum() else "white", hover_color="#bb0000" if self.selectedIdea.getNum() is idea.getNum() else "lightgrey", font="Helvetica 9 bold" if self.selectedIdea.getNum() is idea.getNum() else "Helvetica 8").grid(column=i, row=0, sticky="news")
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
        self.ideaLabel.configure(text=idea.getText())
        self.drawButtons()
        #print(self.selectedIdea.getText() + "   " + str(self.selectedIdea.getNum()))




