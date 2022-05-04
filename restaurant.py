class Table:

    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []
        self.total = 0

    def order(self, item, price, quantity):
        quantity = 1

        bill = dict.fromkeys(['item', 'price','quantity'])
        #orders = {"item": item, "price": price, "quantity": quantity}
        bill.append(item,price,quantity)

    def remove(self):
        pass


    def get_subtotal(self):
        pass


    def get_total(self):
        pass

    def split_bill(self):
        pass







