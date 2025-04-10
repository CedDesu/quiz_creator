"""
next_question = input("")

save to file code
"""

def quiz_creator():

    input("Welcome to Quiz_Creator v.1, please press any button to start.\n")

    #Asks the user for a question and 4 choices
    while True:
        input_question = input("Enter a question: \n")

        choices = {}
        for choice in ['a', 'b', 'c', 'd']:
            answer = input(f"Enter choice {choice}: ")
            choices[choice] = answer

    while True:
        correct_answer = input("Which choice is the correct answer?: \n")
        if correct_answer in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Please type a valid input. (a/b/c/d)")












if __name__ == "__main__":
    quiz_creator()