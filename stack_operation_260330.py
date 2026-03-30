stack = []
capacity = 5

def isFull():
    if len(stack) >= capacity:
        return True
    else:
        return False
    
def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

def push(data):
    if not isFull():
        stack.append(data)
    else:
        print("stack이 차 있어서 더 이상 추가할 수 없습니다.")

def pop():
    if not isEmpty():
        print(f"> 가져온 데이터 : {stack.pop()}")
    else:
        print("stack이 비어 있습니다.")

def peek():
    if not isEmpty():
        print(f"> 가져올 데이터 : {stack[len(stack)-1]}")
    else:
        print("stack이 비어 있습니다.")

#=======================================================================================

print(f"[[ 정수형 스택 연산 실습 (용량 : {capacity}) ]]")
while True:
    print("==================================")
    print("  1.Push  2.Pop  3.Peek  0.Exit")
    print("==================================")
    menu = int(input("> 메뉴 선택 : "))
    if menu == 0:
        break
    elif menu == 1:
        data = int(input("> 데이터 입력 : "))
        push(data)
    elif menu == 2:
        data = pop()
    elif menu == 3:
        data = peek()

    print("> 현재 스택 상태", stack)

print("[[ 정수형 스택 연산 실습 종료 ]]")