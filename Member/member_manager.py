from member.member import MemberService

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

def select_menu():
    print("==================================================================================")
    print(" 1. 회원가입 | 2. 회원목록 | 3. 회원상세정보 | 4. 회원정보수정 | 5. 회원탈퇴 | 0. 종료")
    print("==================================================================================")

    menu = get_input_int_list(">> 메뉴 선택 : ", list(range(6)))
    return menu

ms = MemberService()

print()
print("========== 회원가입 ==========")

while True:
    menu = select_menu()
    if menu == False:
        print("올바른 메뉴 번호를 입력해주세요.")
        continue
    elif menu == 0:
        break
    elif menu == 1:
        member_num, id, pw, name, phone_num, address = get_input_int(">> 회원번호 : "), input(">> 아이디 : "), input(">> 비밀번호 : "), input(">> 이름 : "), get_input_int(">> 전화번호 : "), input(">> 주소 : ")
        if ms.register(member_num, id, pw, name, phone_num, address):
            print("결과 : 회원 가입을 성공했습니다.")
    elif menu == 2:
        member_list = ms.list_memeber()
        print("----------")
        print(" 회원 목록 ")
        print("----------")
        for member in member_list:
            print(member)
    elif menu == 3:
        print("-----------")
        print("회원상세정보")
        print("-----------")
        
        member_num = get_input_int(">> 조회할 회원번호 : ")
        info = ms.member_info(member_num)

        if info != False:
            print(info)
        else:
            print("무언가 잘못되었습니다.")
    elif menu == 4:
        print("-----------")
        print("회원정보수정")
        print("-----------")
        
        member_num = get_input_int(">> 수정할 회원번호 : ")
        new_member_num, new_id, new_pw, new_name, new_phone_num, new_address = get_input_int(">> 회원번호 : "), input(">> 아이디 : "), input(">> 비밀번호 : "), input(">> 이름 : "), get_input_int(">> 전화번호 : "), input(">> 주소 : ")
        
        if ms.modify_member_info(member_num, new_member_num, new_id, new_pw, new_name, new_phone_num, new_address) != False:
            print("회원정보가 수정되었습니다.")
        else:
            print("무언가 잘못되었습니다.")

    elif menu == 5:
        print("----------")
        print(" 회원 탈퇴 ")
        print("----------")

        member_num = get_input_int(">> 탈퇴할 회원번호 : ")
        if ms.unregister(member_num) != False:
            print("탈퇴 처리되었습니다.")
        else:
            print("무언가 잘못되었습니다.")

print("========== 이용해 주셔서 감사합니다. ==========")