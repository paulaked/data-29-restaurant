import decimal


class Table:

    def __init__(self,num):
        self.table = num
        self.bill =[]
        self.total = 0

    def order(self, item, price, quantity=1):
        a=False
        p = 0
        for i in self.bill:
            if self.bill[p]["item"] == item and self.bill[p]["price"] == price:
                self.bill[p]["quantity"] += 1
                p+=1
        self.bill.append({"item": item, "price" : price, "quantity": quantity})



    def remove(self, item, price, quantity):
        p=0
        for i in self.bill:
            if self.bill[p]["item"] == item and self.bill[p]["price"]==price:
                if self.bill[p]["quantity"] - int(quantity) >= 1:
                    self.bill[p]["quantity"] -= int(quantity)

                else:
                    self.bill[p].clear()
            p+=1


    def get_subtotal(self):
        p=0
        for i in self.bill:
            self.total += (self.bill[p]["price"] * self.bill[p]["quantity"])
            p+=1
        return self.total

    def get_total(self, service):
        self.get_subtotal()
        t= "{:.2f}".format(self.total)
        sc= self.total*service
        final_total= self.total + sc
        total={"Sub Total": f'£{t}', "Service Charge": f'£{sc}', "Total":f'£{final_total}'}
        return total

    def split_bill(self):
        self.get_subtotal()
        return self.total / self.table








