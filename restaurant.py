class Table:

    def __init__(self, number_of_people):
        self.number_of_people = number_of_people
        self.bill = []
        self.total = 0

    def order(self, item, price, quantity):
        new_order = {"item": item, "price": price, "quantity": quantity}
        quantity = 1
        if new_order not in self.bill:
            self.bill.append(new_order)
        return self.bill

    def remove(self, item,price, quantity):
        for i in range(0, len(self.bill)):
            if self.bill[i]["item"] == item and self.bill[i]["price"] == price:
                if self.bill[i]["quantity"] - int(quantity) >= 1:
                    self.bill[i]["quantity"] -= int(quantity)

                else:
                    self.bill[i].clear()


    def get_subtotal(self):
        total = 0
        if self.bill == []:
            return 0
        else:
            for i in self.bill:
                self.total +=  i["price"] * i["quantity"]
        return self.total

    def get_total(self, service_charge):
        self.get_subtotal()
        service_charge_total = self.total * service_charge
        final_total = service_charge_total + self.total
        new_total = {"Sub Total":f"£{self.total}", "Service Charge":f"£{service_charge_total}" , "Final Total":f"£{final_total}"}
        return new_total

    def split_bill(self):
        self.get_subtotal()
        return self.total/self.number_of_people




