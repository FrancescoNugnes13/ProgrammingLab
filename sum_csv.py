def sum_csv(my_file):
    values = []
    file = open(my_file, 'r')
    for line in file:
        elements = line.split(',')
        if elements[0] != 'Date':
            values.append(float(elements[1]))
    file.close()
    if(len(values)==0):
        return None
    else:
        return sum(values)
        
my_file = 'shampoo_sales.csv'
print('sum: {}'.format(sum_csv(my_file)))
