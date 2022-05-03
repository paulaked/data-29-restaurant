class Table:
    def __init__ (self,people):
        self.bill = []
        self.people = people
        self.total = 0

    def order (self, item, price, quantity=1) -> list:
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
            return False
        elif self.bill != []:
            for x in self.bill:
                iandp = list(x.values())
                iandp = [iandp[0],iandp[2]]
                if x['item'] == item and x['quantity'] - quantity >= 1:
                    x.update({'item': item, 'price': price, 'quantity': (x['quantity']-quantity)})
                    return True
                if x['item'] == item and x['quantity'] - quantity < 1:
                    self.bill.pop(self.bill.index(x))
                    return True
        else:
            return False

    def get_subtotal (self):
        total = 0
        if self.bill == []:
            return 0
        if self.bill !=[]:
            for x in self.bill:
                total += x['price'] * x['quantity']
            return total

    def get_total (self,service_charge=0.1):
        subtotal = self.get_subtotal()
        self.total = subtotal + subtotal * service_charge
        return {'Sub Total': f'£{subtotal:.2f}', 'Service Charge': f'£{subtotal*service_charge:.2f}',
                'Total': f'£{self.total:.2f}'}

    @property
    def split_bill(self):
        self.total = (((self.total * 100)/self.people))/100
        return f'£{self.total:.2f}'



table01 = Table(5)
table01.order("Risotto", 12.50, 2)
table01.order("Risotto", 12.50, 2)
table01.order("Risotto", 12.50, 2)
table01.order("chicken", 12.50, 2)
print(table01.get_total())
print(table01.split_bill)