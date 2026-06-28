from Purchase.purchase_log import PurchaseLog

# 거래 로그(판매 로그) 데이터 접근
# 거래 내역은 보존 대상이므로 수정/삭제 기능을 두지 않는다. (NFR-REL-003)
class PurchaseLogDAO:
    def __init__(self):
        self.__logDB = {}  # 거래번호 : PurchaseLog 객체

    def insert_log(self, log):
        log_no = log.get_log_no()
        if log_no not in self.__logDB:
            self.__logDB[log_no] = log
            return True
        return False

    # 구매자 기준 조회 (구매 내역)
    def select_logs_by_buyer(self, buyer_id):
        log_list = []
        for log in self.__logDB.values():
            if log.get_buyer_id() == buyer_id:
                log_list.append(log)
        if len(log_list):
            return log_list
        return None

    # 판매자 기준 조회 (판매 내역)
    def select_logs_by_seller(self, seller_id):
        log_list = []
        for log in self.__logDB.values():
            if log.get_seller_id() == seller_id:
                log_list.append(log)
        if len(log_list):
            return log_list
        return None

    def select_all_logs(self):
        log_list = list(self.__logDB.values())
        if len(log_list):
            return log_list
        return None