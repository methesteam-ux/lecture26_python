import random

error_limit = 7
num_error = 0

word_list = ["apple", "banana", "man", "woman", "tomato"]
target_word = word_list[random.randint(0, len(word_list)-1)]
blank_char = "_"
word_screen = blank_char * len(target_word)
used_char = []

while num_error < error_limit:
    user_input = input(">> 알파벳 입력 : ").lower()

    if user_input in used_char:
        print("이미 제출한 알파벳을 제출했습니다.")
        continue
    
    if target_word.find(user_input) == -1:
        num_error += 1
        print(f"오답 : {num_error}회")
    else:
        for i in range(len(target_word)):
            if target_word[i] == user_input:
                word_screen = word_screen[:i] + user_input + word_screen[i+1:]
        print("정답 :", word_screen)

    if word_screen.count(blank_char) == 0:
        print("You win")
        break

    used_char.append(user_input)

if num_error >= error_limit:
    print("Game Over, 정답 :", target_word)