"""
Automate the boring stuff Table Printer
"""


def print_table(tables):
    """
    
    :param tables: 
    :return: 
    """
    column_width = [0] * len(tables)

    for i in range(len(tables[0])):
        for j in range(len(tables)):
            column_width[j] = len(max(tables[j], key=len))
            a = tables[j][i]
            print(a.rjust(column_width[j]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
