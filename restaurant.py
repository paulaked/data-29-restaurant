class Table:

    def __init__(self, diners: int):
        self.diners = diners
        self.bill = []

    # method to append a menu item to the bill
    # passes test_order and test_order_no_quantity
    def order(self, item, price, quantity = 1):
        if {"item": item, "price": price, "quantity": quantity} not in self.bill:
            self.bill.append({"item": item, "price": price, "quantity": quantity})
        else:
            self.bill.update({"quantity": quantity + 1})

    # method to remove bill items
    # passes test_remove_no_item
    def remove(self, item, price, quantity = 1):
        if {"item": item, "price": price, "quantity": quantity}  in self.bill:
            self.bill.pop({"item": item, "price": price, "quantity": quantity})
        else:
            pass

