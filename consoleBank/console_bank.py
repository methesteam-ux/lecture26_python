from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.account_service import AccountService

class ConsoleBank:
    start_menu = ['종료', '로그인', '회원가입']
    banking_menu = ['로그아웃', '계좌목록', '입금', '출금', '계좌생성', '계좌해지', '내 정보']
    member_myinfo_menu = ['돌아가기', '내 정보 보기', '비밀번호 수정', '회원탈퇴']
    admin_menu = ['로그아웃', '회원관리', '계좌관리']
    admin_member_menu = ['돌아가기', '회원목록', '회원정보조회', '회원강퇴']
    admin_account_menu = ['돌아가기', '전체계좌목록', '회원별계좌목록']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()

    # ========== 시작 메뉴 ==========
    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.start_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()
            else:
                print('없는 메뉴입니다.')

    def menu_join(self):
        id = input('>> id : ')
        password = input('>> password : ')
        name = input('>> name : ')
        member = Member(id, password, name)
        if self.msv.join(member):
            print('회원가입이 완료되었습니다.')
        else:
            print('이미 존재하는 id입니다.')

    def menu_login(self):
        id = input('>> id : ')
        password = input('>> password : ')
        if self.msv.login(id, password):
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_banking_menu()
        else:
            print('로그인에 실패하였습니다.')

    def menu_logout(self):
        self.msv.logout()
        print('로그아웃 되었습니다.')

    # ========== 회원 메뉴 ==========
    def run_banking_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.banking_menu)
            if menu == 0:
                self.menu_logout()
                break
            elif menu == 1:
                self.menu_list_my_accounts()
            elif menu == 2:
                self.menu_deposit()
            elif menu == 3:
                self.menu_withdraw()
            elif menu == 4:
                self.menu_create_account()
            elif menu == 5:
                self.menu_delete_account()
            elif menu == 6:
                if self.menu_myinfo():
                    break
            else:
                print('없는 메뉴입니다.')

    def menu_list_my_accounts(self):
        accounts = self.asv.get_members_accounts(self.msv.current_user)
        if not accounts:
            print('보유한 계좌가 없습니다.')
        else:
            for account in accounts:
                print(account)

    def menu_deposit(self):
        account_no = input('>> 계좌번호 : ')
        try:
            amount = int(input('>> 입금액 : '))
        except ValueError:
            print('올바른 금액을 입력해주세요.')
            return
        if self.asv.deposit(account_no, amount):
            print(f'{amount}원이 입금되었습니다.')
        else:
            print('존재하지 않는 계좌입니다.')

    def menu_withdraw(self):
        account_no = input('>> 계좌번호 : ')
        try:
            amount = int(input('>> 출금액 : '))
        except ValueError:
            print('올바른 금액을 입력해주세요.')
            return
        password = input('>> 계좌 비밀번호 : ')
        try:
            self.asv.withdraw(self.msv.current_user, account_no, amount, password)
            print(f'{amount}원이 출금되었습니다.')
        except LookupError:
            print('존재하지 않는 계좌입니다.')
        except KeyError:
            print('계좌 정보가 일치하지 않습니다.')
        except ValueError:
            print('잔액이 부족합니다.')

    def menu_create_account(self):
        password = input('>> 계좌 비밀번호 : ')
        try:
            balance = int(input('>> 초기 입금액 : '))
        except ValueError:
            print('올바른 금액을 입력해주세요.')
            return
        account = Account(0, self.msv.current_user, balance, password)
        if self.asv.create_account(account):
            print('계좌가 생성되었습니다.')
        else:
            print('계좌 생성에 실패하였습니다.')

    def menu_delete_account(self):
        account_no = input('>> 계좌번호 : ')
        password = input('>> 계좌 비밀번호 : ')
        try:
            self.asv.delete_account(self.msv.current_user, account_no, password)
            print('계좌가 해지되었습니다.')
        except LookupError:
            print('존재하지 않는 계좌입니다.')
        except KeyError:
            print('계좌 정보가 일치하지 않습니다.')
        except ValueError:
            print('잔액이 남아있어 해지할 수 없습니다.')

    def menu_myinfo(self):
        return self.run_my_info_menu()

    # ========== 내 정보 메뉴 ==========
    def run_my_info_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.member_myinfo_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_view_myinfo()
            elif menu == 2:
                self.menu_update_password()
            elif menu == 3:
                if self.menu_delete_membership():
                    return True
            else:
                print('없는 메뉴입니다.')

    def menu_view_myinfo(self):
        member = self.msv.view_member_info(self.msv.current_user)
        if member:
            print(member)

    def menu_update_password(self):
        org_password = input('>> 기존 비밀번호 : ')
        new_password = input('>> 새 비밀번호 : ')
        if self.msv.update_member_password(self.msv.current_user, org_password, new_password):
            print('비밀번호가 변경되었습니다.')
        else:
            print('비밀번호 변경에 실패하였습니다.')

    def menu_delete_membership(self):
        confirm = input('정말 탈퇴하시겠습니까? (yes/no) : ')
        if confirm != 'yes':
            return False
        if self.asv.has_remaining_balance(self.msv.current_user):
            print('잔액이 남아있는 계좌가 있어 탈퇴할 수 없습니다.')
            return False
        if self.msv.remove_member(self.msv.current_user):
            print('탈퇴 처리되었습니다.')
            self.msv.logout()
            return True
        else:
            print('탈퇴 처리에 실패하였습니다.')
            return False

    # ========== 관리자 메뉴 ==========
    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_menu)
            if menu == 0:
                self.menu_logout()
                break
            elif menu == 1:
                self.run_admin_member_menu()
            elif menu == 2:
                self.run_admin_account_menu()
            else:
                print('없는 메뉴입니다.')

    def run_admin_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_member_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_members()
            elif menu == 2:
                self.menu_view_member_info()
            elif menu == 3:
                self.menu_delete_member()
            else:
                print('없는 메뉴입니다.')

    def menu_list_members(self):
        members = self.msv.list_members()
        if not members or len(members) <= 1:
            print('가입한 회원이 없습니다.')
        else:
            for member in members[1:]:  # admin 제외
                print(member)

    def menu_view_member_info(self):
        id = input('>> id : ')
        member = self.msv.view_member_info(id)
        if member:
            print(member)
        else:
            print('존재하지 않는 회원입니다.')

    def run_admin_account_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_account_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_all_accounts()
            elif menu == 2:
                self.menu_list_member_accounts()
            else:
                print('없는 메뉴입니다.')

    def menu_list_all_accounts(self):
        accounts = self.asv.get_all_accounts()
        if not accounts:
            print('계좌가 없습니다.')
        else:
            for account in accounts:
                print(account)

    def menu_list_member_accounts(self):
        id = input('>> id : ')
        accounts = self.asv.get_members_accounts(id)
        if not accounts:
            print('보유한 계좌가 없습니다.')
        else:
            for account in accounts:
                print(account)

    def menu_delete_member(self):
        id = input('>> 강퇴할 회원 id : ')
        if self.asv.has_remaining_balance(id):
            print('잔액이 남아있는 계좌가 있어 강퇴할 수 없습니다.')
            return
        if self.msv.remove_member(id):
            print('강퇴 처리되었습니다.')
        else:
            print('강퇴 처리에 실패하였습니다.')

    # ========== 공통 ==========
    def show_welcome(self):
        print('======== Console Bank ==========')

    def say_goodbye(self):
        print('>> Console Bank를 이용해 주셔서 감사합니다.')

    def print_menu(self, menu_list):
        print('-' * 40)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 40)

    def select_menu(self, menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택 : '))
            return menu
        except ValueError:
            return -1

if __name__ == '__main__':
    app = ConsoleBank()
    app.main()