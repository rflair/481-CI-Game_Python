# Programming Quiz
# Robert Flair and Richard 

name = input("Hello! Please enter in your name\n")
print("\nYou are now ready to take the quiz,", name, "Good luck!\n")

# Question 1
q1answer = ""
q1attempts = 0
q1 = "false"
while q1answer.lower() != "d" and q1attempts < 2:
    print("QUESTION 1: Which of the following most accurately describes a computer program?")
    print("\na. A collection of objects, all of them the same type")
    print("\nb. A collection of objects of different types")
    print("\nc. A list of instructions for objects to perform certain actions")
    print("\nd. A set of instructions telling the computer how to perform tasks")
    q1answer = input("\n\nType in the letter of the correct answer\n")
    if q1answer.lower() != "d":
        q1attempts = q1attempts + 1
        print("Your answer is not correct\n\n")
    else:
        q1attempts = q1attempts + 1
        q1 = "true"
        print("Correct!\n\n")

# Question 2
q2answer = ""
q2attempts = 0
q2 = "false"
while q2answer.lower() != "b" and q2attempts < 2:
    print("QUESTION 2: What is an algorithm")
    print("\na. A collection of objects, all of the same type")
    print("\nb. A sequence of steps that are going to help you complete a task")
    print("\nc. A list of instructions to perform certain actions")
    print("\nd. All of the above")
    q2answer = input("\nType in the letter of the correct answer\n")
    if q2answer.lower() != "b":
        q2attempts = q2attempts + 1
        print("Your answer is not correct\n\n")
    else:
        q2attempts = q2attempts + 1
        q2 = "true"
        print("Correct!\n\n")

# Question 3
q3answer = ""
q3attempts = 0
q3 = "false"

while q3answer.lower() != "d" and q3attempts < 2:
    print("QUESTION 3: What are variables?")
    print("\na. Variables are used to store data in a program")
    print("\nb. Variables are used to represent the data")
    print("\nc. Each variable has a unique name")
    print("\nd. All of the above")
    q3answer = input("\nType in the letter of the correct answer\n")
    if q3answer.lower() != "d":
        q3attempts = q3attempts + 1
        print("Your answer is not correct\n\n")
    else:
        q3attempts = q3attempts + 1
        q3 = "true"
        print("Correct!\n\n")

# Question 4
q4answer = ""
q4attempts = 0
q4 = "false"

while q4answer.lower() != "b" and q4attempts < 2:
    print("QUESTION 4: How did we use variables in our app?")
    print("\na. We used variables to make the block editor bigger")
    print("\nb. We used variables to store 'count'")
    print("\nc. We used variables to eliminate loops")
    print("\nd. We used variables to solve a problem")
    q4answer = input("\nType in the letter of the correct answer\n")
    if q4answer.lower() != "b":
        q4attempts = q4attempts + 1
        print("Your answer is not correct\n\n")
    else:
        q4attempts = q4attempts + 1
        q4 = "true"
        print("Correct!\n\n")

# Calculate final score
final_score = 0
scores = (q1, q2, q3, q4)
for i in scores:
    if i == "true":
        final_score += 1

# Progress Report
q1score = 0
q2score = 0
q3score = 0
q4score = 0
print("You scored a ", final_score, "out of 4.")
print("Question 1")
print("Number of attempts: ", q1attempts)
if q1 == "true":
    q1score = 1
    print("Score = 1\n")
else:
    print("Score = 0\n")

print("Question 2")
print("Number of attempts: ", q2attempts)
if q2 == "true":
    q2score = 1
    print("Score = 1\n")
else:
    print("Score = 0\n")

print("Question 3")
print("Number of attempts: ", q3attempts)
if q3 == "true":
    q3score = 1
    print("Score = 1\n")
else:
    print("Score = 0\n")

print("Question 4")
print("Number of attempts: ", q4attempts)
if q4 == "true":
    q4score = 1
    print("Score = 1\n")
else:
    print("Score = 0\n")

# Prints a report to a file called "report.txt"
file = open("report.txt", "w")
line1 = name + " scored a " + str(final_score) + " out of 4\n"
file.write(line1)
line2 = "Question 1 took " + str(q1attempts) + " attempt(s) with a score of " + str(q1score) + "\n"
file.write(line2)
line3 = "Question 2 took " + str(q2attempts) + " attempt(s) with a score of "+ str(q2score) + "\n"
file.write(line3)
line4 = "Question 3 took " + str(q3attempts) + " attempt(s) with a score of " + str(q3score) + "\n"
file.write(line4)
line5 = "Question 4 took " + str(q4attempts) + " attempt(s) with a score of " + str(q4score) + "\n"
file.write(line5)
file.close()


input("\n\nPress the enter key to exit.")
