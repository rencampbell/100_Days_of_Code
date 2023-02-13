# this class serves as the brain of our game
class QuizBrain:

    #initializes class
    #question number and score are set to 0 and a list of questions must be passed as an attribute
    def __init__(self, q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    #checks if there are more questions in the list returns true or false
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    #shows a question to the userand checks their answer
    def next_question(self):
        current_question=self.question_list[self.question_number]
        correct_answer=current_question.answer
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,correct_answer)

    #checks if user's answer is correct by comparing it to the correct answer
    #prints an appropriate message as well as the current score
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("Tou got it right!")
            self.score+=1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
