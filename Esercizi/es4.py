class CSVFile():

    def __init__(self,name):
        self.name = name
    
    def get_data(self):
        elements = []
        list = []
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                elements[1] = elements[1].strip('\n')
                list.append(elements) 
                #print("elements: {}", list)
                
        my_file.close()
        return list

csv_file = CSVFile("shampoo_sales.csv")
data = csv_file.get_data()
print(data)