# Member 데이터 모델 (회원)
class Member:
    def __init__(self, id, password, name, balance=0, address=''):
        self.__member_no = 0        # 회원번호 (가입 시 자동 부여)
        self.__id = id              # 아이디
        self.__password = password  # 비밀번호
        self.__name = name          # 이름
        self.__balance = balance    # 예치금 잔액
        self.__address = address    # 집 주소

    def get_member_no(self):
        return self.__member_no
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance
    def get_address(self):
        return self.__address

    def set_member_no(self, member_no):
        self.__member_no = member_no
    def set_id(self, id):
        self.__id = id
    def set_password(self, password):
        self.__password = password
    def set_name(self, name):
        self.__name = name
    def set_balance(self, balance):
        self.__balance = balance
    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return (f'[회원 {self.__member_no}] {self.__id} / {self.__name} / '
                f'잔액 {self.__balance}원 / 주소 {self.__address}')