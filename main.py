'''
  Name: Cameron Labes
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# packages

# functions

def create_quiz():
  # Makes quiz variable global
  global quiz
  # Creates quiz dictionary
  quiz = {}
  # Asks user for amount of questions
  question_amount = int(input("How many questions do you want in your quiz? "))
  # Loops for the amount of questions a user wants
  for i in range(question_amount):
    # Asks user for question
    question = input(f"Enter question {i+1}: ")
    # Asks user for choices for question
    choices = input(f"Enter the answer choices for question {i+1}, separated by commas: ").split(",")
    lettered_choices = {}
    # Gives an index letter (A - Z) for each choice
    for index, choice in enumerate(choices):
      lettered_choices[chr(ord('A') + index)] = choice.strip()
    # Asks user for correct answer to question
    answer = input(f"What is the correct answer for question {i+1}? ").strip().upper()
    # Organizes inputs into main quiz dictionary
    quiz[question] = {"IndexNum": i+1, "choices": lettered_choices, "answer": answer}

# main routine
# Print options
print("#*#*#*# Quiz Creator #*#*#*#")
print("OPTIONS")
print("A - Play the default quiz")
print("B - Create a new quiz")
print("C - Import an existing quiz")
# User selection of choice
user_selection = input("Your selection (A/B/C): ").lower()
# Selection
if user_selection == "a":
  print("Success")
elif user_selection == "b":
  create_quiz()
  print(quiz)
elif user_selection == "c":
  print("Success")
else:
  print("Error")