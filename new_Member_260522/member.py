#======================
# 데이터 모델 정의 : Member
class Member:
    def __init__(self, id, password, name):
        self.__member_no = 0
        self.__id = id
        self.__password = password
        self.__name = name

    def get_member_no(self):
        return self.__member_no
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def set_password(self, password):
        self.__password = password
    
    def __str__(self):
        return f'{self.__member_no}\t{self.__id}\t{self.__name}\t{self.__password}'   

#==================
# 회원 관리 서비스 로직 (Controller) : MemberService
class MemberService:
    def __init__(self, memberDao):
        self.__dao = memberDao

    def join(self, member):
        # 이미 있는 아이디인지 확인
        if self.__dao.is_exist(member.get_id()):
            return False
        self.__dao.insert_member(member)
        return True

    def login(self, id, password):
        member = self.__dao.get_member_info(id)
        if member:
            if password == member.get_password():
                return id
        return None
    
    def delete_member(self, id):
        return self.__dao.delete_member(id)

    def update_password(self, id, new_password):
        return self.__dao.update_password(id, new_password)

    def get_member(self, id):
        return self.__dao.get_member_info(id)

    def list_members(self):
        member_list = self.__dao.get_all_members()
        return member_list

#====================
# 회원 데이터 접근 (CRUD) : MemberDAO
class MemberDAO:
    def __init__(self):
        self.__memberDB = {}
        self.__next_no = 1
    
    def insert_member(self, member):
        member._Member__member_no = self.__next_no
        self.__next_no += 1
        self.__memberDB[member.get_id()] = member

    def delete_member(self, id):
        if self.is_exist(id):
            del self.__memberDB[id]
            return True
        return False

    def update_password(self, id, new_password):
        if self.is_exist(id):
            self.__memberDB[id].set_password(new_password)
            return True
        return False

    def is_exist(self, id):
        if id in self.__memberDB.keys() : return True
        return False
    
    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        else:
            return None
        
    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
    