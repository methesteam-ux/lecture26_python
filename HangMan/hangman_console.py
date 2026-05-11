from hangman import Hangman

word_list = ["apple", "banana", "man", "woman", "tomato"]

print()
print("========== Hangman ==========")

hangman = Hangman(word_list)
print(f"{hangman.display_word} {len(hangman.word)}글자")

while True:
    # 알파벳 입력
    letter = input(">> 알파벳 입력 : ")

    # 정답 확인
    result = hangman.check_letter(letter)
    if result == Hangman.RIGHT:
        print(f"정답 : {hangman.display_word}")
    elif result == Hangman.WRONG:
        print(f"오답 : {hangman.num_try}회 시도")

    # 승패 확인
    result = hangman.is_win()
    if result == Hangman.WIN:
        print(f"You win! : {hangman.num_try}회 틀림")
        break
    elif result == Hangman.LOSE:
        print(f"You lose! : {hangman.word}")
        break