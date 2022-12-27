
from tabulate import tabulate

table = [['First Name', 'Last Name', 'Age'],
['John', 'Smith', 39],
['Mary', 'Jane', 25],
['Jennifer', 'Doe', 28]]

print(tabulate(table,headers='firstrow'))
print(tabulate(table, headers='firstrow', tablefmt='grid'))
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

# 使用字典生成表格
info = {'First Name': ['John', 'Mary', 'Jennifer'],
'Last Name': ['Smith', 'Jane', 'Doe'],
'Age': [39, 25, 28]}
print(info)
print(tabulate(info,headers='keys'))
print(tabulate(info, headers='keys', tablefmt='fancy_grid'))
print(tabulate(info, headers='keys', tablefmt='fancy_grid',showindex=True))
print(tabulate(info, headers='keys', tablefmt='fancy_grid',showindex=range(1,4)))