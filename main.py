import json
import random

with open("questions.json", "r") as file:
    data = json.load(file)

questions = data["questions"]

name = input("Enter your name: ")

score = 0
chosen_number = []

while True:

 available = [n for n in range(1, len(questions) + 1) if n not in chosen_number]
 if not available:
    break

 number = random.choice(available)
 chosen_number.append(number)

 for q in questions:
    if q["id"] == number:
        question = q
        break
 print("Question:", question["question"])

 answer = input("Your answer: ").lower()

 if answer == question["answer"]:
        print("Correct answer!")
        score += question["mark"]
 else:
        print("Wrong answer. You lost the game.")
        break

 if len(chosen_number) == len(questions):
        print("You answered all questions!")
        break


 print(f"{name}, your final score is {score}/10")