
print("welcome to my computer quiz..")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("ok lets play..")

scores = 0

answer1 = input("What does CPU stand for? ")

if answer1.lower() == "central proccesing unit":
    print("correct!")

    scores += 1
else:
    print("Incorrect")

answer2 = input("What does GPU stands for? ")

if answer2.lower() == "graphic proccesing unit":
    print("correct!")
    scores += 1
else:
    print("incorrect")

answer3 = input("What does RAM stand for? ")

if answer3.lower() == "random access memory":
    print("correct!")

    scores += 1
else:
    print("incorrect")

answer4 = input("What does PSU stand for? ")

if answer4.lower() == "power supply":
    print("Correct!")

    scores += 1
else:
    print("incorrect")

print("You answer on " + str(scores) + " right answers")
print("your right answers are " + str((scores/4) * 100) + "%")


