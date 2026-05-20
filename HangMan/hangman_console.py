from hangman import Hangman
#import os
#print(os.getcwd())

with open("./HangMan/voca.txt", encoding="utf-8") as f_read:
    lines = f_read.readlines()

#print(lines)

new_lines = []
for line in lines:
    new_line = ''.join(c for c in line if c.isalpha() and c.isascii())
    new_lines.append(new_line)

word_list = new_lines
#print(new_lines)

def start_hangman(Hangman):
    print()
    print("========== Hangman ==========")

    hangman = Hangman(word_list)
    print(f"{hangman.display_word} {len(hangman.word)}글자")

    while True:
        # 알파벳 입력
        letter = input(">> 알파벳 입력 : ")
        if not letter.isalpha():
            print("알파벳을 입력하세요.")
            continue

        # 정답 확인
        result = hangman.check_letter(letter)
        if result == Hangman.RIGHT:
            print(f"정답 : {hangman.display_word}")
        elif result == Hangman.WRONG:
            print(f"오답 : {hangman.num_try}회 시도")
        else:
            print(hangman.error_status)

        # 승패 확인
        result = hangman.is_win()
        if result == Hangman.WIN:
            print(f"You win! : {hangman.num_try}회 틀림")
            break
        elif result == Hangman.LOSE:
            print(f"You lose! : {hangman.word}")
            break

if __name__ == "__main__":
    hs = Hangman
    start_hangman(hs)