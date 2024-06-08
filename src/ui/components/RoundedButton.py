import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, master=None, text="", minwidth = 100, fill_color="white", hover_color="lightgrey", font="Helvetica 8 bold", command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.text = text
        self.fill_color = fill_color
        self.min_width = minwidth
        self.hover_color = hover_color
        self.corner_radius = kwargs.get("corner_radius", 20)
        
        # Utilisation de tk.Label pour obtenir la largeur du texte
        temp_label = tk.Label(master, text=self.text, font=font)

        self.text_width = temp_label.winfo_reqwidth()
        temp_label.destroy()


        self.width = self.text_width + 20 if self.text_width + 20 > self.min_width else self.min_width # Ajout de padding horizontal
        self.height = kwargs.get("height", 40)
        
        self.configure(width=self.width, height=self.height, bg=self['bg'], highlightthickness=0)
        
        self.button = self.create_rounded_rectangle(5, 5, self.width-5, self.height-5, self.corner_radius, outline="black", fill=fill_color, width=2)
        self.text_id = self.create_text(self.width/2, self.height/2, text=self.text, fill="black", font=font)

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1,
            x1 + radius, y1,
            x2 - radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1 + radius,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def on_click(self, event):
        if self.command:
            self.command()

    def setHoverColor(self, color: str):
        self.hover_color = color

    def on_enter(self, event):
        self.itemconfig(self.button, fill=self.hover_color)

    def on_leave(self, event):
        self.itemconfig(self.button, fill=self.fill_color)