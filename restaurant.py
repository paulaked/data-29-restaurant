class Table:

    def __init__(self, number_of_people, bill):
        self.number_of_people = number_of_people
        self.bill = bill

    def order(self, item, price, quantity):
        bill = dict.fromkeys(['item', 'price','quantity'])
        #orders = {"item": item, "price": price, "quantity": quantity}
        bill.append(item,price,quantity)

    def remove(self):


    def get_subtotal(self):
        pass


    def get_total(self):
        pass

    def split_bill(self):
        pass







