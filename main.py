'''
  Name: Cameron Labes
  James Hargest College
  Programming Internal for 1.7 ~ 4 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''
# packages
import json
import os, sys, time
# functions

def clearscrn():
  os.system('cls' if os.name == 'nt' else 'clear')

def restart():
  python = sys.executable
  os.execl(python, python, *sys.argv)
def export_quiz(quiz):
  jsonstr = json.dumps(quiz)
  file = open("quiz.json", "w")
  file.write(jsonstr)
  file.close()
  print("Export Successful!")

def create_quiz():
  # Clear the console
  clearscrn()
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
    choices = input(f"Enter the answer choices for question {i+1}, separated by commas: ").upper().split(",")
    lettered_choices = {}
    # Gives an index letter (A - Z) for each choice
    for index, choice in enumerate(choices):
      lettered_choices[chr(ord('A') + index)] = choice.strip()
    # Asks user for correct answer to question
    answer = input(f"What is the correct answer for question {i+1}? ").strip().upper()
    # Organizes inputs into main quiz dictionary
    quiz[question] = {"IndexNum": i+1, "choices": lettered_choices, "answer": answer}

def run_quiz(quiz):
  # Clear the console
  clearscrn()
  # Initialize score variable
  score = 0
  # Sorts the questions into seperate list
  question_list = list(quiz.keys())
  # Sorts other data into seperate list
  question_data_list = list(quiz.values())
  # Repeats for every question
  for question in question_list:
    # Setup of variables for use later
    # Seperates the Index Numbver of a question into a variable
    question_num = question_data_list[question_list.index(question)]['IndexNum']
    # Seperates choices dictionary into a variable
    choices = question_data_list[question_list.index(question)]['choices']
    # Seperates keys of the choices dictionary into a list
    letter_indexs_list = [key for key in choices]
    # Creates a usable output for the choices keys
    letter_index_output = '/'.join(letter_indexs_list)
    # Seperates answer into it's own dictionary
    long_answer = question_data_list[question_list.index(question)]['answer']
    for index, value in choices.items():
      if value == long_answer:
          matching_index = index
          break
    answer = {matching_index:long_answer}
    # Prints the question number and question itself
    print(f"\nQuestion {question_num}:")
    print(question)
    # Prints all avaliable options and their index letters
    for letter_index, full_answer in choices.items():
      print(letter_index, full_answer.capitalize())
    # user input
    user_answer = input(f"Select your answer ({letter_index_output}): ").upper()
    # Checks user input against answer dictionary
    if user_answer in answer:
      print("Correct!")
      score += 1
    elif user_answer in answer.values():
      print("Correct!")
      score += 1
    elif user_answer not in answer:
      if user_answer in choices:
        print("Incorrect!")
      else:
        print("Error!")
    elif user_answer not in answer.values():
      if user_answer in choices.values():
        print("Incorrect!")
      else:
        print("Error!")   
  # Give user their score
  clearscrn()
  print(f"You scored {score} out of {len(quiz)} questions!")
  time.sleep(5)
  restart()
  





# main routine
# Print options
print("#*#*#*# Quiz Creator #*#*#*#")
print("OPTIONS")
print("A - Play the default quiz")
print("B - Create a new quiz")
print("C - Import and play an existing quiz")




# User selection of choice
user_selection = input("Your selection (A/B/C): ").lower()
# Selection
if user_selection == "a":
  quiz = {'What is the capital of New Zealand?': {'IndexNum': 1, 'choices': {'A': 'AUCKLAND', 'B': 'WELLINGTON', 'C': 'DUNEDIN'}, 'answer': 'WELLINGTON'}, 'What is the captial of France?': {'IndexNum': 2, 'choices': {'A': 'LONDON', 'B': 'BERLIN', 'C': 'PARIS'}, 'answer': 'PARIS'}, 'What is the capital of Japan?': {'IndexNum': 3, 'choices': {'A': 'BANGKOK', 'B': 'TOKYO', 'C': 'MOSCOW'}, 'answer': 'TOKYO'}}
  run_quiz(quiz)
elif user_selection == "b":
  create_quiz()
  export_quiz(quiz)
elif user_selection == "c":
  print("Success")
else:
  print("Error")