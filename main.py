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
def import_quiz():
  global quiz
  print("Please enter the file name of your quiz file (case-sensitive)")
  print("Make sure you have spelled it correctly and that the file is in the same folder as this python script.")
  filename = input()
  with open(f'{filename}.json') as file:
    json_data = file.read()
  quiz = json.loads(json_data)

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
  # User decides outcome for quiz
  clearscrn()
  print("Quiz creation successful!")
  print("What would you like to do?")
  print("1 - Save quiz to file")
  print("2 - Play quiz then save to file")
  print("3 - Play quiz then discard")
  print("4 - Discard quiz")
  
  user_selection = input("Selection (1/2/3/4)")
  if user_selection == "1":
    export_quiz(quiz)
  elif user_selection == "2":
    run_quiz(quiz)
    export_quiz(quiz)
  elif user_selection == "3":
    run_quiz(quiz)
    quiz = {}
    restart()
  elif user_selection == "4":
    quiz = {}
    restart()
  

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
print("1 - Play the default quiz")
print("2 - Create a new quiz")
print("3 - Import and play an existing quiz")

# User selection of choice
user_selection = input("Your selection (1/2/3): ").lower()
# Selection
if user_selection == "1":
  quiz = {'What is the capital of Japan?': {'IndexNum': 1, 'choices': {'A': 'BEIJING', 'B': 'SEOUL', 'C': 'TOKYO', 'D': 'HANOI'}, 'answer': 'TOKYO'}, 'Which of the following is the smallest planet in our solar system?': {'IndexNum': 2, 'choices': {'A': 'EATH', 'B': 'MARS', 'C': 'MERCURY', 'D': 'VENUS'}, 'answer': 'MERCURY'}, 'Which of the following is not a type of rock?': {'IndexNum': 3, 'choices': {'A': 'IGNEOUS', 'B': 'METAMORPHIC', 'C': 'SEDIMENTARY', 'D': 'ORGANIC'}, 'answer': 'ORGANIC'}, 'Who is the author of the Harry Potter series?': {'IndexNum': 4, 'choices': {'A': 'STEPHEN KING', 'B': 'JK ROWLING', 'C': 'SUZANNE COLLINS', 'D': 'GEORGE RR MARTIN'}, 'answer': 'JK ROWLING'}, 'What is the tallest mountain in the world?': {'IndexNum': 5, 'choices': {'A': 'MOUNT EVEREST', 'B': 'K2', 'C': 'MOUNT KILLIMANJARO', 'D': 'MOUNT DENALI'}, 'answer': 'MOUNT EVEREST'}, 'Which of the following is a programming language?': {'IndexNum': 6, 'choices': {'A': 'HTML', 'B': 'XML', 'C': 'JAVA', 'D': 'SQL'}, 'answer': 'JAVA'}, 'Who invented the telephone?': {'IndexNum': 7, 'choices': {'A': 'ALEXANDER GRAHAM BELL', 'B': 'THOMAS EDISON', 'C': 'ALBERT EINSTEIN', 'D': 'ISAAC NEWTON'}, 'answer': ''}, 'What is the largest country by land area?': {'IndexNum': 8, 'choices': {'A': 'UNITED STATES', 'B': 'RUSSIA', 'C': 'CHINA', 'D': 'CANADA'}, 'answer': 'RUSSIA'}, 'Which of the following is not a type of cloud?': {'IndexNum': 9, 'choices': {'A': 'STRATUS', 'B': 'CIRRUS', 'C': 'NIMBUS', 'D': 'HAZE'}, 'answer': 'HAZE'}, 'Who was the first man to walk on the moon?': {'IndexNum': 10, 'choices': {'A': 'NEIL ARMSTRONG', 'B': 'BUZZ ALDRIN', 'C': 'YURI GAGARIN', 'D': 'JOHN GLENN'}, 'answer': 'NEIL ARMSTRONG'}, 'What is the chemical symbol for gold?': {'IndexNum': 11, 'choices': {'A': 'AU', 'B': 'AG', 'C': 'CU', 'D': 'PT'}, 'answer': 'AU'}, 'Which of the following is not a type of dance?': {'IndexNum': 12, 'choices': {'A': 'SALSA', 'B': 'WALTZ', 'C': 'TANGO', 'D': 'RUMBA'}, 'answer': 'RUMBA'}, 'Which of the following is a type of pasta?': {'IndexNum': 13, 'choices': {'A': 'LASAGNA', 'B': 'BURRITO', 'C': 'SUSHI', 'D': 'FALAFEL'}, 'answer': 'LASAGNA'}, 'What is the currency of India?': {'IndexNum': 14, 'choices': {'A': 'RUPEE', 'B': 'YEN', 'C': 'EURO', 'D': 'POUND'}, 'answer': 'RUPEE'}, 'Which of the following is a type of whale?': {'IndexNum': 15, 'choices': {'A': 'DOLPHIN', 'B': 'NARWHAL', 'C': 'ORCA', 'D': 'WALRUS'}, 'answer': 'NARWHAL'}, 'Which of the following is not a type of fish?': {'IndexNum': 16, 'choices': {'A': 'TUNA', 'B': 'SALMON', 'C': 'DOLPHIN', 'D': 'COD'}, 'answer': 'DOLPHIN'}, 'Which of the following is not a type of dinosaur?': {'IndexNum': 17, 'choices': {'A': 'T-REX', 'B': 'STEGOSAURUS', 'C': 'PTERODACTYL', 'D': 'SABERTOOTH'}, 'answer': 'SABERTOOTH'}, 'Which of the following is a type of fruit?': {'IndexNum': 18, 'choices': {'A': 'CUCUMBER', 'B': 'EGGPLANT', 'C': 'TOMATO', 'D': 'STRAWBERRY'}, 'answer': 'STRAWBERRY'}, 'Which of the following is not a type of tree?': {'IndexNum': 19, 'choices': {'A': 'OAK', 'B': 'PINE', 'C': 'MAPLE', 'D': 'CORAL'}, 'answer': 'CORAL'}, "Who directed the movie 'Jaws'?": {'IndexNum': 20, 'choices': {'A': 'STEVEN SPIELBURG', 'B': 'MARTIN SCORSESE', 'C': 'QUENTIN TARANTINO', 'D': 'FRANCIS FORD COPPOLA'}, 'answer': 'STEVEN SPIELBURG'}}
  run_quiz(quiz)
elif user_selection == "2":
  create_quiz()
  export_quiz(quiz)
elif user_selection == "3":
  import_quiz()
  run_quiz(quiz)
  restart()
else:
  print("Error")