from datetime import date
from Purchase.purchase_log import PurchaseLog
from Purchase.purchase_log_dao import PurchaseLogDAO

# 구매 거래 서비스 로직
# 구매 = 잔액 이동 + 상품 삭제 + 거래 로그 저장을 하나의 흐름으로 처리한다.
# 잔액 규칙(차감/가산/음수 방지)은 MemberService에 위임한다.
class PurchaseService:
    log_no_seq = 1   # 거래번호 자동 생성용 시퀀스

    def __init__(self, item_service, log_dao, member_service):
        self.__item_svc = item_service
        self.__log_dao = log_dao
        self.__member_svc = member_service

    # 골동품 구매
    # 성공 시 PurchaseLog 객체 반환, 실패 시 사유 문자열 반환
    def buy_item(self, buyer_id, item_no):
        item = self.__item_svc.get_item(item_no)
        if not item:
            return '상품 없음'
        # 본인 상품 구매 불가
        if item.get_seller_id() == buyer_id:
            return '본인 상품'
        price = item.get_price()
        seller_id = item.get_seller_id()
        # 구매자 잔액 차감 (부족하면 MemberService가 거부 → 음수 방지)
        if not self.__member_svc.withdraw_balance(buyer_id, price):
            return '잔액 부족'
        # 판매자 잔액 가산 (정산). 차감과 항상 함께 이루어진다.
        self.__member_svc.add_balance(seller_id, price)
        # 거래 로그 저장 (상품 정보 복사 → 원본 삭제 후에도 보존)
        log = PurchaseLog(str(PurchaseService.log_no_seq), item_no, item.get_name(),
                          price, seller_id, buyer_id, str(date.today()))
        PurchaseService.log_no_seq += 1
        self.__log_dao.insert_log(log)
        # 거래 완료된 상품은 목록에서 삭제
        self.__item_svc.force_delete_item(item_no)
        return log

    # 구매 내역 조회 (구매자 기준)
    def get_purchases(self, buyer_id):
        return self.__log_dao.select_logs_by_buyer(buyer_id)

    # 판매 내역 조회 (판매자 기준)
    def get_sales(self, seller_id):
        return self.__log_dao.select_logs_by_seller(seller_id)