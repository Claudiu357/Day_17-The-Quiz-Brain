from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
game_running = True
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question_now = Question(q_text, q_answer)
    question_bank.append(question_now)

quiz = QuizBrain(question_bank)
while game_running:
    quiz.next_question()