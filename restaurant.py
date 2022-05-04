class Table:

    def __init__(self, diners: int):
        self.diners = diners
        self.bill = []
        self._total = 0
        self._subtotal = 0

    # method to append a menu item to the bill
    def order(self, item, price, quantity = 1):

        food_item = {"item": item, "price": price, "quantity": quantity}
        amend_list = []
        append_list = []
        if len(self.bill) > 0:
            for i in self.bill:
                if i["item"] == food_item["item"] and i["price"] == food_item["price"]:
                    i["quantity"] += food_item["quantity"]
                else:
                    self.bill.append(i)
        else:
            self.bill.append(food_item)

        return self.bill



    # method to remove bill items
    def remove(self, item, price, quantity = 1):
        if len(self.bill) != 0:
            for i in self.bill:
                if item == i["item"]:
                    if i["quantity"] - quantity <= 0:
                        self.bill.remove(i)
                    else:
                        i["quantity"] -= quantity
                else:
                    return False
        else:
            return False

    # get the total cost for the table based on quantities and prices in the bill
    def get_subtotal(self):
        bill_total = 0
        if len(self.bill) != 0:
            for i in self.bill:
                item_total = i["price"] * i["quantity"]
                bill_total += item_total
            self._subtotal = round(bill_total, 2)
            return self._subtotal
        else:
            pass


table02 = Table(2)

table02.order('Food1', 10.00, 3)
table02.order('Food2', 20.00, 1)
table02.order('Food3', 0.50, 1)

print(table02.bill)