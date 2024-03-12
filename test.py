import random
import pyttsx3
import tkinter as tk

# TTS 엔진 초기화
engine = pyttsx3.init()
# 사용 가능한 음성 목록 가져오기
voices = engine.getProperty('voices')
# 영어 음성으로 설정
for voice in voices:
    if 'English' in voice.name:  # 음성 이름에 'English'가 포함되어 있는지 확인
        engine.setProperty('voice', voice.id)
        break
# 음성 속도 조절
engine.setProperty('rate', 150)
# 사용할 단어 리스트
word_list = [
    {'Word': 'Environment', 'Pronunciation': '인바이어먼트', 'Meaning': '환경'},
    {'Word': 'Globalization', 'Pronunciation': '글로벌라이제이션', 'Meaning': '세계화'},
    {'Word': 'Innovation', 'Pronunciation': '이노베이션', 'Meaning': '혁신'},
    {'Word': 'Entrepreneurship', 'Pronunciation': '엔트러프러너십', 'Meaning': '창업'},
    {'Word': 'Sustainability', 'Pronunciation': '서스테이너빌리티', 'Meaning': '지속 가능성'},
    {'Word': 'Technology', 'Pronunciation': '테크놀러지', 'Meaning': '기술'},
    {'Word': 'Diversity', 'Pronunciation': '다이버시티', 'Meaning': '다양성'},
    {'Word': 'Leadership', 'Pronunciation': '리더십', 'Meaning': '리더십'},
    {'Word': 'Critical thinking', 'Pronunciation': '크리티컬 띵킹', 'Meaning': '비판적 사고'},
    {'Word': 'Problem solving', 'Pronunciation': '프라블럼-솔빙', 'Meaning': '문제 해결'},
    {'Word': 'Research', 'Pronunciation': '리서치', 'Meaning': '연구'},
    {'Word': 'Analysis', 'Pronunciation': '어낼리시스', 'Meaning': '분석'},
    {'Word': 'Experiment', 'Pronunciation': '익스페리먼트', 'Meaning': '실험'},
    {'Word': 'Cybersecurity', 'Pronunciation': '사이버시큐리티', 'Meaning': '사이버 보안'},
    {'Word': 'Graduation', 'Pronunciation': '그래듀에이션', 'Meaning': '졸업'},
    {'Word': 'Professor', 'Pronunciation': '프로페서', 'Meaning': '교수'},
    {'Word': 'Scholarship', 'Pronunciation': '스칼라쉽', 'Meaning': '장학금'},
    {'Word': 'Ethics', 'Pronunciation': '에틱스', 'Meaning': '윤리'},
    {'Word': 'Interesting', 'Pronunciation': '인터레스팅', 'Meaning': '흥미로운'},
    {'Word': 'Serendipity', 'Pronunciation': '세렌디피티', 'Meaning': '우연한 행운'},
    {'Word':'Intricate', 'Pronunciation': '인트리케이트', 'Meaning': '복잡한'},
    {'Word': 'Enigma', 'Pronunciation': '이니그마', 'Meaning': '수수께끼'},
    {'Word': 'Indispensable', 'Pronunciation': '인디스펜서블', 'Meaning': '필수적인'},
    {'Word': 'Zeal', 'Pronunciation': '질', 'Meaning': '열정'},
    {'Word': 'Intrigue', 'Pronunciation': '인트리그', 'Meaning': '흥미를 끌다'},
    {'Word': 'Exquisite', 'Pronunciation': '익스퀴짓', 'Meaning': '아주 아름다운'},
    {'Word': 'Empathy', 'Pronunciation': '엠파시', 'Meaning': '공감'},
    {'Word': 'Ambiguous', 'Pronunciation': '앰비규어스', 'Meaning': '애매한'},
    {'Word': 'Impeccable', 'Pronunciation': '임페커블', 'Meaning': '흠잡을 데 없는'},
    {'Word': 'Tenacious', 'Pronunciation': '테네이셔스', 'Meaning': '끈질긴'},
    {'Word': 'Serene', 'Pronunciation': '세린', 'Meaning': '평온한'},
    {'Word': 'Solitude', 'Pronunciation': '솔리튜드', 'Meaning': '고독'},
    {'Word': 'Reverie', 'Pronunciation': '레버리', 'Meaning': '몽상'},
    {'Word': 'Nefarious', 'Pronunciation': '다페어리어스', 'Meaning': '사악한'},
    {'Word': 'Mellifluous', 'Pronunciation': '멜리플루어스', 'Meaning': '달콤한'},
    {'Word': 'Epitome', 'Pronunciation': '에피토미', 'Meaning': '전형적인 예'},
    {'Word': 'Supercilious', 'Pronunciation': '슈퍼실리어스', 'Meaning': '거만한'},
    {'Word': 'Ostentatious', 'Pronunciation': '어스텐테이셔스', 'Meaning': '과시하는'},
    {'Word': 'Ineffable', 'Pronunciation': '이네파블', 'Meaning': '말로 표현할 수 없는'},
    {'Word': 'Capricious', 'Pronunciation': '캡리셔스', 'Meaning': '변덕스러운'},
    {'Word': 'Dude', 'Pronunciation': '두드', 'Meaning': '친구, 재밌는 사람'},
    {'Word': 'Chill', 'Pronunciation': '칠', 'Meaning': '느긋하게 지내다'},
    {'Word': 'Hangover', 'Pronunciation': '항오버', 'Meaning': '숙취'},
    {'Word': 'Crush', 'Pronunciation': '크러쉬', 'Meaning': '짝사랑'},
    {'Word': 'FOMO (Fear Of Missing Out)', 'Pronunciation': '포모', 'Meaning': '놓치는 두려움'},
    {'Word': 'Hangry (Hungry + Angry)', 'Pronunciation': '행그리', 'Meaning': '배고픈 상태에서 성난'},
    {'Word': 'Binge-watch', 'Pronunciation': '빈지워치', 'Meaning': '한꺼번에 많은 양의 콘텐츠를 연속으로 시청하다'},
    {'Word': 'Netflix and chill', 'Pronunciation': '넷플릭스 앤 칠', 'Meaning': '영어권판 라면먹고갈래?뜻'},
    {'Word': 'Hangover', 'Pronunciation': '항오버', 'Meaning': '숙취'},
    {'Word': 'Hang out', 'Pronunciation': '항 아웃', 'Meaning': '어울리다, 놀다'},
    {'Word': 'Chill', 'Pronunciation': '칠', 'Meaning': '쿨하게 지내다'},
    {'Word': 'How  it going?', 'Pronunciation': '하우 잇 고잉?', 'Meaning': '어떻게 지내?'},
    {'Word': 'Bestie', 'Pronunciation': '베스티', 'Meaning': '절친'},
]
# 현재 단어와 입력된 단어를 담을 변수
current_word = {}
typed_word = ''
def check_word(event=None):
    global typed_word
    typed_word = entry.get()
    
