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
import shutil
import re

# functions
def clear_screen():
    # Clear console screen
    os.system('cls' if os.name == 'nt' else 'clear')


def restart_program():
    # restart_program the program
    python = sys.executable
    os.execl(python, python, *sys.argv)


def user_input(prompt):
    # User input with confirmation
    while True:
        user_answer = input(prompt)
        confirm = input(f"   You entered '{user_answer}'. Is this correct? (y/n): ")
        while confirm.lower() not in ["y", "n"]:
            print("   Invalid input. Please enter 'y' or 'n'.")
            confirm = input("   Is this correct? (y/n): ")
        if confirm.lower() == "y":
            break
    return user_answer


def import_quiz():
    # Import quiz from existing JSON file
    global quiz

    # Title
    clear_screen()
    print("   #*#*#*# Importing #*#*#*#")
    while True:

        # User instructions
        print("   Please enter the file name of your quiz file")
        print("   Make sure the file is in the same folder as this python script.")
        filename = input().lower()
        try:

            # Try to open filename provided
            with open(f'{filename}.json') as file:
                json_data = file.read()
            quiz = json.loads(json_data)
            break
        except (NameError, FileNotFoundError):
            print(
                "   The quiz file was not found. Please try again and make sure you spelled the file name correctly and the file is in the right folder."
            )


def export_quiz(quiz):
    # Export quiz to JSON file
    # Title
    clear_screen()
    print("   #*#*#*# Exporting #*#*#*#")

    while True:
        # JSON file
        print("   Exporting...")
        time.sleep(1)
        try:
            jsonstr = json.dumps(quiz)
            file = open("quiz.json", "w")
            file.write(jsonstr)
            file.close()
            print("   Export Successful!")
            print("   File saved as quiz.json")
            time.sleep(2)
            break
        except:
            print("   Export was not successful, retrying")


def print_high_scores(quiz):
    # Prints high scores of a quiz
    high_scores = quiz['scores']
    sorted_scores = dict(
        sorted(high_scores.items(), key=lambda item: item[1], reverse=True))
    if sorted_scores:
        for username, score in sorted_scores.items():
            print(f"   {username} - {score}")
    else:
        print("   There are no high scores to display.")
    input("   Press enter to continue: ")

def create_quiz():
    # Creates quiz from user input
    # Title function
    def quiz_creator_title(num, total):
        clear_screen()
        if num is not None:
            print("   #*#*#*# Quiz Creator #*#*#*#")
            print(f"   Question {num + 1} out of {total}")
        else:
            print("   #*#*#*# Quiz Creator #*#*#*#")

    quiz_creator_title(None, None)

    # Initialize quiz variable
    global quiz
    quiz = {}

    # Quiz name input
    quiz_name = user_input("   Please enter a name for this quiz: ")

    # Number of questions input
    while True:
        try:
            question_amount = int(input("   How many questions do you want in your quiz? "))
            break
        except ValueError:
            print("   Please enter an appropriate value, (e.g. 1, 10, 17)")

    # Loops for the amount of questions a user wants
    for i in range(question_amount):
        # Title
        quiz_creator_title(i, question_amount)

        # Asks user for question
        question = user_input(f"   Enter question {i + 1}: ")

        # Asks user for choices for question
        while True:
            choices = re.sub(r',\s+', ',', user_input(
                f"   Enter the answer choices for question {i + 1}, separated by commas: ")).split(",")
            if len(choices) > 26:
                print(
                    "   You have entered more than 26 choices which means each choice cannot be assigned its own letter. Please consider lowering the amount of choices in this particular question and try again.")
            else:
                break
        lettered_choices = {}

        # Gives an index letter (A - Z) for each choice
        for index, choice in enumerate(choices):
            lettered_choices[chr(ord('A') + index)] = choice.strip()

        while True:
            # Asks user for correct answer to question
            answer = user_input(f"   What is the correct answer for question {i + 1}? ").strip().upper()

            # Copies lettered choices dictionary and makes copy uppercase for answer checking
            lettered_choices_upper = lettered_choices.copy()
            for key in lettered_choices:
                lettered_choices_upper[key] = lettered_choices[key].upper()

            # Check if the answer key is in the lettered_choices_upper dictionary
            if answer in lettered_choices_upper.values():
                # Get the index letter corresponding to the answer value
                correct_choice = [key for key, value in lettered_choices_upper.items() if value == answer][0]

                # Organizes inputs into main quiz dictionary
                quiz[question] = {
                    "IndexNum": i + 1,
                    "choices": lettered_choices,
                    "answer": correct_choice
                }
                quiz['scores'] = {}
                quiz['name'] = quiz_name
                break
            else:
                print("   The answer key is not one of the answer choices given. Please try again.")

    # User decides outcome for quiz
    quiz_creator_title(None, None)
    print("Quiz creation successful!")
    print("What would you like to do?")
    print("1 - Save quiz to file")
    print("2 - Play quiz then save to file")
    print("3 - Play quiz then discard")
    print("4 - Discard quiz")
    
    while True:
        user_selection = input("   Selection (1/2/3/4): ")
        if user_selection == "1":
            export_quiz(quiz)
            break
        elif user_selection == "2":
            run_quiz(quiz)
            export_quiz(quiz)
            break
        elif user_selection == "3":
            run_quiz(quiz)
            quiz = {}
            print("   Quiz has been removed from memory")
            time.sleep(2)
            break
        elif user_selection == "4":
            quiz = {}
            print("   Quiz has been removed from memory")
            time.sleep(2)
            break
        else:
            print("   No valid selection was chosen. Please try again.")
    restart_program()


