class Member:
    def __init__(self, member_num:int, id:str, pw:str, name:str, phone_num:int, address:str):
        self.__member_num = member_num
        self.__id = id
        self.__pw = pw
        self.__name = name
        self.__phone_num = phone_num
        self.__address = address

    def __str__(self):
        return "회원번호: " + str(self.__member_num) + " | 아이디: " + self.__id + " | 비밀번호: " + self.__pw + " | 이름: " + self.__name + " | 전화번호: " + str(self.__phone_num) + " | 주소: " + self.__address

    def get_member_num(self):
        return self.__member_num
    
    def get_id(self):
        return self.__id
    
    def get_pw(self):
        return self.__pw
    
    def get_name(self):
        return self.__name
    
    def get_phone_num(self):
        return self.__phone_num
    
    def get_address(self):
        return self.__address
    
class MemeberService:
    def __init__(self):
        self.__member_list = []

    def register(self, member_num, id, pw, name, phone_num, address):
        newMember = Member(member_num, id, pw, name, phone_num, address)
        self.__member_list.append(newMember)
        return True

    def list_memeber(self):
        return self.__member_list
    
    def member_info(self, member_num:int):
        for member in self.__member_list:
            if member.get_member_num() == member_num:
                return member
        return False

    def modify_member_info(self, member_num:int, new_member_num, new_id, new_pw, new_name, new_phone_num, new_address):
        for member in self.__member_list:
            if member.get_member_num() == member_num:
                i = self.__member_list.index(member)
                self.__member_list[i] = Member(new_member_num, new_id, new_pw, new_name, new_phone_num, new_address)
                return True
        return False

    def unregister(self, member_num:int):
        for member in self.__member_list:
            if member.get_member_num() == member_num:
                try:
                    self.__member_list.remove(member)
                    return True
                except:
                    return False
        return False

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

ms = MemeberService()

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