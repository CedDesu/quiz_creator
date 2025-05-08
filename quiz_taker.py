"""
Quiz taker - 2nd part of quiz creator which uses tkinter library to open a new window for answering the made quiz

"""

import tkinter as tk

def load_questions_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    questions_data = []
    for index in range(0, len(lines), 6):
        if lines[index].startswith("Q") and lines[index + 5].startswith("Correct answer:"):
            question_text = lines[index]
            choices = lines[index + 1 : index + 5]
            correct_answer_line = lines[index + 5]
            questions_data.append((question_text, choices, correct_answer_line))
    return questions_data

def display_quiz_window(questions_data):
    window = tk.Tk()
    window.title("Interactive Quiz")

    canvas = tk.Canvas(window)
    scrollbar = tk.Scrollbar(window, command=canvas.yview)
    question_container = tk.Frame(canvas)

