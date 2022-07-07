from datetime import datetime

from utilities.db.db_manager import dbManager


class Order:
    def _init_(self, email, order_time, time_wanted, address, phone_number, pizza, amount, total_price, cc_number,
                 cc_exp, cvv):
        super()._init_()
        self.email = email
        self.order_time = order_time
        self.time_wanted = time_wanted
        self.address = address
        self.phone_number = phone_number
        self.pizza = pizza
        self.amount = amount
        self.total_price = total_price
        self.cc_number = cc_number
        self.cc_exp = cc_exp
        self.cvv = cvv

    def add_order(self):
        query = "INSERT INTO orders(email, order_time, time_wanted, address, phone_number, pizza, amount," \
                " total_price, cc_number, cc_exp, cvv) VALUES ('%s', '%s', '%s', %s,'%s', '%s', '%s', %s,'%s', '%s', '%s')" % (
            self.email, datetime.today(), self.time_wanted, self.address, self.phone_number, self.pizza, self.amount,
            self.total_price, self.cc_number, self.cc_exp, self.cvv)
        query_result = dbManager.commit(query)
        print(query_result)

    def search_order(self):
        query = f"select * from orders where email='%s'" % self.email
        query_result = dbManager.fetch(query)
        return query_result

    # def update_order(self):
    #     query = f"UPDATE orders set  where
    #     query_result = dbManager.commit(query)
    #     return query_result