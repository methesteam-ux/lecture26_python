# PurchaseLog 데이터 모델 (거래 내역 / 판매 로그)
# 구매가 성사되면 상품 정보를 복사해 보관한다.
# 원본 Item이 목록에서 삭제되어도 거래 내역은 보존된다.
class PurchaseLog:
    def __init__(self, log_no, item_no, item_name, price,
                 seller_id, buyer_id, trade_date):
        self.__log_no = log_no          # 거래번호 (자동 생성)
        self.__item_no = item_no        # 거래된 상품번호
        self.__item_name = item_name    # 상품 이름 (조회 편의용 복사본)
        self.__price = price            # 거래 가격
        self.__seller_id = seller_id    # 판매자 아이디
        self.__buyer_id = buyer_id      # 구매자 아이디
        self.__trade_date = trade_date  # 거래일

    def get_log_no(self):
        return self.__log_no
    def get_item_no(self):
        return self.__item_no
    def get_item_name(self):
        return self.__item_name
    def get_price(self):
        return self.__price
    def get_seller_id(self):
        return self.__seller_id
    def get_buyer_id(self):
        return self.__buyer_id
    def get_trade_date(self):
        return self.__trade_date

    def __str__(self):
        return (f'[거래 {self.__log_no}] {self.__item_name}(상품 {self.__item_no}) / '
                f'{self.__price}원 / 판매자 {self.__seller_id} / '
                f'구매자 {self.__buyer_id} / 거래일 {self.__trade_date}')