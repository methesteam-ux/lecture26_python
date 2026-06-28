from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Item.item_dao import ItemDAO
from Item.item_service import ItemService
from Purchase.purchase_log_dao import PurchaseLogDAO
from Purchase.purchase_service import PurchaseService


class ConsoleStore:
    # 0번 항목(종료/로그아웃/돌아가기)을 리스트 맨 앞에 두고, 1번부터 메뉴를 나열한다.
    start_menu = ['종료', '로그인', '회원가입']
    member_menu = ['로그아웃', '골동품 거래', '내 거래 내역', '내 정보']
    trade_menu = ['돌아가기', '상품 목록 조회', '상품 상세 조회', '상품 검색',
                  '상품 등록', '상품 구매']
    myhist_menu = ['돌아가기', '내 판매 목록 조회', '내 상품 정보 수정', '내 상품 등록 취소',
                   '구매 내역 조회', '판매 내역 조회']
    myinfo_menu = ['돌아가기', '비밀번호 변경', '예치금 입금', '주소 변경', '회원 탈퇴']
    admin_menu = ['로그아웃', '상품 관리', '회원 관리']
    item_mng_menu = ['돌아가기', '상품 목록 조회', '상품 상세 조회', '상품 등록 취소']
    member_mng_menu = ['돌아가기', '회원 목록 조회', '회원 정보 조회', '회원 강제 퇴장']

    def __init__(self):
        self.ms = MemberService(MemberDAO())
        self.is_ = ItemService(ItemDAO())
        self.ps = PurchaseService(self.is_, PurchaseLogDAO(), self.ms)

    # ===== 공통 유틸 =====
    def show_welcome(self):
        print('======== 골동품 거래 사이트에 오신 것을 환영합니다 ========')

    def say_goodbye(self):
        print('>> 프로그램을 종료합니다. 이용해 주셔서 감사합니다.')

    # 메뉴 출력 후 번호를 입력받아 정수로 반환 (잘못된 입력이면 -1)
    def select_menu(self, menu_list):
        print('-' * 50)
        for index in range(1, len(menu_list)):
            print(f"{index}. {menu_list[index]}", end="   ")
        print(f"0. {menu_list[0]}")
        print('-' * 50)
        try:
            num = int(input(">> 메뉴 : "))
        except ValueError:
            return -1
        else:
            return num

    def input_int(self, prompt):
        try:
            return int(input(prompt))
        except ValueError:
            print("숫자로 입력해주세요.")
            return None

    # ===== 시작 메뉴 =====
    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()

    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleStore.start_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()
            else:
                print("잘못된 선택입니다.")

    def menu_join(self):
        print('>>>> 회원가입 <<<<')
        id = input('아이디 > ').strip()
        if self.ms.is_exist(id):
            print('  이미 존재하는 아이디입니다.')
            return
        password = input('비밀번호 > ').strip()
        name = input('이름 > ').strip()
        balance = self.input_int('초기 예치금 > ')
        if balance is None:
            return
        address = input('집 주소 > ').strip()
        if self.ms.join(Member(id, password, name, balance, address)):
            print(f'  {name}님, 회원가입이 완료되었습니다.')
        else:
            print('  회원가입에 실패했습니다.')

    def menu_login(self):
        print('>>>> 로그인 <<<<')
        id = input('아이디 > ').strip()
        password = input('비밀번호 > ').strip()
        if not self.ms.login(id, password):
            print('  아이디 또는 비밀번호가 올바르지 않습니다.')
            return
        print(f'  {id}님, 로그인되었습니다.')
        if self.ms.is_admin(id):
            self.run_admin_menu()
        else:
            self.run_member_menu()

    # ===== 회원 메뉴 =====
    def run_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleStore.member_menu)
            if menu == 0:
                self.menu_logout()
                break
            elif menu == 1:
                self.run_trade_menu()
            elif menu == 2:
                self.run_myhist_menu()
            elif menu == 3:
                self.run_myinfo_menu()
            else:
                print("잘못된 선택입니다.")

    def menu_logout(self):
        self.ms.logout()
        print('  로그아웃되었습니다.')

    # --- 골동품 거래 메뉴 ---
    def run_trade_menu(self):
        print('>>>> 골동품 거래 메뉴 <<<<')
        while True:
            menu = self.select_menu(ConsoleStore.trade_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_item_list()
            elif menu == 2:
                self.menu_item_detail()
            elif menu == 3:
                self.menu_item_search()
            elif menu == 4:
                self.menu_item_register()
            elif menu == 5:
                self.menu_item_buy()
            else:
                print("잘못된 선택입니다.")

    def menu_item_list(self):
        print('>>>> 골동품 목록 <<<<')
        items = self.is_.get_all_items()
        if not items:
            print('  등록된 상품이 없습니다.'); return
        for item in items:
            print(' ', item)

    def menu_item_detail(self):
        item_no = input('상품번호 > ').strip()
        item = self.is_.get_item(item_no)
        if not item:
            print('  해당 상품이 없습니다.'); return
        print(f'  [{item.get_item_no()}] {item.get_name()}')
        print(f'  설명: {item.get_description()}')
        print(f'  가격: {item.get_price()}원 / 판매자: {item.get_seller_id()}')

    def menu_item_search(self):
        keyword = input('검색어 > ').strip()
        items = self.is_.search_items(keyword)
        if not items:
            print('  검색 결과가 없습니다.'); return
        for item in items:
            print(' ', item)

    def menu_item_register(self):
        print('>>>> 골동품 등록 <<<<')
        name = input('상품 이름 > ').strip()
        description = input('상품 설명 > ').strip()
        price = self.input_int('가격 > ')
        if price is None:
            return
        if price <= 0:
            print('  가격은 1원 이상이어야 합니다.'); return
        item = self.is_.register_item(name, description, price, self.ms.current_user)
        if item:
            print(f'  상품이 등록되었습니다. (상품번호 {item.get_item_no()})')
        else:
            print('  상품 등록에 실패했습니다.')

    def menu_item_buy(self):
        # 구매 가능한 상품(본인 등록 상품 제외) 목록을 먼저 보여준다
        items = self.is_.get_all_items()
        buyable = [it for it in items if it.get_seller_id() != self.ms.current_user] if items else []
        if not buyable:
            print('  구매 가능한 상품이 없습니다.'); return
        print('>>>> 구매 가능한 골동품 목록 <<<<')
        for item in buyable:
            print(' ', item)
        item_no = input('구매할 상품번호 > ').strip()
        result = self.ps.buy_item(self.ms.current_user, item_no)
        if isinstance(result, str):
            reason = {'상품 없음': '해당 상품이 없습니다.',
                      '본인 상품': '본인이 등록한 상품은 구매할 수 없습니다.',
                      '잔액 부족': '잔액이 부족합니다.'}.get(result, result)
            print(f'  구매 실패: {reason}')
        else:
            print(f'  구매 완료! {result.get_item_name()} ({result.get_price()}원)')
            print(f'  현재 잔액: {self.ms.get_balance(self.ms.current_user)}원')

    # --- 내 거래 내역 메뉴 ---
    def run_myhist_menu(self):
        print('>>>> 내 거래 내역 메뉴 <<<<')
        while True:
            menu = self.select_menu(ConsoleStore.myhist_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_my_sales_list()
            elif menu == 2:
                self.menu_item_update()
            elif menu == 3:
                self.menu_item_cancel()
            elif menu == 4:
                self.menu_purchase_history()
            elif menu == 5:
                self.menu_sales_history()
            else:
                print("잘못된 선택입니다.")

    def menu_my_sales_list(self):
        print('>>>> 내 판매 목록 (판매 중) <<<<')
        items = self.is_.get_my_items(self.ms.current_user)
        if not items:
            print('  등록한 상품이 없습니다.'); return
        for item in items:
            print(' ', item)

    def menu_item_update(self):
        item_no = input('수정할 상품번호 > ').strip()
        name = input('새 이름 > ').strip()
        description = input('새 설명 > ').strip()
        price = self.input_int('새 가격 > ')
        if price is None:
            return
        if price <= 0:
            print('  가격은 1원 이상이어야 합니다.'); return
        if self.is_.update_item(item_no, self.ms.current_user, name, description, price):
            print('  수정되었습니다.')
        else:
            print('  수정 실패: 본인 상품이 아니거나 존재하지 않습니다.')

    def menu_item_cancel(self):
        item_no = input('취소할 상품번호 > ').strip()
        if self.is_.delete_my_item(item_no, self.ms.current_user):
            print('  등록이 취소되었습니다.')
        else:
            print('  취소 실패: 본인 상품이 아니거나 존재하지 않습니다.')

    def menu_purchase_history(self):
        print('>>>> 구매 내역 <<<<')
        logs = self.ps.get_purchases(self.ms.current_user)
        if not logs:
            print('  구매 내역이 없습니다.'); return
        for log in logs:
            print(' ', log)

    def menu_sales_history(self):
        print('>>>> 판매 내역 <<<<')
        logs = self.ps.get_sales(self.ms.current_user)
        if not logs:
            print('  판매 내역이 없습니다.'); return
        for log in logs:
            print(' ', log)

    # --- 내 정보 메뉴 ---
    def run_myinfo_menu(self):
        print('>>>> 내 정보 메뉴 <<<<')
        while True:
            menu = self.select_menu(ConsoleStore.myinfo_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_update_password()
            elif menu == 2:
                self.menu_deposit()
            elif menu == 3:
                self.menu_update_address()
            elif menu == 4:
                if self.menu_withdraw_member():  # 탈퇴 시 상위로
                    return
            else:
                print("잘못된 선택입니다.")

    def menu_update_password(self):
        print('>>>> 비밀번호 변경 <<<<')
        org = input('기존 비밀번호 > ').strip()
        new = input('새 비밀번호 > ').strip()
        if self.ms.update_password(self.ms.current_user, org, new):
            print('  비밀번호가 변경되었습니다.')
        else:
            print('  변경 실패: 기존 비밀번호가 일치하지 않습니다.')

    def menu_deposit(self):
        amount = self.input_int('입금액 > ')
        if amount is None:
            return
        if self.ms.deposit(self.ms.current_user, amount):
            print(f'  입금 완료. 현재 잔액: {self.ms.get_balance(self.ms.current_user)}원')
        else:
            print('  입금 실패: 금액을 확인하세요.')

    def menu_update_address(self):
        address = input('새 주소 > ').strip()
        if self.ms.update_address(self.ms.current_user, address):
            print('  주소가 변경되었습니다.')
        else:
            print('  변경에 실패했습니다.')

    # 반환 True면 탈퇴 완료 → 로그인 해제 후 시작 메뉴로
    def menu_withdraw_member(self):
        print('>>>> 회원 탈퇴 <<<<')
        uid = self.ms.current_user
        balance = self.ms.get_balance(uid)
        if balance and balance > 0:
            print(f'  [경고] 잔액 {balance}원이 남아 있습니다. 탈퇴 시 소멸됩니다.')
            confirm = input('  정말 탈퇴하시겠습니까? (y/n) > ').strip().lower()
            if confirm != 'y':
                print('  탈퇴를 취소했습니다.')
                return False
        if self.ms.withdraw_member(uid, uid):
            print('  탈퇴가 완료되었습니다.')
            self.ms.logout()
            return True
        print('  탈퇴에 실패했습니다.')
        return False

    # ===== 관리자 메뉴 =====
    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleStore.admin_menu)
            if menu == 0:
                self.menu_logout()
                break
            elif menu == 1:
                self.menu_manage_items()
            elif menu == 2:
                self.menu_manage_members()
            else:
                print("잘못된 선택입니다.")

    # 관리자 메뉴 → 품목 관리 진입
    def menu_manage_items(self):
        self.run_item_mng_menu()

    # 관리자 메뉴 → 회원 관리 진입
    def menu_manage_members(self):
        self.run_member_mng_menu()

    # --- 품목 관리 ---
    def run_item_mng_menu(self):
        print('>>>> 품목 관리 메뉴 <<<<')
        while True:
            menu = self.select_menu(ConsoleStore.item_mng_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_admin_item_list()
            elif menu == 2:
                self.menu_admin_item_detail()
            elif menu == 3:
                self.menu_admin_item_delete()
            else:
                print("잘못된 선택입니다.")

    def menu_admin_item_list(self):
        self.menu_item_list()

    def menu_admin_item_detail(self):
        self.menu_item_detail()

    def menu_admin_item_delete(self):
        print('>>>> 상품 등록 취소 <<<<')
        item_no = input('삭제할 상품번호 > ').strip()
        if self.is_.force_delete_item(item_no):
            print('  상품이 삭제되었습니다.')
        else:
            print('  삭제 실패: 해당 상품이 없습니다.')

    # --- 회원 관리 ---
    def run_member_mng_menu(self):
        print('>>>> 회원 관리 메뉴 <<<<')
        while True:
            menu = self.select_menu(ConsoleStore.member_mng_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_admin_member_list()
            elif menu == 2:
                self.menu_admin_member_detail()
            elif menu == 3:
                self.menu_admin_member_kick()
            else:
                print("잘못된 선택입니다.")

    def menu_admin_member_list(self):
        print('>>>> 회원 목록 <<<<')
        members = self.ms.list_members()
        if not members:
            print('  회원이 없습니다.'); return
        for m in members:
            print(' ', m)

    def menu_admin_member_detail(self):
        id = input('회원 아이디 > ').strip()
        m = self.ms.view_member(id)
        if not m:
            print('  해당 회원이 없습니다.'); return
        print(' ', m)

    def menu_admin_member_kick(self):
        print('>>>> 회원 강제 퇴장 <<<<')
        id = input('강제 퇴장시킬 회원 아이디 > ').strip()
        m = self.ms.view_member(id)
        if not m:
            print('  해당 회원이 없습니다.'); return
        if m.get_balance() > 0:
            print(f'  [경고] 잔액 {m.get_balance()}원이 남아 있습니다. 삭제 시 소멸됩니다.')
            confirm = input('  강제 퇴장하시겠습니까? (y/n) > ').strip().lower()
            if confirm != 'y':
                print('  취소했습니다.'); return
        if self.ms.force_remove_member(id):
            print('  강제 퇴장되었습니다.')
        else:
            print('  실패: 관리자 계정은 삭제할 수 없습니다.')


if __name__ == '__main__':
    app = ConsoleStore()
    app.main()