def run_quiz(quiz):
    """Runs existing quiz"""
    # Title function
    def quiz_player_title(quiz_name):
        clear_screen()
        if quiz_name is None:
            print("   #*#*#*# Quiz Player #*#*#*#")
        else:
            print(f"   #*#*#*# {quiz_name} #*#*#*#")

    # Initialize variables
    quiz_name = quiz['name']
    score = 0
    last_answer = None

    # Separates imported quiz into different lists
    question_list = list(quiz.keys())
    question_data_list = list(quiz.values())
    question_list.remove('scores')
    question_list.remove('name')

    # Repeat for every question
    for question in question_list:

        # Title and last answer printout
        if last_answer is not None:
            quiz_player_title(quiz_name)
            print(f"   Last answer was {last_answer}")
        else:
            quiz_player_title(quiz_name)

        # Setup of variables for use later
        # Creates separate dictionaries and variables for contents of quiz lists
        question_num = question_data_list[question_list.index(
            question)]['IndexNum']
        choices = question_data_list[question_list.index(question)]['choices']
        upper_choices = {key: value.upper() if isinstance(
            value, str) else value for key, value in choices.items()}
        letter_indexes_list = [key for key in choices]
        letter_index_output = '/'.join(letter_indexes_list)
        long_answer = question_data_list[question_list.index(question)]['answer']
        matching_index = 0
        for index, value in upper_choices.items():
            if value == long_answer:
                matching_index = index
                break
        answer = {matching_index: long_answer}

        # Print Question info
        print(f"\n   Question {question_num}:\n")
        print(f"   {question}\n")
        for letter_index, full_answer in choices.items():
            print(f"   {letter_index} - {full_answer}")

        # User answer and checking
        while True:
            user_answer = input(
                f"\n   Select your answer ({letter_index_output}):").upper()

            # Checks user input against answer dictionary
            # Index answer (Correct)
            if user_answer in answer:
                last_answer = "\033[32;49mcorrect\u001b[37m!"
                score += 1
                break

            # Long answer (Correct)
            elif user_answer in answer.values():
                last_answer = "\033[32;49mcorrect\u001b[37m!"
                score += 1
                break

            # Answer is not correct
            elif user_answer not in answer:

                # Same as index choices (Incorrect)
                if user_answer in upper_choices:
                    last_answer = "\033[31;49mincorrect\u001b[37m!"
                    break

                # Same as long answer choices (Incorrect)
                elif user_answer in upper_choices.values():
                    last_answer = "\033[31;49mincorrect\u001b[37m!"
                    break

                # Not the same as anything provided (Error)
                else:
                    print("   Your response was not any of the choices listed, "
                          "   please try again by choosing one of the choices listed.")

    # User Score and other high scores
    quiz_player_title(quiz_name)
    print(f"You scored {score} out of {len(quiz)-1} questions!")
    print("\nWould you like to save your score to the quiz?")
    
    while True:
        score_input = input("\nYour selection (y/n): ")
        if score_input == "y":
            username = str(input("Please enter your name: "))
            quiz['scores'][username] = score
            export_quiz(quiz)
            print("Current High Scores:")
            print_high_scores(quiz)
            break
        elif score_input == "n":
            print("Current High Scores:")
            print_high_scores(quiz)
            print("Skipping score saving...")
            break
        else:
            print("Invalid input! Please enter a valid input (y/n).")

while True:
    # Main routine
    clear_screen()

    # Logo and option strings
    logo = '''
    _.--,-```-.    
   /    /      '.  
  /____/         ; 
  \    \  .``-    '
   \ ___\/    \   :
         \    :   |
         |    ;  . 
        ;   ;   :  
       /   :   :   
       `---'.  |   
        `--..`;    
      .--,_        
      |    |`.     
      `-- -`, ;    
        '---``     
    '''
    options = '''
    #*#*#*# Quizzing #*#*#*#
    OPTIONS
    
    1 - Play the default quiz
    2 - Create a new quiz
    3 - Import and play an existing quiz
    4 - Import and view the high scores of an existing quiz
    5 - Exit
    '''
    # Get the width of the console window
    terminal_width = shutil.get_terminal_size().columns

    # Calculate the number of spaces needed to center the logo and options
    spaces_logo = (terminal_width - max(len(line) for line in logo.split('\n'))) // 2
    spaces_options = (terminal_width - max(len(line) for line in options.split('\n'))) // 2

    # Print the logo and options with the calculated spaces
    print(' ' * spaces_logo + logo)
    print(' ' * spaces_options + options)

    # User selection of choice
    user_selection = input("\n  Your selection (1/2/3/4/5): ")

    # Selection outputs
    # Default Quiz
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
    },
    "scores": {
      "Cam": 19,
      "ethcor2": 16,
      "Jess": 8,
      "Artemis": 20
    },
    "name": "Defualt Quiz"
}
        run_quiz(quiz)
        restart_program()

    # Create a Quiz
    elif user_selection == "2":
        create_quiz()
        break

    # Import and play a quiz
    elif user_selection == "3":
        import_quiz()
        run_quiz(quiz)
        restart_program()
        break

    # Import and view scores of a quiz
    elif user_selection == "4":
        import_quiz()
        clear_screen()
        print("High Scores for this quiz:")
        print_high_scores(quiz)

    # Exit program
    elif user_selection == "5":
        exit()
    else:
        print("Invalid Input. Please try again with a correct input.")
