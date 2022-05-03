class Table:
    def __init__ (self,people):
        self.bill = []
        self.people = people

    def order (self, item, price, quantity:1) -> list:
        if self.bill == []:
            self.bill.append({'item': item, 'price': price, 'quantity': quantity})
            return
        else:
            for x in self.bill:
                iandp = list(x.values())
                if iandp[0:2] == [item, price]:
                    new_value = iandp[2]
                    x.update({'item': item, 'price': price, 'quantity': quantity + new_value})
                    return
            else:
                self.bill.append({'item': item, 'price': price, 'quantity': quantity})
                return

    def remove (self, item, price, quantity:1) -> list:
        if self.bill == []:
            return
        else:
            for x in self.bill:
                iandp = list(x.values())
                iandp = [iandp[0],iandp[2]]
                if x['item'] == item and x['quantity'] - quantity >= 1:
                    x.update({'item': item, 'price': price, 'quantity': (x['quantity']-quantity)})
                    return
                if x['item'] == item and x['quantity'] - quantity < 1:
                    self.bill.pop(self.bill.index(x))
                    return




table01 = Table(5)
table01.order("Risotto", 12.50, 2)
table01.order("Risotto", 12.50, 2)
print(table01.bill)
table01.order("Chicken", 12.50, 2)
print(table01.bill)
table01.remove("Risotto", 12.50, 2)
table01.remove("Risotto", 12.50, 2)



print(table01.bill)