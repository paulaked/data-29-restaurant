class Table:

    def __init__(self, diners, bill): 
        self.bill = []          
        self.diners = diners

    def order(self, item, price, quantity=1):
        add_order = {
            'item': item,
            'price': price,
            'quantity': quantity
        }

        temp.list = []

        for i in self.bill:
            temp.list.append(i['item'])
        
        if item not in temp.list:
           self.bill.append(add_order)
        
        if item in temp.list:
            for x in self.bill:
                if item == x['item']:
                    x['quantity'] += quantity

    my_table = Table(4,5)
    my_table.order('burger', 14,2) 
    my_table.order('chips', 3,1)
    my_table.order('chip', 3,6)
    # print(my_table.bill)               
        
    #     #check if the item is already on the bill
    #     #if it is on the bill, update the quantity
    #     #if the item is not on the bill, we add the item
       
    # def remove(self, item, price, quantity=1): #these are items which you are passing through to the remove function
    #     # we need to edit the bill
    #     # returing true or false based on whether the bill was changed
    #     print()

    # def get_subtotal(self):
    #     print()   

    # def get_total(self, service_charge=0.1):
    #     # return dict. with the keys: sub total(use get_subtotal), s
    #     # service charge=0.1, (subtotal * service charge)
    #     #
    #     print() 


    # def split_bill(self):    
    #     #return sub       



