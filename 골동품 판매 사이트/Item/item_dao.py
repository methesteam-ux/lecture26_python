from Item.item import Item

# 골동품 상품 데이터 접근 (CRUD)
class ItemDAO:
    def __init__(self):
        self.__itemDB = {}  # 상품번호 : Item 객체

    def insert_item(self, item):
        item_no = item.get_item_no()
        if item_no not in self.__itemDB:
            self.__itemDB[item_no] = item
            return True
        return False

    def select_item_by_no(self, item_no):
        if item_no in self.__itemDB:
            return self.__itemDB[item_no]
        return None

    def select_all_items(self):
        item_list = list(self.__itemDB.values())
        if len(item_list):
            return item_list
        return None

    # 특정 회원이 등록한(판매 중인) 상품 목록
    def select_items_by_seller(self, seller_id):
        item_list = []
        for item in self.__itemDB.values():
            if item.get_seller_id() == seller_id:
                item_list.append(item)
        if len(item_list):
            return item_list
        return None

    # 이름에 키워드가 포함된 상품 검색
    def search_items_by_name(self, keyword):
        item_list = []
        for item in self.__itemDB.values():
            if keyword in item.get_name():
                item_list.append(item)
        if len(item_list):
            return item_list
        return None

    def update_item(self, item_no, item):
        if item_no in self.__itemDB:
            self.__itemDB[item_no] = item
            return True
        return False

    def delete_item(self, item_no):
        if item_no in self.__itemDB:
            self.__itemDB.pop(item_no)
            return True
        return False