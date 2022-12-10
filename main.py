## A simple interactive quiz with python

print("Welcome to the Python Quiz!")

score = 0

question_1 = input("What is the capital of India?\nA. Mumbai\nB. Delhi\nC. Bangalore\n")

if question_1 == "B":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Delhi.")

question_2 = input("What is the currency of India?\nA. Rupee\nB. Dollar\nC. Euro\n")

if question_2 == "A":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is Rupee.")

question_3 = input("In what year did India gain independence?\nA. 1947\nB. 1950\nC. 1952\n")

if question_3 == "A":
    score += 1
    print("Correct!")
else:
    print("Incorrect. The correct answer is 1947.")

print("Your final score is:", score)
