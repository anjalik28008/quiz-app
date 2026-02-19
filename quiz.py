
questions = [
    {
        "question": "What is the output of print(2 + 3)?",
        "options": ["A. 23", "B. 5", "C. 6", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "What data type is [1, 2, 3] in Python?",
        "options": ["A. Tuple", "B. Dictionary", "C. Set", "D. List"],
        "answer": "D"
    },
    {
        "question": "Which of these is used to take user input in Python?",
        "options": ["A. scan()", "B. input()", "C. get()", "D. read()"],
        "answer": "B"
    },
    {
        "question": "What does len('hello') return?",
        "options": ["A. 4", "B. 6", "C. 5", "D. Error"],
        "answer": "C"
    }
]

score = 0

print("===== Python Quiz =====\n")

for i, q in enumerate(questions):
    print(f"Q{i+1}. {q['question']}")
    for option in q['options']:
        print(option)
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == q['answer']:
        print("✓ Correct!\n")
        score += 1
    else:
        print(f"✗ Wrong! Correct answer is {q['answer']}\n")

print(f"===== Quiz Complete! =====")
print(f"Your Score: {score}/{len(questions)}")