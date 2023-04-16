from colorama import init, Fore, Style
import msvcrt
import random
import os

if not os.path.isfile("type.txt"):
    print("type.txt 파일이 존재하지 않습니다.\n\ntype.txt를 만들어주세요.")
    while True:
        pass

# colorama 모듈 초기화
init()

length = int(input("타이핑 할때마다 출력되는 값을 입력해주세요. : "))
color = str(input("색깔을 지정해주세요. 예시) GREEN , RED , WHITE : "))
justcheck = input("만약 종료하고 싶으시다면 [CTRL + C] 를 눌러 종료하세요. (아무 키를 눌러 진행)")

typelength = length
typecolor = color.upper()

os.system("cls")

# type.txt 파일에서 단어 리스트를 읽어옴
with open("type.txt", "r", encoding="utf-8") as f:
    words = f.readlines()
words = [word.strip() for word in words]

while True:
    # 출력
    for word in words:
        i = 0
        while i < len(word):
            for j in range(typelength):
                if i + j >= len(word):
                    break
                print(getattr(Fore, typecolor) + word[i + j], end="", flush=True)
            i += typelength
            # 줄바꿈
            if i >= len(word):
                print(Style.RESET_ALL)
            while True:
                # 아무키
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8')
                    break