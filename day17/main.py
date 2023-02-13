from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#defines quiz_bank as an empty list
#will be used to store objects from the Question class
question_bank=[]

#for each member of the question_data list
for question in question_data:
    #stores the corresponding text as question_text
    question_text=question["text"]
    #stores the corresponding answer as question_answer
    question_answer=question["answer"]
    #creates an object of the Question class and stores it as new_question
    new_question=Question(q_text=question_text,q_answer=question_answer)
    #appends the new_question object to the question_bank list
    question_bank.append(new_question)

#creates an object of the QuizBrain class which takes the question_bank list, containing objects of the Question class
quiz=QuizBrain(question_bank)

#checks if there are still questions left. If so, passes the next question to the user
while quiz.still_has_questions():
    quiz.next_question()

#prints congratulatory message at the end of quiz
print("You completed the quiz")
#prints final score at the end of quiz
print(f"Your final score was: {quiz.score}/{quiz.question_number}")