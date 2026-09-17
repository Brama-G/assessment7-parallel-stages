"""
Online Examination and Evaluation System
A simple, single-file Python application.
"""

import json
import os
import random
from datetime import datetime

# ---------- Configuration ----------
QUESTIONS_FILE = "questions.json"
RESULTS_FILE = "results.json"

# Default question bank (used if questions.json doesn't exist)
DEFAULT_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "id": 2,
        "question": "Which language is primarily used for data science?",
        "options": ["A) Java", "B) C++", "C) Python", "D) HTML"],
        "answer": "C"
    },
    {
        "id": 3,
        "question": "What does CPU stand for?",
        "options": ["A) Central Process Unit", "B) Computer Personal Unit",
                    "C) Central Processing Unit", "D) Central Processor Unit"],
        "answer": "C"
    },
    {
        "id": 4,
        "question": "Which of these is a Python web framework?",
        "options": ["A) Django", "B) React", "C) Angular", "D) Vue"],
        "answer": "A"
    },
    {
        "id": 5,
        "question": "What is 7 x 8?",
        "options": ["A) 54", "B) 56", "C) 64", "D) 48"],
        "answer": "B"
    }
]

# ---------- Utility Functions ----------
def load_questions():
    """Load questions from JSON file or return defaults."""
    if os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "r") as f:
            return json.load(f)
    else:
        save_questions(DEFAULT_QUESTIONS)
        return DEFAULT_QUESTIONS

def save_questions(questions):
    """Save questions to JSON file."""
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=2)

def load_results():
    """Load past results from JSON file."""
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_results(results):
    """Save results to JSON file."""
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2)

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 50)
    print(f"  {title.center(46)}")
    print("=" * 50)

# ---------- Core Features ----------
def take_exam(student_name):
    """Conduct the exam and return the score."""
    questions = load_questions()
    if not questions:
        print("\nNo questions available. Please ask the admin to add questions.")
        return None

    random.shuffle(questions)
    score = 0
    total = len(questions)

    print_header(f"EXAM STARTED - {student_name}")
    print(f"Total Questions: {total}")
    print("Type the letter (A/B/C/D) of your answer and press Enter.\n")

    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}. {q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")

        while True:
            answer = input("Your answer: ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("Invalid input. Please enter A, B, C, or D.")

        if answer == q["answer"].upper():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong. Correct answer: {q['answer']}\n")

    percentage = (score / total) * 100
    print_header("EXAM COMPLETED")
    print(f"Student : {student_name}")
    print(f"Score   : {score}/{total}")
    print(f"Percent : {percentage:.2f}%")
    print(f"Result  : {'PASS' if percentage >= 40 else 'FAIL'}")

    # Save result
    results = load_results()
    results.append({
        "student": student_name,
        "score": score,
        "total": total,
        "percentage": round(percentage, 2),
        "status": "PASS" if percentage >= 40 else "FAIL",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_results(results)
    return percentage

def view_results():
    """Display all past exam results."""
    results = load_results()
    if not results:
        print("\nNo results found yet.")
        return

    print_header("ALL EXAM RESULTS")
    print(f"{'#':<4}{'Student':<20}{'Score':<10}{'Percent':<10}{'Status':<8}{'Date'}")
    print("-" * 80)
    for i, r in enumerate(results, start=1):
        print(f"{i:<4}{r['student']:<20}{r['score']}/{r['total']:<7}"
              f"{r['percentage']:<10}{r['status']:<8}{r['date']}")

def add_question():
    """Admin: add a new question."""
    print_header("ADD NEW QUESTION")
    question = input("Enter the question: ").strip()
    options = []
    for letter in ["A", "B", "C", "D"]:
        opt = input(f"Enter option {letter}: ").strip()
        options.append(f"{letter}) {opt}")
    answer = input("Enter correct answer (A/B/C/D): ").strip().upper()
    while answer not in ("A", "B", "C", "D"):
        answer = input("Invalid. Enter A/B/C/D: ").strip().upper()

    questions = load_questions()
    new_id = max([q["id"] for q in questions], default=0) + 1
    questions.append({
        "id": new_id,
        "question": question,
        "options": options,
        "answer": answer
    })
    save_questions(questions)
    print("\nQuestion added successfully!")

def view_questions():
    """Admin: view all questions."""
    questions = load_questions()
    if not questions:
        print("\nNo questions in the bank.")
        return

    print_header("QUESTION BANK")
    for q in questions:
        print(f"\nID {q['id']}: {q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")
        print(f"   Answer: {q['answer']}")

def admin_menu():
    """Admin sub-menu."""
    while True:
        print_header("ADMIN MENU")
        print("1. Add Question")
        print("2. View All Questions")
        print("3. View All Results")
        print("4. Back to Main Menu")
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            view_results()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

# ---------- Main Menu ----------
def main():
    print_header("ONLINE EXAMINATION & EVALUATION SYSTEM")
    while True:
        print("\n1. Take Exam")
        print("2. View Results")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            name = input("Enter your name: ").strip()
            if name:
                take_exam(name)
            else:
                print("Name cannot be empty.")
        elif choice == "2":
            view_results()
        elif choice == "3":
            password = input("Enter admin password: ").strip()
            if password == "admin123":   # Change this password as needed
                admin_menu()
            else:
                print("Incorrect password.")
        elif choice == "4":
            print("\nThank you for using the Online Examination System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# ---------- Entry Point ----------
if __name__ == "__main__":
    main()
