## A simple interactive Github and GIT quiz with python

print("Welcome GitHub Quiz!")

score = 0

question_1 = input("What is another name for Repository in GitHub?\nA. Mainfile\nB. File\nC. Folder\n")

if question_1 == "C" or "b":
    score += 10
    print("Correct!")
else:
    print("Incorrect. The correct answer is Folder.")

question_2 = input("What is GIT ?\nA. It is a CMD app\nB. version control system\nC. A coding storage\n")

if question_2 == "A":
    score += 10
    print("Correct!")
else:
    print("Incorrect. The correct answer is version control system.")

question_3 = input("In what year did India gain independence?\nA. 1947\nB. 1950\nC. 1952\n")

if question_3 == "A":
    score += 10
    print("Correct!")
else:
    print("Incorrect. The correct answer is 1947.")

print("Your final score is:", score)

input = input("Press the Enter key to exit")