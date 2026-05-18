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