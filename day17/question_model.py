#defines question class 
#when initialized each object must be given some text (the question) andan answer
class Question:
    def __init__(self, q_text, q_answer):
        self.text=q_text
        self.answer=q_answer