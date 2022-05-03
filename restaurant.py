class Table:

    def __init__(self, diners: int):
        self.diners = diners
        self.bill = []
        self._total = 0
        self._subtotal = 0

    # method to append a menu item to the bill
    # passes test_order and test_order_no_quantity
    def order(self, item, price, quantity = 1):
        if len(self.bill) > 0:
            for i in self.bill:
                if item != i["item"]:
                    self.bill.append({"item": item, "price": price, "quantity": quantity})
                else:
                    i["quantity"] += quantity
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})


    # method to remove bill items
    # passes test_remove_no_item
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
        item_total = 0
        if len(self.bill) != 0:
            for i in self.bill:
                item_total = i["price"] * i["quantity"]
                bill_total += item_total
            self._subtotal = bill_total
            return round(self._subtotal, 2)
        else:
            pass
