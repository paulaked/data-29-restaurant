import ast

class Table():
    # pass
    def __init__(self, table_number):
        self.table_number = table_number
        # self.guests = guests
        self.bill = []
        self.sub_total = 0
        self.total = 0

    def order(self, item, price, quantity=1):
        add_order = {
            'item': item,
            'price': price,
            'quantity': quantity
        }

        temp_list = []

        for i in self.bill:
            temp_list.append(i['item'])

        # Check Item not in self.bill
        if item not in temp_list:
            self.bill.append(add_order)

        # Update quantity of existing item
        if item in temp_list:
            for x in self.bill:
                if item == x['item']:
                    x['quantity'] += quantity

    def remove(self, item, price, quantity=1):
        # delete_order = {
        #     'item': item,
        #     'price': price,
        #     'quantity': quantity
        # }

        temp_list = []

        for i in self.bill:
            temp_list.append(i['item'])

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

    def get_total(self, ser_charge=0.10):
        # ser_charge_amt = self.sub_total * (ser_charge / 100)
        ser_charge_amt = self.sub_total * (ser_charge)
        total_amt = self.sub_total + ser_charge_amt

        total_summary = {}
        total_summary['Sub total'] = self.sub_total
        total_summary['Service charge'] = ser_charge_amt
        total_summary['Total'] = total_amt
        print(total_summary)
        self.total = str(total_summary)

    def split_bill(self, guests=4):
        # Code directly below converts a Dict to a Str. Note the import
        str_to_dict = ast.literal_eval(self.total)
        str_to_dict['Total'] / guests
        print(str_to_dict['Total'] / guests)

