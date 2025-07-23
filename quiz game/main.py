from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for entry in question_data:
    q_text = entry["text"]
    q_answer = entry["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is:{quiz.score}/{len(question_bank)}")
