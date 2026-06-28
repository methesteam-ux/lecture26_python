from Member.member_dao import MemberDAO
from Member.member import Member

# 회원 관리 서비스 로직
class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '123'
    member_no_seq = 1   # 회원번호 자동 생성용 시퀀스

    def __init__(self, member_dao):
        self.__dao = member_dao
        self.current_user = None
        # 관리자 계정을 미리 등록 (별도 회원가입 불필요)
        self.join(Member(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD, '관리자'))

    # 회원가입
    def join(self, member):
        if self.__dao.is_exist(member.get_id()):
            return False
        member.set_member_no(MemberService.member_no_seq)
        MemberService.member_no_seq += 1
        self.__dao.insert_member(member)
        return True

    # 로그인
    def login(self, id, password):
        member = self.__dao.get_member_info(id)
        if member and member.get_password() == password:
            self.current_user = id
            return True
        return False

    def logout(self):
        self.current_user = None

    def is_exist(self, id):
        return self.__dao.is_exist(id)

    def is_admin(self, id):
        return id == MemberService.ADMIN_ID

    # 비밀번호 변경 (본인만)
    def update_password(self, id, org_password, new_password):
        if self.current_user != id:
            return False
        member = self.__dao.get_member_info(id)
        if not member:
            return False
        if member.get_password() != org_password:
            return False
        member.set_password(new_password)
        return self.__dao.update_member_info(id, member)

    # 예치금 입금
    def deposit(self, id, amount):
        if amount <= 0:
            return False
        member = self.__dao.get_member_info(id)
        if not member:
            return False
        member.set_balance(member.get_balance() + amount)
        return self.__dao.update_member_info(id, member)

    # 주소 변경 (본인만)
    def update_address(self, id, address):
        if self.current_user != id:
            return False
        member = self.__dao.get_member_info(id)
        if not member:
            return False
        member.set_address(address)
        return self.__dao.update_member_info(id, member)

    # --- 잔액 이동: 구매 거래 시 PurchaseService가 호출 (잔액 규칙을 이곳에 집중) ---
    # 출금: 잔액이 부족하면 실패 (음수 방지)
    def withdraw_balance(self, id, amount):
        member = self.__dao.get_member_info(id)
        if not member or amount <= 0:
            return False
        if member.get_balance() < amount:
            return False
        member.set_balance(member.get_balance() - amount)
        return self.__dao.update_member_info(id, member)

    # 입금(가산): 판매 대금 정산용
    def add_balance(self, id, amount):
        member = self.__dao.get_member_info(id)
        if not member or amount <= 0:
            return False
        member.set_balance(member.get_balance() + amount)
        return self.__dao.update_member_info(id, member)

    def get_balance(self, id):
        member = self.__dao.get_member_info(id)
        if member:
            return member.get_balance()
        return None

    # 회원 탈퇴 (본인)
    def withdraw_member(self, id, requester_id):
        if requester_id != id:
            return False
        return self.__dao.remove_member(id)

    # 회원 강제 퇴장 (관리자)
    def force_remove_member(self, id):
        if self.is_admin(id):   # 관리자 계정 자신은 삭제 불가
            return False
        return self.__dao.remove_member(id)

    def list_members(self):
        return self.__dao.get_all_members()

    def view_member(self, id):
        return self.__dao.get_member_info(id)