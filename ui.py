from tkinter import *

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.canvas.create_text(150,125,text="Test", font=FONT, fill='black')
        self.canvas.grid(column=0, row=0)

        self.window.mainloop()