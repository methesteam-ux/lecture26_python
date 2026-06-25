from Member.member import Member

# 회원 데이터 접근 (CRUD)
class MemberDAO:
    def __init__(self):
        self.__memberDB = {}  # 아이디 : Member 객체

    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
        return True

    def is_exist(self, id):
        return id in self.__memberDB.keys()

    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        return None

    def get_all_members(self):
        member_list = list(self.__memberDB.values())
        if len(member_list):
            return member_list
        return None

    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member
            return True
        return False

    def remove_member(self, id):
        if self.is_exist(id):
            self.__memberDB.pop(id)
            return True
        return False