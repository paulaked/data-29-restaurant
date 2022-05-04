class Table:
    def __init__(self,num_of_people):
        self.num_of_people = num_of_people
        self.bill = []

    def order (self, item: object, price: object, quantity: object = 1) -> object:

        add_order = {'item': item, 'price': price, 'quantity': quantity}

        temp_list =[]

        for i in self.bill:
            temp_list.append(i['item'])

        if item not in temp_list:
            self.bill.append(add_order)

        if item in temp_list:
            for x in self.bill:
                if item == x ['item']:
                    x['quantity'] += quantity


    def remove (self, item, price, quantity =1):
        pass
    #editing the bill
    #returing true or false based on wheather the bill was changed

    def get_subtotal (self):
        pass
    #calculating the total for each price of item by quantity
    #return the subtotal
    # values should be returned to 2 decimal places

    def get_total (self, service_charge=0.1):
        pass
    #retunr a dict with the keys: subtotal (use get_subtotal), service charge, total (sub total * service charge)
    #values should be returned to 2 decimal places

    def split_bill (self):
        pass
        #retun sub_total/ num of people