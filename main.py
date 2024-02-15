## A simple interactive Github and GIT quiz with python

print("Welcome GitHub Quiz!")


score = 0

question_1 = input("What is another name for Repository in GitHub?\nA. Mainfile\nB. File\nC. Folder\n").upper()

if question_1 == "C":
    score += 10
    print("Correct!")
else:
    print("Incorrect. The correct answer is Folder.")

question_2 = input("What is GIT ?\nA. It is a CMD app\nB. version control system\nC. A coding storage\n").upper()

if question_2 == "B":
    score += 10
    print("Correct!")
else:
    print("Incorrect. The correct answer is version control system.")

question_3 = input("How can you stage a new file on GIT?\nA. git add [filename]\nB. git commmit -m 'message'\nC. git shiftx\n").upper()

if question_3 == "A":
    score += 10
    print("Correct!")
else:
    print("Incorrect. The correct answer is git add [filename].")

print("Your final score is:", score)

input = input("Press the Enter key to exit")

