"""
Quiz taker - 2nd part of quiz creator which uses tkinter library to open a new window for answering the made quiz

"""

import tkinter as tk

def load_questions_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    questions_data = []
    for index in range(0, len(lines), 6):
        if lines[index].startswith("Q") and lines[index