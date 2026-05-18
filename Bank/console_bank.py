from account.account import AccountService

def get_input_int(text:str):
    while True:
        try:
            return int(input(text))
        except:
            print("숫자만 입력 가능합니다. 다시 입력해주세요.")

def get_input_int_list(text:str, arr:list):
    try:
        temp = int(input(text))
        if not temp in arr:
            temp = False
    except:
        temp = False
    return temp

# 메뉴와 사용자 interaction에 따른 서비스 호출
def select_menu():
    print("=======================================================")
    print(" 1. 계좌생성 | 2. 계좌목록 | 3. 입금 | 4. 출금 | 0. 종료")
    print("=======================================================")
    menu = get_input_int_list(">> 메뉴 선택 : ", list(range(5)))
    return menu

aservice = AccountService()

print()
print("========== Bank ==========")

while True:
    menu = select_menu()
    if menu == 0: # 종료
        break
    elif menu == 1: # 계좌 생성
        # 계좌번호, 계좌주, 잔액 입력을 받아서 계좌 생성
        account_no = input(">> 계좌번호 : ")
        owner = input(">> 계좌주 : ")
        balance = get_input_int(">> 초기 입금액 : ")
        if aservice.create_account(account_no, owner, balance):
            print("결과 : 계좌가 생성되었습니다.")
    elif menu == 2: # 계좌 목록
        account_list = aservice.list_account()
        print("----------")
        print(" 계좌 목록 ")
        print("----------")
        for account in account_list:
            print(account)
    elif menu == 3: # 입금
        print("----------")
        print("   예금   ")
        print("----------")
        account_no = input(">> 계좌번호 : ")
        amount = get_input_int(">> 예금액 : ")
        aservice.deposit(account_no, amount) 
    elif menu == 4: # 출금
        print("----------")
        print("   출금   ")
        print("----------")
        account_no = input(">> 계좌번호 : ")
        amount = get_input_int(">> 출금액 : ")
        aservice.withdraw(account_no, amount)

print("========== 이용해 주셔서 감사합니다. ==========")