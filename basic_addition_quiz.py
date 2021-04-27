import random


mode = input("Choose difficulty mode (1,2,3): ")
print("Let us begin")

# Difficulty selection


if mode == "1":
    print("You have picked easy mode")
    x, y = 0, 10 
elif mode == "2": 
    print("You have picked medium mode")
    x, y = 0, 100 
elif mode == "3":
    print("You have picked hard mode")
    x, y = 0, 1000 
else:
    print("Invalid option")


# quiz

Answer = ""
loop_counter = 0
correct_counter = 0
while Answer != "stop":
    loop_counter += 1

    a = random.randint(x, y)
    b = random.randint(x, y)

    answer = input(str(a) + " + " + str(b) + ' = ')
    
    if answer == "stop":
        print("final score = " + str(correct_counter) + '/' + str(loop_counter))
        Answer += "stop"
        print(Answer)
    elif int(answer) != (a + b):
        print("incorrect")
    elif int(answer) == (a + b):
        print("correct")
        correct_counter += 1
        
