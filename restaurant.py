class Table:


    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order(self, item, price, quantity=1):
        new_item = True
        for exist_item in self.bill:
            if item == exist_item["item"] and price == exist_item["price"]:
                exist_item["quantity"] += quantity
                new_item = False
        if new_item:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity = 1):
        for exist_item in self.bill:
            if item == exist_item["item"] and price == exist_item["price"]:
                if exist_item["quantity"] < quantity:
                    return False
                elif exist_item["quantity"] == quantity:
                    self.bill.remove(exist_item)
                    return True
                else:
                    exist_item["quantity"] -= quantity
                    return True
        return False

    def get_subtotal(self):
        subtotal = 0
        for item in self.bill:
            subtotal += (item["price"] * item["quantity"])
        return subtotal

    def get_total(self, service_charge=0.1):
        subtotal = self.get_subtotal()
        return {
            "Sub Total": f"£{subtotal:.2f}",
            "Service Charge": f"£{subtotal * service_charge:.2f}",
            "Total": f"£{subtotal * (1+service_charge):.2f}"
        }

    def split_bill(self):
        return f"{self.get_subtotal() / self.num_of_people}"
