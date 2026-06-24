# ============================================================
# PHASE 1 PROJECT — Student Result Calculator + Quiz Game
# ============================================================
# This project uses EVERYTHING from Phase 1:
# ✅ Variables & data types
# ✅ Operators & expressions
# ✅ If / else conditions
# ✅ Loops (for & while)
# ✅ Functions
# ✅ Lists, Dicts
# ✅ Debugging (try/except)
# NEW FEATURES:
# ✅ Difficulty levels (Easy / Medium / Hard)
# ✅ Timer per question
# ============================================================
 
import threading
import time
 
 
# ======================================================
# PART 1 — STUDENT RESULT CALCULATOR
# ======================================================
 
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"
 
 
def get_status(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
 
 
def calculate_results(student_name, subjects):
    total   = sum(subjects.values())
    average = total / len(subjects)
    return {
        "name"   : student_name,
        "total"  : total,
        "average": round(average, 2),
        "grade"  : get_grade(average),
        "status" : get_status(average)
    }
 
 
def print_result_card(result, subjects):
    print("\n" + "=" * 45)
    print(f"       RESULT CARD — {result['name'].upper()}")
    print("=" * 45)
    for subject, marks in subjects.items():
        print(f"  {subject:<15} : {marks} / 100")
    print("-" * 45)
    print(f"  {'Total':<15} : {result['total']} / {len(subjects) * 100}")
    print(f"  {'Average':<15} : {result['average']}")
    print(f"  {'Grade':<15} : {result['grade']}")
    print(f"  {'Status':<15} : {result['status']}")
    print("=" * 45)
 
 
def student_result_calculator():
    print("\n" + "#" * 45)
    print("#     STUDENT RESULT CALCULATOR           #")
    print("#" * 45)
 
    students_data = []
 
    while True:
        try:
            num_students = int(input("\nHow many students? "))
            if num_students <= 0:
                print("Please enter a number greater than 0")
            else:
                break
        except ValueError:
            print("Invalid input! Enter a number")
 
    while True:
        try:
            num_subjects = int(input("How many subjects? "))
            if num_subjects <= 0:
                print("Please enter a number greater than 0")
            else:
                break
        except ValueError:
            print("Invalid input! Enter a number")
 
    subject_names = []
    print("\nEnter subject names:")
    for i in range(num_subjects):
        name = input(f"  Subject {i + 1}: ")
        subject_names.append(name)
 
    for s in range(num_students):
        print(f"\n--- Student {s + 1} ---")
        student_name = input("Student name: ")
        subjects = {}
        for subject in subject_names:
            while True:
                try:
                    marks = int(input(f"  Marks in {subject} (0-100): "))
                    if 0 <= marks <= 100:
                        subjects[subject] = marks
                        break
                    else:
                        print("  Marks must be between 0 and 100")
                except ValueError:
                    print("  Invalid input! Enter a number")
 
        result = calculate_results(student_name, subjects)
        students_data.append((result, subjects))
 
    print("\n\n========== ALL RESULTS ==========")
    for result, subjects in students_data:
        print_result_card(result, subjects)
 
    print("\n========== CLASS SUMMARY ==========")
    averages = [r["average"] for r, _ in students_data]
    names    = [r["name"] for r, _ in students_data]
    passed   = [r["name"] for r, _ in students_data if r["status"] == "Pass"]
    failed   = [r["name"] for r, _ in students_data if r["status"] == "Fail"]
 
    topper_index = averages.index(max(averages))
    print(f"  Total Students  : {len(students_data)}")
    print(f"  Passed          : {len(passed)}")
    print(f"  Failed          : {len(failed)}")
    print(f"  Class Average   : {round(sum(averages) / len(averages), 2)}")
    print(f"  Topper          : {names[topper_index]} ({max(averages)}%)")
    if failed:
        print(f"  Failed Students : {', '.join(failed)}")
    print("=" * 35)
 
 
# ======================================================
# PART 2 — QUIZ GAME WITH DIFFICULTY + TIMER
# ======================================================
 
def load_questions():
    questions = {
        "easy": [
            {
                "question"   : "What is the output of: 2 + 3 * 2 ?",
                "options"    : ["A) 10", "B) 8", "C) 7", "D) 6"],
                "answer"     : "B",
                "explanation": "* is done before + (BODMAS) — 3*2=6, then 2+6=8"
            },
            {
                "question"   : "Which keyword defines a function in Python?",
                "options"    : ["A) function", "B) define", "C) def", "D) fun"],
                "answer"     : "C",
                "explanation": "def is used to define functions in Python"
            },
            {
                "question"   : "What does len([1, 2, 3, 4, 5]) return?",
                "options"    : ["A) 4", "B) 6", "C) 5", "D) 0"],
                "answer"     : "C",
                "explanation": "len() returns the number of items in a list"
            },
            {
                "question"   : "What is the output of: 10 % 3 ?",
                "options"    : ["A) 3", "B) 1", "C) 0", "D) 2"],
                "answer"     : "B",
                "explanation": "% gives remainder — 10 divided by 3 is 3 remainder 1"
            },
            {
                "question"   : "What does not True give?",
                "options"    : ["A) True", "B) 1", "C) None", "D) False"],
                "answer"     : "D",
                "explanation": "not flips True to False and False to True"
            },
        ],
        "medium": [
            {
                "question"   : "What is the output of: 2 ** 10 ?",
                "options"    : ["A) 20", "B) 512", "C) 1024", "D) 100"],
                "answer"     : "C",
                "explanation": "** is power — 2 to the power 10 = 1024"
            },
            {
                "question"   : "Which of these CANNOT be changed after creation?",
                "options"    : ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
                "answer"     : "D",
                "explanation": "Tuples are immutable — they cannot be modified"
            },
            {
                "question"   : "What does range(1, 6) produce?",
                "options"    : ["A) 1 2 3 4 5 6", "B) 1 2 3 4 5", "C) 0 1 2 3 4 5", "D) 2 3 4 5 6"],
                "answer"     : "B",
                "explanation": "range(1, 6) gives 1,2,3,4,5 — stop value is excluded"
            },
            {
                "question"   : "How do you add an item to the end of a list?",
                "options"    : ["A) list.add()", "B) list.push()", "C) list.append()", "D) list.insert()"],
                "answer"     : "C",
                "explanation": "append() adds an item to the end of a list"
            },
            {
                "question"   : "What keyword exits a loop early?",
                "options"    : ["A) exit", "B) stop", "C) return", "D) break"],
                "answer"     : "D",
                "explanation": "break immediately exits the loop"
            },
        ],
        "hard": [
            {
                "question"   : "What is the output of: 10 // 3 ?",
                "options"    : ["A) 3.33", "B) 3", "C) 4", "D) 1"],
                "answer"     : "B",
                "explanation": "// is floor division — drops the decimal"
            },
            {
                "question"   : "What does 5 > 3 and 2 > 8 give?",
                "options"    : ["A) True", "B) False", "C) Error", "D) None"],
                "answer"     : "B",
                "explanation": "and needs BOTH sides True — 2>8 is False so result is False"
            },
            {
                "question"   : "What is the output of: bool(0) ?",
                "options"    : ["A) 0", "B) True", "C) False", "D) None"],
                "answer"     : "C",
                "explanation": "0 is falsy in Python — bool(0) gives False"
            },
            {
                "question"   : "What does dict.get('key', 'default') do if key is missing?",
                "options"    : ["A) Raises KeyError", "B) Returns None", "C) Returns 'default'", "D) Returns 0"],
                "answer"     : "C",
                "explanation": ".get() returns the default value if key is not found"
            },
            {
                "question"   : "What is the output of: [i*2 for i in range(3)] ?",
                "options"    : ["A) [1,2,3]", "B) [0,2,4]", "C) [2,4,6]", "D) [0,1,2]"],
                "answer"     : "B",
                "explanation": "range(3) gives 0,1,2 — multiplied by 2 gives 0,2,4"
            },
        ]
    }
    return questions
 
 
# ── TIMER FUNCTION ────────────────────────────────────────────
 
def timed_input(prompt, time_limit):
    """Ask for input with a countdown timer"""
    answer = [None]
    timed_out = [False]
 
    def get_input():
        try:
            answer[0] = input(prompt)
        except:
            pass
 
    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
 
    # countdown display
    for remaining in range(time_limit, 0, -1):
        if not thread.is_alive():
            break
        print(f"\r  ⏱  Time left: {remaining}s   ", end="", flush=True)
        time.sleep(1)
 
    print()  # newline after timer
 
    if thread.is_alive():
        timed_out[0] = True
        print("  ⌛ Time's up! Moving to next question.")
 
    return answer[0], timed_out[0]
 
 
def run_quiz(player_name):
    all_questions = load_questions()
 
    # Choose difficulty
    print("\n" + "=" * 45)
    print("         CHOOSE DIFFICULTY LEVEL")
    print("=" * 45)
    print("  1. Easy    — 30 seconds per question")
    print("  2. Medium  — 20 seconds per question")
    print("  3. Hard    — 10 seconds per question")
    print("=" * 45)
 
    while True:
        diff_choice = input("Enter choice (1/2/3): ").strip()
        if diff_choice == "1":
            difficulty  = "easy"
            time_limit  = 30
            diff_label  = "Easy"
            break
        elif diff_choice == "2":
            difficulty  = "medium"
            time_limit  = 20
            diff_label  = "Medium"
            break
        elif diff_choice == "3":
            difficulty  = "hard"
            time_limit  = 10
            diff_label  = "Hard"
            break
        else:
            print("Please enter 1, 2 or 3")
 
    questions = all_questions[difficulty]
    score     = 0
    total     = len(questions)
    wrong     = []
 
    print("\n" + "#" * 45)
    print("#           PYTHON QUIZ GAME              #")
    print("#" * 45)
    print(f"\n  Player     : {player_name}")
    print(f"  Difficulty : {diff_label}")
    print(f"  Questions  : {total}")
    print(f"  Time/Q     : {time_limit} seconds")
    print(f"  Scoring    : +1 correct | 0 wrong | 0 timeout")
    print("\nPress Enter to start...")
    input()
 
    for i, q in enumerate(questions):
        print(f"\n{'─' * 45}")
        print(f"  Q{i + 1} / {total}  [{diff_label}]")
        print(f"{'─' * 45}")
        print(f"  {q['question']}\n")
        for option in q["options"]:
            print(f"     {option}")
        print()
 
        answer, timed_out = timed_input("  Your answer (A/B/C/D): ", time_limit)
 
        if timed_out or answer is None:
            print(f"  ❌ No answer! Correct answer was: {q['answer']}")
            print(f"  💡 {q['explanation']}")
            wrong.append(q)
        else:
            answer = answer.strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                print(f"  ⚠️  Invalid answer! Correct answer was: {q['answer']}")
                wrong.append(q)
            elif answer == q["answer"]:
                print("  ✅ Correct!")
                score += 1
            else:
                print(f"  ❌ Wrong! Correct answer: {q['answer']}")
                print(f"  💡 {q['explanation']}")
                wrong.append(q)
 
    # Final result
    percentage = round(score / total * 100, 1)
    print("\n" + "=" * 45)
    print(f"       QUIZ RESULT — {player_name.upper()}")
    print("=" * 45)
    print(f"  Difficulty  : {diff_label}")
    print(f"  Score       : {score} / {total}")
    print(f"  Percentage  : {percentage}%")
    print(f"  Time/Q      : {time_limit} seconds")
 
    if score == total:
        print("  🏆 Perfect Score! Outstanding!")
    elif score >= 4:
        print("  🎉 Excellent! You know Python well!")
    elif score >= 3:
        print("  👍 Good job! Keep practicing!")
    elif score >= 2:
        print("  📚 Fair. Revise the topics again.")
    else:
        print("  💪 Keep going! Practice makes perfect.")
 
    if wrong:
        print(f"\n  Topics to revise:")
        for q in wrong:
            print(f"  → {q['question'][:50]}...")
            print(f"     💡 {q['explanation']}")
 
    print("=" * 45)
    return score
 
 
# ======================================================
# MAIN MENU
# ======================================================
 
def main():
    print("\n" + "*" * 45)
    print("*       PHASE 1 PROJECT — PYTHON          *")
    print("*   Student Result Calculator + Quiz Game *")
    print("*" * 45)
 
    player_name = input("\nEnter your name to get started: ")
 
    while True:
        print(f"\nHello, {player_name}! What do you want to do?")
        print("  1. Student Result Calculator")
        print("  2. Python Quiz Game")
        print("  3. Exit")
 
        choice = input("\nEnter choice (1/2/3): ").strip()
 
        if choice == "1":
            student_result_calculator()
        elif choice == "2":
            run_quiz(player_name)
        elif choice == "3":
            print(f"\nGoodbye, {player_name}! Keep coding! 🚀")
            break
        else:
            print("Invalid choice! Enter 1, 2 or 3")
            continue
 
        again = input("\nGo back to main menu? (yes/no): ").strip().lower()
        if again != "yes":
            print(f"\nGoodbye, {player_name}! Keep coding! 🚀")
            break
 
main()