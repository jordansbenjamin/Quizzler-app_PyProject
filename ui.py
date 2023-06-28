from tkinter import *

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=40, bg=THEME_COLOR)
        
        # Canvas
        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.canvas.create_text(150,125,text="Test", font=FONT, fill='black')
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=40)

        # Score label
        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR, font=('Arial', 18, 'normal'))
        self.score_label.grid(column=1, row=0)

        # Green button
        green_img = PhotoImage(file="./images/true.png")
        self.green_btn = Button(image=green_img, highlightthickness=0)
        self.green_btn.grid(column=0, row=2)

        # Red button
        red_img = PhotoImage(file="./images/false.png")
        self.red_btn = Button(image=red_img, highlightthickness=0)
        self.red_btn.grid(column=1, row=2)

        self.window.mainloop()