def speak_word():
    engine.setProperty('rate', 150)  # 음성 속도 조절
    engine.say(current_word['Word'])  # 현재 단어 발음
    engine.runAndWait()


def start_game():
    global current_word
    current_word = random.choice(word_list)
    word_label.config(text=f"단어: {current_word['Word']}")
    entry.delete(0, tk.END)
    entry.focus_set()
    next_button.config(state=tk.DISABLED)


def speak_word_func():
    pass


def check_word(event=None):
    global typed_word
    typed_word = entry.get()
    if typed_word == current_word['Word']:
        result_label.config(text="정답입니다!", fg="green")
        # 정답일 경우 한국어 뜻과 발음 보여주기
        word_label.config(text=f"뜻: {current_word['Meaning']}\n발음: {current_word['Pronunciation']}")
        speak_word()  # 수정된 부분: 함수 호출
        next_button.config(state=tk.NORMAL)  # 정답일 경우 다음 버튼 활성화
    else:
        result_label.config(text="틀렸습니다. 다음 버튼을 눌러주세요.", fg="red")
        entry.delete(0, tk.END)
        entry.focus_set()
        next_button.config(state=tk.DISABLED)  # 오답일 경우 다음 버튼 비활성화

def next_word(event=None):
    start_game()

# GUI 생성
window = tk.Tk()
window.title("한컴타자 연습")

word_label = tk.Label(window, text="", font=("Helvetica", 20))
word_label.pack(pady=20)

entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack()

entry.bind("<Return>", check_word)  # Enter 키로도 확인 가능하도록 설정
entry.bind("<F1>", next_word)

# 좌쉬프트 키로 다음 단어로 넘어가도록 설정
check_button = tk.Button(window, text="확인", command=check_word)
check_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

next_button = tk.Button(window, text="다음", command=next_word, state=tk.DISABLED)  # 초기에는 비활성화 상태로 설정
next_button.pack(pady=10)

timer_label = tk.Label(window, text="")
timer_label.pack()

start_game()  # 게임 시작

window.mainloop()
