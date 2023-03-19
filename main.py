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
  print("File saved as quiz.json")

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
    choices = input(f"Enter the answer choices for question {i+1}, separated by commas: ").split(",")
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
    # Copies the choices dictionary for use in checking answers in all caps
    upper_choices = {key: value.upper() if isinstance(value, str) else value for key, value in choices.items()}
    # Seperates keys of the choices dictionary into a list
    letter_indexs_list = [key for key in choices]
    # Creates a usable output for the choices keys
    letter_index_output = '/'.join(letter_indexs_list)
    # Seperates answer into it's own dictionary
    long_answer = question_data_list[question_list.index(question)]['answer']
    for index, value in upper_choices.items():
      if value == long_answer:
          matching_index = index
          break
    answer = {matching_index:long_answer}
    # Prints the question number and question itself
    print(f"\nQuestion {question_num}:")
    print(question)
    # Prints all avaliable options and their index letters
    for letter_index, full_answer in choices.items():
      print(letter_index, full_answer)
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
  quiz = {
    "What is the capital of Japan?": {
        "IndexNum": 1,
        "choices": {
            "A": "Beijing",
            "B": "Seoul",
            "C": "Tokyo",
            "D": "Hanoi"
        },
        "answer": "TOKYO"
    },
    "Which of the following is the smallest planet in our solar system?": {
        "IndexNum": 2,
        "choices": {
            "A": "Earth",
            "B": "Mars",
            "C": "Mercury",
            "D": "Venus"
        },
        "answer": "MERCURY"
    },
    "Which of the following is not a type of rock?": {
        "IndexNum": 3,
        "choices": {
            "A": "Igneous",
            "B": "Metamorphic",
            "C": "Sedimentary",
            "D": "Organic"
        },
        "answer": "ORGANIC"
    },
    "Who is the author of the Harry Potter series?": {
        "IndexNum": 4,
        "choices": {
            "A": "Stephen King",
            "B": "JK Rowling",
            "C": "Suzanne Collins",
            "D": "George RR Martin"
        },
        "answer": "JK ROWLING"
    },
    "What is the tallest mountain in the world?": {
        "IndexNum": 5,
        "choices": {
            "A": "Mount Everest",
            "B": "K2",
            "C": "Mount Kilimanjaro",
            "D": "Mount Denali"
        },
        "answer": "MOUNT EVEREST"
    },
    "Which of the following is a programming language?": {
        "IndexNum": 6,
        "choices": {
            "A": "HTML",
            "B": "XML",
            "C": "Java",
            "D": "SQL"
        },
        "answer": "JAVA"
    },
    "Who invented the telephone?": {
        "IndexNum": 7,
        "choices": {
            "A": "Alexander Graham Bell",
            "B": "Thomas Edison",
            "C": "Albert Einstein",
            "D": "Isaac Newton"
        },
        "answer": "ALEXANDER GRAHAM BELL"
    },
    "What is the largest country by land area?": {
        "IndexNum": 8,
        "choices": {
            "A": "United States",
            "B": "Russia",
            "C": "China",
            "D": "Canada"
        },
        "answer": "RUSSIA"
    },
    "Which of the following is not a type of cloud?": {
        "IndexNum": 9,
        "choices": {
            "A": "Stratus",
            "B": "Cirrus",
            "C": "Nimbus",
            "D": "Haze"
        },
        "answer": "HAZE"
    },
    "Who was the first man to walk on the moon?": {
        "IndexNum": 10,
        "choices": {
            "A": "Neil Armstrong",
            "B": "Buzz Aldrin",
            "C": "Yuri Gagarin",
            "D": "John Glenn"
        },
        "answer": "NEIL ARMSTRONG"
    },
    "What is the chemical symbol for gold?": {
        "IndexNum": 11,
        "choices": {
            "A": "Au",
            "B": "Ag",
            "C": "Cu",
            "D": "Pt"
        },
        "answer": "AU"
    },
    "Which of the following is not a type of dance?": {
        "IndexNum": 12,
        "choices": {
            "A": "Salsa",
            "B": "Waltz",
            "C": "Tango",
            "D": "Rumba"
        },
        "answer": "RUMBA"
    },
    "Which of the following is a type of pasta?": {
        "IndexNum": 13,
        "choices": {
            "A": "Lasagna",
            "B": "Burrito",
            "C": "Sushi",
            "D": "Falafel"
        },
        "answer": "LASAGNA"
    },
    "What is the currency of India?": {
        "IndexNum": 14,
        "choices": {
            "A": "Rupee",
            "B": "Yen",
            "C": "Euro",
            "D": "Pound"
        },
        "answer": "RUPEE"
    },
    "Which of the following is a type of whale?": {
        "IndexNum": 15,
        "choices": {
            "A": "Dolphin",
            "B": "Narwhal",
            "C": "Orca",
            "D": "Walrus"
        },
        "answer": "NARWHAL"
    },
    "Which of the following is not a type of fish?": {
        "IndexNum": 16,
        "choices": {
            "A": "Tuna",
            "B": "Salmon",
            "C": "Dolphin",
            "D": "Cod"
        },
        "answer": "DOLPHIN"
    },
    "Which of the following is not a type of dinosaur?": {
        "IndexNum": 17,
        "choices": {
            "A": "T-Rex",
            "B": "Stegosaurus",
            "C": "Pterodactyl",
            "D": "Sabertooth"
        },
        "answer": "SABERTOOTH"
    },
    "Which of the following is a type of fruit?": {
        "IndexNum": 18,
        "choices": {
            "A": "Cucumber",
            "B": "Eggplant",
            "C": "Tomato",
            "D": "Strawberry"
        },
        "answer": "STRAWBERRY"
    },
    "Which of the following is not a type of tree?": {
        "IndexNum": 19,
        "choices": {
            "A": "Oak",
            "B": "Pine",
            "C": "Maple",
            "D": "Coral"
        },
        "answer": "CORAL"
    },
    "Who directed the movie 'Jaws'?": {
        "IndexNum": 20,
        "choices": {
            "A": "Steven Spielberg",
            "B": "Martin Scorsese",
            "C": "Quentin Tarantino",
            "D": "Francis Ford Coppola"
        },
        "answer": "STEVEN SPIELBURG"
    }
}
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