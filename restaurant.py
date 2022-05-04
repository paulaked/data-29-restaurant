class Table:


    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self):
        pass

    def get_subtotal(self):
        pass

    def split_bill(self):
        pass
