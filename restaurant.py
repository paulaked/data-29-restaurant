class Table():
    # pass
    def __init__(self, table_number):
        self.table_number = table_number
        self.bill = []
        self.sub_total = 0

    def order(self, item, price, quantity=1):
        add_order = {
            'item': item,
            'price': price,
            'quantity': quantity
        }
        # self.bill.append(add_order)

        temp_list = []

        for i in self.bill:
            temp_list.append(i['item'])

        if item not in temp_list:
            self.bill.append(add_order)

        if item in temp_list:
            for x in self.bill:
                if item == x['item']:
                    x['quantity'] += quantity

    def remove(self, item, quantity=1):
        delete_order = {
            'item': item,
            'quantity': quantity
        }

        temp_list = []

        # for i in self.bill:
        #     temp_list.append(i['item'])

        for i in self.bill:
            temp_list.append(i['item'])

        if item in temp_list:
            for x in self.bill:
                if item == x['item']:
                    x['quantity'] -= quantity
                    if x['quantity'] <= 0:
                        print('success')
                        print(type(str(self.bill[0])))
                        self.bill.pop(len(temp_list) - 1)
                        break
        else:
            print(item, 'does not exist in your bill')

    def get_subtotal(self):
        for i in self.bill:
            self.sub_total += i['price'] * i['quantity']

        print(self.sub_total)
