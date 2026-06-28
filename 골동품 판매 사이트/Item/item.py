# Item 데이터 모델 (골동품 상품)
class Item:
    def __init__(self, item_no, name, description, price, seller_id):
        self.__item_no = item_no            # 상품번호 (등록 시 자동 부여)
        self.__name = name                  # 상품 이름
        self.__description = description     # 상품 설명
        self.__price = price                # 가격
        self.__seller_id = seller_id        # 판매자(등록한 회원) 아이디

    def get_item_no(self):
        return self.__item_no
    def get_name(self):
        return self.__name
    def get_description(self):
        return self.__description
    def get_price(self):
        return self.__price
    def get_seller_id(self):
        return self.__seller_id

    def set_item_no(self, item_no):
        self.__item_no = item_no
    def set_name(self, name):
        self.__name = name
    def set_description(self, description):
        self.__description = description
    def set_price(self, price):
        self.__price = price
    def set_seller_id(self, seller_id):
        self.__seller_id = seller_id

    def __str__(self):
        return (f'[{self.__item_no}] {self.__name} / {self.__price}원 / '
                f'판매자 {self.__seller_id}')