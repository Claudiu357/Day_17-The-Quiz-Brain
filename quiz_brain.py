class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input_answer = input(f"Q.{self.question_number}:{current_question.text}(True or False)?").lower()
        self.check_answer(input_answer, current_question.answer)

    def still_have_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer, correct_answer):
        if answer == "true" or answer == "false":
            if answer == correct_answer.lower():
                self.question_number += 1
                self.score += 1
                print("Correct")
                print(f"Your current score is {self.score}/{self.question_number}")
            else:
                self.question_number += 1
                print("Incorrect")
                print(f"The correct answer was: {correct_answer}")
                print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("Type again")