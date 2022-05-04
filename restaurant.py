class Table:

    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []
        self.total = 0

    def order(self, item, price, quantity):
        quantity = 1
        new_order = {"item": item, "price": price, "quantity": quantity}

        if new_order not in self.bill:
            self.bill.append(new_order)
        return self.bill
        #bill = dict.fromkeys(['item', 'price','quantity'])

        #bill.append(item,price,quantity)




        #if item not in self.bill:
        #bill.append(item)
        #for i in self.bill

    def remove(self):
        pass


    def get_subtotal(self):
        pass


    def get_total(self):
        pass

    def split_bill(self):
        pass







