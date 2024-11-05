class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

        
    # def next_question(self):
    #     #current question number
    #     question = self.question_list[self.question_number]
    #     self.question_number += 1
    #     print(question.text)
    #     input("True or False:")
            
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You have answered all the questions")
            print(f"Your final score was {self.score}/{self.question_number} -> {self.score / self.question_number}%")
            return False
        #could be written as **return** self < len(self) as "<" is a true/false operator to start with
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct answer, your score is {self.score}/{self.question_number}")
            
        else:
            print("Incorrect answer")
        print(f"The correct answer was {correct_answer}, your score is {self.score}/{self.question_number}")
        