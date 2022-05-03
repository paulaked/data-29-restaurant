class Table:

    def __init__(self, diners: int):
        self.diners = diners
        self.bill = []

    # method to append a menu item to the bill
    def order(self, item, price, quantity = 1):
        if {"item": item, "price": price, "quantity": quantity} not in self.bill:
            self.bill.append({"item": item, "price": price, "quantity": quantity})
        else:
            self.bill.update({"quantity": quantity + 1})

    

