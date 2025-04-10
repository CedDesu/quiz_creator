"""
next_question = input("")

save to file code
"""

def quiz_creator():
    user_quiz_data = []

    input("Welcome to Quiz_Creator v.1, please press any button to start.\n")

    #Asks the user for a question and 4 choices
    while True:
        input_question = input("Enter a question: \n")

        choices = {}
        for choice in ['a', 'b', 'c', 'd']:
            answer = input(f"Enter choice {choice}: ")
            choices[choice] = answer

        while True:
            correct_answer = input("Which choice is the correct answer?: \n").strip()
            if correct_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Please type a valid input. (a/b/c/d)")

        user_quiz_data.append({
            "question": input_question,
            "choices": choices,
            "answers": correct_answer
        })

        next_question = input("Do you want to input another question? (yes/no)\n").strip().lower()
        if next_question not in ('yes','y'):
            break

    with open("quiz.txt", "w") as f:
        for idx, item in enumerate(user_quiz_data, 1):
            f.write(f"Q{idx}: {item['question']}\n")
            for key in ['a', 'b', 'c', 'd']:
                f.write(f"  {key}) {item['options'][key]}\n")

















if __name__ == "__main__":
    quiz_creator()