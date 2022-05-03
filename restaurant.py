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




table01 = Table(5)
table01.order("Risotto", 12.50, 2)
table01.order("Chicken", 12.50, 2)
table01.order("Risotto", 12.50, 2)
print(table01.bill)