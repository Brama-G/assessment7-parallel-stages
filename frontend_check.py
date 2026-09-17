"""
Frontend checks for the Online Examination System.
Simulates validation of the user-facing layer (question display, options format).
"""
import time
from exam_system import DEFAULT_QUESTIONS

def check_question_formatting():
    print("Running frontend checks...")
    time.sleep(3)  # Simulate a slow check

    for q in DEFAULT_QUESTIONS:
        # Every question must have exactly 4 options
        assert len(q["options"]) == 4, f"Question {q['id']} does not have 4 options"
        # Every option must start with a letter prefix like "A) "
        for opt in q["options"]:
            assert opt[0] in "ABCD", f"Option '{opt}' missing letter prefix"
            assert opt[1:3] == ") ", f"Option '{opt}' missing ') ' separator"

    print(f"Frontend checks passed: {len(DEFAULT_QUESTIONS)} questions formatted correctly.")

if __name__ == "__main__":
    check_question_formatting()
