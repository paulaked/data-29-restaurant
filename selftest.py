from restaurant import Table

table_one = Table(1)
# print(table_one.table_number)
# print(table_one.bill)
table_one.order('salad', 12, 1)
table_one.order('sandwich', 12, 1)
table_one.order('coke', 12, 4)
table_one.order('salad', 12, 1)
# print(table_one.bill)
table_one.remove('coke', 1)
table_one.remove('hagis', 2)
print(table_one.bill)
table_one.get_subtotal()
print(table_one.sub_total)