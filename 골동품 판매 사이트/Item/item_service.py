from Item.item import Item
from Item.item_dao import ItemDAO

# 골동품 상품 관리 서비스 로직
class ItemService:
    item_no_seq = 1001   # 상품번호 자동 생성용 시퀀스

    def __init__(self, item_dao):
        self.__dao = item_dao

    # 골동품 등록 (상품번호 자동 부여)
    def register_item(self, name, description, price, seller_id):
        item = Item(str(ItemService.item_no_seq), name, description, price, seller_id)
        ItemService.item_no_seq += 1
        if self.__dao.insert_item(item):
            return item
        return None

    def get_all_items(self):
        return self.__dao.select_all_items()

    def get_item(self, item_no):
        return self.__dao.select_item_by_no(item_no)

    # 이름 검색
    def search_items(self, keyword):
        return self.__dao.search_items_by_name(keyword)

    # 내 판매 목록 (현재 등록되어 있는 내 상품)
    def get_my_items(self, seller_id):
        return self.__dao.select_items_by_seller(seller_id)

    # 내 상품 정보 수정 (판매자 본인만)
    def update_item(self, item_no, requester_id, name, description, price):
        item = self.__dao.select_item_by_no(item_no)
        if not item:
            return False
        if item.get_seller_id() != requester_id:   # 소유 검증
            return False
        item.set_name(name)
        item.set_description(description)
        item.set_price(price)
        return self.__dao.update_item(item_no, item)

    # 내 상품 등록 취소 (판매자 본인만)
    def delete_my_item(self, item_no, requester_id):
        item = self.__dao.select_item_by_no(item_no)
        if not item:
            return False
        if item.get_seller_id() != requester_id:   # 소유 검증
            return False
        return self.__dao.delete_item(item_no)

    # 관리자 강제 삭제 (소유 검증 없음)
    def force_delete_item(self, item_no):
        return self.__dao.delete_item(item_no)