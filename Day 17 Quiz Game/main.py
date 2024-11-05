from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    acqtual_q = questions['question']
    question_a = questions['correct_answer']
    new_question = Question(acqtual_q, question_a)
    question_bank.append(new_question)    


quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()