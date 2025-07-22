import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.false_image = tk.PhotoImage(file="./images/false.png")
        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.window.title("Quizzler")

        self.__question_box()
        self.btn_false = self.__btn(self.false_image, 3, 0, self.answer_false)
        self.btn_true = self.__btn(self.true_image, 3, 1, self.answer_true)
        
        self.score_label = tk.Label(
            self.window, text="Score: 0", bg=THEME_COLOR, fg="white"
        )
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def __btn(self, image, row, column, command):
        btn = tk.Button(self.window, image=image, highlightthickness=0, command=command)
        btn.grid(row=row, column=column)
        return btn

    def __question_box(self):
        self.question_box = tk.Canvas(
            self.window, width=300, height=250, bg="white", highlightthickness=0
        )
        self.question_text = self.question_box.create_text(
            150,
            125,
            text="Lorem ipsum dolor sit amet.",
            font=("Arial", 20, "italic"),
            width=280,
        )
        self.question_box.grid(row=1, column=0, columnspan=2, pady=50)

    def get_next_question(self):
        self.question_box.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)
        else:
            self.question_box.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")

        self.window.after(1000, self.get_next_question)
