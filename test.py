import tkinter as tk
from tkinter import messagebox, Label, Radiobutton, Button, StringVar
import sqlite3



# 영어 수준을 판별하는 함수
def determine_level(score, total_questions):
    score_percentage = (score / total_questions) * 100
    if score_percentage < 20:
        return '초등'
    elif score_percentage < 40:
        return '중등'
    elif score_percentage < 60:
        return '고등'
    elif score_percentage < 80:
        return '대학생'
    else:
        return '원어민'

# 사용자의 수준과 이름을 데이터베이스에 저장하는 함수
def save_user_info(name, level):
    conn = sqlite3.connect('english_test.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    level TEXT)''')
    conn.execute("INSERT INTO users (name, level) VALUES (?, ?)", (name, level))
    conn.commit()
    conn.close()

# 테스트 진행 함수
def conduct_test(questions):
    global current_question, score, user_answer
    score = 0
    current_question = 0
    user_answer = StringVar()

    display_question(questions[current_question])

def display_question(question):
    global options_frame, question_label, root

    for widget in options_frame.winfo_children():
        widget.destroy()

    question_text, choices, _ = question
    question_label.config(text=question_text)

    for choice in choices:
        Radiobutton(options_frame, text=choice, variable=user_answer, value=choice[0], command=select_answer).pack(
            anchor='w')

    root.update()

def select_answer():
    next_button.config(state="normal")

def next_question():
    global current_question, score
    _, _, correct_answer = questions[current_question]

    if user_answer.get().lower() == correct_answer.lower():
        score += 1

    current_question += 1
    if current_question < len(questions):
        display_question(questions[current_question])
        next_button.config(state="disabled")
        user_answer.set(None)
    else:
        level = determine_level(score, len(questions))
        messagebox.showinfo("테스트 결과", f"당신의 점수는 {score}/{len(questions)}입니다. 당신의 영어 수준은 {level}입니다.")

        # 사용자의 이름을 입력받습니다.
        name = input("이름을 입력하세요: ")

        # 사용자의 수준과 이름을 데이터베이스에 저장합니다.
        save_user_info(name, level)

        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("영어 단어 테스트")

    question_label = Label(root, text="", width=50, height=4)
    question_label.pack(pady=(10, 20))

    options_frame = tk.Frame(root)
    options_frame.pack()

    next_button = Button(root, text="다음", command=next_question)
    next_button.pack(pady=(10, 20))
    next_button.config(state="disabled")

questions = [
    ("다음 중 '사과'를 영어로 가장 잘 번역한 것은?", ["a. Apple", "b. Banana", "c. Cherry"], "a"),
    ("'고양이 '를 영어로 무엇이라고 할까요?", ["a. Cat", "b. Dog", "c. Bird"], "a"),
    ("'물'을 영어로 무엇이라고 할까요?", ["a. Milk", "b. Juice", "c. Water"], "c"),
    ("'햄버거'를 영어로 무엇이라고 할까요?",["a. Pizza","b. Hamburger","c. Sandwich"],"b"),
    ("'환경'을 영어로 무엇이라고 할까요?", ["a. Environment", "b. Ecology", "c. Nature"], "a"),
    ("'도전'을 영어로 무엇이라고 할까요?", ["a. Challenge", "b. Adventure", "c. Opportunity"], "a"),
    ("'지속적인'을 영어로 무엇이라고 할까요?", ["a. Endless", "b. Permanent", "c. Continuous"], "c"),
    ("'연구'를 영어로 무엇이라고 할까요?", ["a. Study", "b.  Research", "c. Investigation"], "b"),
    ("'취약한'을 영어로 무엇이라고 할까요?", ["a.  Fragile", "b. Vulnerable", "c. Weak"], "b"),
    ("'포괄적인'을 영어로 무엇이라고 할까요?", ["a. Inclusive", "b. Encompassing", "c. Comprehensive"], "c"),
    ("'효과적인'을 영어로 무엇이라고 할까요?", ["a. Efficient", "b. Effective", "c. Productive"], "b"),
    ("'추상적인'을 영어로 무엇이라고 할까요?", ["a. Abstract", "b. Imaginary", "c. Conceptual"], "a"),
    ("'자극적인'을 영어로 무엇이라고 할까요?", ["a. Stimulating", "b. Provocative", "c. Exciting"], "a"),
    ("'인식'을 영어로 무엇이라고 할까요?", ["a. Recognition", "b. Perception", "c. Awareness"], "b"),
    ("'비판적 사고'를 영어로 무엇이라고 할까요?", ["a. Critical thinking", "b. Analytical reasoning", "c. Logical analysis"], "a"),
    ("'혁신'을 영어로 무엇이라고 할까요?", ["a. Revolution", "b. Innovation", "c. Transformation"], "b"),
    ("'통합'을 영어로 무엇이라고 할까요?", ["a. Integration", "b. Consolidation", "c. Unification"], "a"),
    ("'비판적인'를 영어로 무엇이라고 할까요?", ["a. Analytical", "b. Critical", "c. Judicious"], "b"),
    ("'어리석은'을 영어로 무엇이라고 할까요?", ["a. Dim-witted", "b. Daft", "c.  Foolish"], "c"),
    ("'자리를 비우다'를 영어로 무엇이라고 할까요?", ["a. Split", "b. Dip", "c. Bail"], "c"),
    ("'최고의'를 영어로 무엇이라고 할까요?", ["a. Top-notch", "b. Prime", "c. Stellar"], "a"),
    ("'돈'을 영어로 무엇이라고 할까요?", ["a. Dough", "b. Cash", "c. Moolah"], "a"),
    ("'급식'을 영어로 무엇이라고 할까요?", ["a. Grub", "b. Chow", "c. Meal"], "b"),

]

conduct_test(questions)

root.mainloop()
