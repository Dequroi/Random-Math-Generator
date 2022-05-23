import random


# add score system based on difficulty of questions
# Users/Farjan/PycharmProjects/Replit_Projects/main.py


def check(user_answer):
    global streak
    streak = []
    if user_answer == response:
        print("Correct")
    else:
        print("Incorrect")
        print(f"The correct answer is {user_answer}")
    choice1 = input("Continue? Y or N \n").lower()
    if choice1 == "y":
        streak.append("correct")
        return True
    elif choice1 == "n":
        streak.clear()
        return False
    else:
        print("Invalid input")
        streak.clear()
        return False


# noinspection PyGlobalUndefined
def difficulty(selection_1):
    # noinspection PyGlobalUndefined
    global first_integer
    # noinspection PyGlobalUndefined
    global second_integer
    chosen_difficulty = input("Difficulty? Easy = 0, Medium = 1, Hard = 2, Expert = 3 \n")
    selection1 = selection_1
    if selection1 == "divide":
      local_continuing = True
      while local_continuing:  # means true
          first_integer = random.randint(1, 100)
          second_integer = random.randint(2, 100)
          if first_integer == second_integer:
            first_integer = random.randint(1, 100)
            second_integer = random.randint(2, 100)
          if first_integer % second_integer == 0:
            return
          else:
            first_integer = random.randint(1, 100)
            second_integer = random.randint(2, 100)
    elif selection1 == "multiply":
        if chosen_difficulty == "0":
            first_integer = random.randint(1, 5)
            second_integer = random.randint(0, 5)
        if chosen_difficulty == "1":
            first_integer = random.randint(2, 10)
            second_integer = random.randint(1, 5)
        if chosen_difficulty == "2":
            first_integer = random.randint(2, 10)
            second_integer = random.randint(2, 10)
        if chosen_difficulty == "3":
            first_integer = random.randint(10, 20)
            second_integer = random.randint(2, 10)
    else:
        if chosen_difficulty == "0":
            first_integer = random.randint(0, 10)
            second_integer = random.randint(0, 10)
        if chosen_difficulty == "1":
            first_integer = random.randint(10, 100)
            second_integer = random.randint(0, 10)
        if chosen_difficulty == "2":
            first_integer = random.randint(10, 1000)
            second_integer = random.randint(10, 100)
        if chosen_difficulty == "3":
            first_integer = random.randint(100, 1000)
            second_integer = random.randint(10, 1000)


true_streak = 0


def streak_point_check():
    global true_streak
    for _ in streak:
        true_streak += 1
    print(f"Your streak is {true_streak}")
    return


print("""
  __  __       _   _        _____                           _             
 |  \/  |     | | | |      / ____|                         | |            
 | \  / | __ _| |_| |__   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |\/| |/ _` | __| '_ \  | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | | (_| | |_| | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|  |_|\__,_|\__|_| |_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   

""")


print("Welcome to the Random Math Problem Generator")
print("This generator will generate random addition, subtraction, multiplication, and division problems")
selection = input("Type add, subtract, multiply, and divide \n").lower()
global_continuing = True
if selection == "add":
    while global_continuing:
        difficulty("add")
        print(f"{first_integer} + {second_integer} = ???")
        response = int(input())
        answer = first_integer + second_integer
        global_continuing = check(answer)
        streak_point_check()
if selection == "subtract":
    while global_continuing:
        difficulty("subtract")
        print(f"{first_integer} - {second_integer} = ???")
        response = int(input())
        answer = first_integer - second_integer
        global_continuing = check(answer)
        streak_point_check()
if selection == "multiply":
    while global_continuing:
        difficulty("multiply")
        print(f"{first_integer} * {second_integer} = ???")
        response = int(input())
        answer = first_integer * second_integer
        global_continuing = check(answer)
        streak_point_check()
if selection == "divide":
    while global_continuing:
        difficulty("divide")
        print(f"{first_integer} / {second_integer} = ???")
        response = int(input())
        answer = first_integer / second_integer
        global_continuing = check(answer)
        streak_point_check()
