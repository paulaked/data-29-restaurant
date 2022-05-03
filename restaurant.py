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


    def get_subtotal(self):
        pass
