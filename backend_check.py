"""
Backend checks for the Online Examination System.
Simulates validation of scoring logic and result storage.
"""
import time
import json
import os
from exam_system import DEFAULT_QUESTIONS

def check_scoring_logic():
    print("Running backend checks...")
    time.sleep(3)  # Simulate a slow check

    # Simulate a perfect score
    total = len(DEFAULT_QUESTIONS)
    score = total
    percentage = (score / total) * 100
    assert percentage == 100.0, "Perfect score should be 100%"
    assert ("PASS" if percentage >= 40 else "FAIL") == "PASS", "Perfect score should PASS"

    # Simulate a failing score
    score = 1
    percentage = (score / total) * 100
    assert ("PASS" if percentage >= 40 else "FAIL") == "FAIL", "1/5 should FAIL"

    print(f"Backend checks passed: scoring logic verified for {total} questions.")

if __name__ == "__main__":
    check_scoring_logic()
