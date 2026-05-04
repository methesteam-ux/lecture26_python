import random

cap = 7
limit = 100
answer = random.randint(1, limit)
win = False

def tryguess(n):
    if answer > n:
        return 1
    elif answer < n:
        return -1
    else:
        return 0
    
print("======숫자 맞추기 게임=====")

for i in range(cap):
    trynumber = int(input("숫자를 입력하세요 : "))

    if tryguess(trynumber) == 1:
        print("Up")
    elif tryguess(trynumber) == -1:
        print("Down")
    elif tryguess(trynumber) == 0:
        print(f"{i+1}턴 만에 정답을 맞췄습니다!")
        win = True
        break

if win == False:
    print("Game Over")