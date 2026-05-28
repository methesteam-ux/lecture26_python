from member import Member, MemberDAO, MemberService

class MemberManager:
    start_menu = ['종료', '로그인', '회원가입']
    admin_menu = ['로그아웃', '회원목록', '회원정보조회', '회원탈퇴']
    member_menu = ['로그아웃', '내정보조회', '내정보수정', '회원탈퇴']
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self):
        self.current_user = None
        self.ms = MemberService(MemberDAO())

    def main(self):
        self.show_welcome()
        self.ms.join(Member(MemberManager.ADMIN_ID, MemberManager.ADMIN_PASSWORD, None))
        while True:
            menu = self.select_menu(MemberManager.start_menu)
            if menu == 0: break
            elif menu == 1: # 로그인
                id = input('>> id : ')
                password = input('>> password : ')
                self.current_user = self.ms.login(id, password)
                if self.current_user:
                    if self.current_user == MemberManager.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.start_member_menu()
                else:
                    print('로그인에 실패하였습니다.')

            elif menu == 2: # 회원가입
                id = input('>> id : ')
                password = input('>> password : ')
                name = input('>> name : ')
                member = Member(id, password, name)
                if self.ms.join(member):
                    print('회원가입이 완료되었습니다.')
                else:
                    print('회원가입에 실패하였습니다.')
            else:
                print('없는 메뉴입니다.')
        self.say_goodbye()

    def start_admin_menu(self):
        print('---------- 관리자 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.admin_menu)
            if menu == 0: break
            elif menu == 1: # 회원목록
                self.list_all_member()
            elif menu == 2: # 회원정보조회
                id = input('>> 조회할 id : ')
                member = self.ms.get_member(id)
                if member:
                    print(f'번호\tid\t이름\t비밀번호')
                    print(member)
                else:
                    print('존재하지 않는 회원입니다.')
            elif menu == 3: # 회원강퇴
                id = input('>> 강퇴할 id : ')
                if id == MemberManager.ADMIN_ID:
                    print('관리자는 강퇴할 수 없습니다.')
                elif self.ms.delete_member(id):
                    print(f'{id} 회원을 강퇴하였습니다.')
                else:
                    print('존재하지 않는 회원입니다.')
            else:
                print('없는 메뉴입니다.')

    def list_all_member(self):
        print(self.current_user)
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        
        member_list = self.ms.list_members()
        if len(member_list) <= 1:
            print('가입한 회원이 없습니다.')
        else:
            for member in member_list[1:]:
                print(member)

    def start_member_menu(self):
        print('---------- 회원 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.member_menu)
            if menu == 0: break
            elif menu == 1: # 내정보조회
                member = self.ms.get_member(self.current_user)
                print(f'번호\tid\t이름\t비밀번호')
                print(member)
            elif menu == 2: # 내정보수정 (비밀번호 변경)
                old_pw = input('>> 현재 비밀번호 : ')
                member = self.ms.get_member(self.current_user)
                if old_pw != member.get_password():
                    print('현재 비밀번호가 일치하지 않습니다.')
                else:
                    new_pw = input('>> 새 비밀번호 : ')
                    new_pw2 = input('>> 새 비밀번호 확인 : ')
                    if new_pw != new_pw2:
                        print('새 비밀번호가 일치하지 않습니다.')
                    else:
                        self.ms.update_password(self.current_user, new_pw)
                        print('비밀번호가 변경되었습니다.')
            elif menu == 3: # 회원탈퇴
                confirm = input('정말 탈퇴하시겠습니까? (yes/no) : ')
                if confirm == 'yes':
                    self.ms.delete_member(self.current_user)
                    self.current_user = None
                    print('탈퇴가 완료되었습니다.')
                    break
            else:
                print('없는 메뉴입니다.')

    def show_welcome(self):
        print('=' * 50)
        title = 'Member Manager'
        print(f'{title:^50}')
        print('=' * 50)

    def say_goodbye(self):
        print('안녕히 가세요')

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
    app = MemberManager()
    app.main()