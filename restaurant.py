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

    def remove(self, item, quantity):

        #new_order = {"item": item, "price": price, "quantity": quantity}
        pass
    #edit the bill
    #returning true or false based on the bill


    def get_subtotal(self):
        total = 0
        if self.bill == []:
            return 0
        else:
            for i in self.bill:
                total +=  i["price"] * i["quantity"]
        return total

    def get_total(self, service_charge):
        self.get_subtotal()
        total_service_charge = total * service_charge
        final_total = total_service_charge + total
        total = {"Sub Total":total,"Service Charge":total_service_charge ,"Final Total":final_total}



    def split_bill(self):
        self.get_subtotal()
        return self.total/self.number_of_people




