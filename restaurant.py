class Table:

    def __init__(self, diners: int):
        self.diners = diners
        self.bill = []
        self._total = 0
        self._subtotal = 0

    # method to append a menu item to the bill
    def order(self, item, price, quantity = 1):
        food_item = {"item": item, "price": price, "quantity": quantity}
        new_item = True
        if len(self.bill) > 0:
            for i in self.bill:
                if i["item"] == item and i["price"] == price:
                    i["quantity"] += quantity
                    new_item = False
        if new_item:
            self.bill.append(food_item)


    # method to remove bill items
    def remove(self, item, price, quantity = 1):
        if len(self.bill) != 0:
            for i in self.bill:
                if item == i["item"] and price == i["price"]:
                    if i["quantity"] - quantity <= 0:
                        self.bill.remove(i)
                    else:
                        i["quantity"] -= quantity
                else:
                    return False
        else:
            return False

    # get the total cost for the table based on quantities and prices in the bill
    def get_subtotal(self):
        bill_total = 0
        if len(self.bill) != 0:
            for i in self.bill:
                item_total = i["price"] * i["quantity"]
                bill_total += item_total
            self._subtotal = round(bill_total, 2)
            return self._subtotal
        else:
            pass

    # get the total, service charge, subtotal, returns a dictionary
    def get_total(self, service_charge_rate = 0.1):
        subtotal = (self.get_subtotal())
        self._total = (subtotal * (1+service_charge_rate))
        service_charge = (subtotal * service_charge_rate)
        return {"Sub Total": "£{:,.2f}".format(subtotal), "Service Charge": "£{:,.2f}".format(service_charge),
                "Total": "£{:,.2f}".format(self._total)}

    # no inputs, returns the subtotal / diners as float to 2 decimal places
    def split_bill(self):
        return round((self.get_subtotal()/self.diners), 2)
