class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input_answer = input(f"Q.{self.question_number}:{current_question.text}(True or False)?").lower()
        if input_answer == "true" or input_answer == "false":
            if input_answer == current_question.answer.lower():
                print("Correct")
                self.question_number += 1
            else:
                print("Incorrect")
                self.question_number += 1
        else:
            print("Type again")