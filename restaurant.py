class Table:

    def __init__(self,num):
        self.table = num
        self.bill =[]
        self.total = 0

    def order(self, item, price, quantity=1):
        for i in range(0,len(self.bill)):
            if self.bill[i]["item"] == item and self.bill[i]["price"] == price:
                self.bill[i]["quantity"] += 1

        self.bill.append({"item": item, "price" : price, "quantity": quantity})

    def remove(self, item, price, quantity):
        for i in range(0,len(self.bill)):
            if self.bill[i]["item"] == item and self.bill[i]["price"]==price:
                if self.bill[i]["quantity"] - int(quantity) >= 1:
                    self.bill[i]["quantity"] -= int(quantity)

                else:
                    self.bill[i].clear()

    def get_subtotal(self):
        for i in range(0,len(self.bill)):
            self.total += round((self.bill[i]["price"] * self.bill[i]["quantity"]),2)
        return self.total

    def get_total(self, service):
        self.get_subtotal()
        sc= self.total*service
        final_total= self.total + sc
        total={"Sub Total": f'£{"{:.2f}".format(self.total)}', "Service Charge": f'£{sc}', "Total":f'£{final_total}'}
        return total

    def split_bill(self):
        self.get_subtotal()
        return self.total / self.table








