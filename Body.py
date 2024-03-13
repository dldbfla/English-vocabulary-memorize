import sqlite3
from tkinter import Tk, Label

# 사용자로부터 이름 입력 받기
user_name = input("조회할 사용자의 이름을 입력하세요: ")


# 데이터베이스에서 사용자의 'level' 정보를 가져오는 함수
def fetch_user_level(user_name):
    # 데이터베이스에 연결
    conn = sqlite3.connect('english_test.db')
    cursor = conn.cursor()

    # 입력 받은 이름에 해당하는 사용자의 'id', 'name', 'level' 조회
    cursor.execute("SELECT level FROM users WHERE name = ?", (user_name,))
    level = cursor.fetchone()

    # 연결 종료
    conn.close()

    if level:
        return level[0]
    else:
        return None


# GUI 생성 및 사용자 'level' 데이터 표시
def create_gui_with_user_level(user_name):
    user_level = fetch_user_level(user_name)

    root = Tk()
    root.title(f"{user_name}'s Level Display")

    # 사용자의 'level' 데이터가 있는 경우 GUI에 표시
    if user_level is not None:
        label = Label(root, text=f"Name: {user_name}, Level: {user_level}")
        label.pack()
    else:
        label = Label(root, text="해당 이름을 가진 사용자를 찾을 수 없습니다.")
        label.pack()

    root.mainloop()


# GUI 실행
create_gui_with_user_level(user_name)
