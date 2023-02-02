class CSVFile():

    def __init__(self,name):
            self.name = name

    def get_data(self):
        elements = []
        list = []
        try:
            my_file = open(self.name, 'r')
            for line in my_file:
                elements = line.split(',')
                if elements[0] != 'Date':
                    #elements[1] = elements[1].strip('\n')
                    list.append(elements) 
                #print("elements: {}", list)
                
            my_file.close()
            return list
        except FileNotFoundError:
            print('Errore! File non trovato')
class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        
        string_data = super().get_data()
        
        numerical_data = []
        
        for string_row in string_data: 
            
            numerical_row = []
            
            for i,element in enumerate(string_row):
                
                if i == 0:
                    numerical_row.append(element)
            
                else:
                    
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerics: "{}"'.format(element, e))

            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        
        return numerical_data
        
        #print("\n")
        #print("{}".format(list))
        
csv_file = NumericalCSVFile("shampoo_sales.csv")
data = csv_file.get_data()
data = data[1:2]
print(data)