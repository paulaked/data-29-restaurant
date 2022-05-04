class Table:

    def __init__(self, tables):
        self.tables = tables
        self.bill = []


    def order(self, item, price, quantity=1):
        new_item = True
        for existing_order in self.bill:
            if item == existing_order["item"] and price == existing_order["price"]:
                existing_order["quantity"]+=quantity                            #changing quantity
                new_item = False
        if new_item == True:
            self.bill.append({"item": item, "price": price, "quantity":quantity})  # add item to the bill - append bill


    def remove(self, item, price, quantity=1):
        existing_item = True
        for existing_item in self.bill:
            if item == existing_item["item"] and price == existing_item["price"]:#item in bill with same item and price = true   #if statement
                existing_item["quantity"]-=quantity
        if quantity in self.bill == 0:
             self.bill.pop({"item": item, "price": price, "quantity":quantity})


            #if table order quantity = 0 then remove
        # #if existing_item["quantity"]=0 then remove #pop?
        # quantity less than or equal to existsing
        #check if item exists in bill (if item and price same in bill)
        #return true(remove item) if item and price same as bill
        #if quantity = 0 then remove item from bill
        #return false and bill does not change if item and price is not same as bill


    def get_subtotal(self):
        pass
        #return price * quantity
        #return price * quanity


    def get_total(self, service_charge=0.1):
        pass
        # return dictionary - use get_subtotal, service charge and total (subtotal * service charge)
       # up to 2 decimal places


    def split_bill(self):
        pass
    #total divided by number of diners
    #subtotal or total???


table1 = Table(5)
print(table1.bill)
table1.order("apple", "3", 2)
table1.order("apple", "3", 4)
table1.order("oranges", "2", 2)
print(table1.bill)
table1.remove("apple", "3",2)
print(table1.bill)
table1.remove("apple", "3", 4)
print(table1.bill)


