class Errore(Exception):
    pass

class CSVFile():

    def __init__(self,name):
        self.name = name
        if not isinstance(self.name, str):
            raise Errore('Errore, Nome file non conforme')

    def get_data(self, start = None, finish = None):
            
        elements = []
        list = []
        try:
            my_file = open(self.name, 'r')

            if my_file == '':
                raise Errore('Errore, File vuoto')
            elif not isinstance(start, int) or not isinstance(finish, int):
                raise Errore('Errore, Start e finish devono essere 2 numeri interi')
            #elif finish > len(range(my_file)):
            #    raise Errore('Start non può essere più grande della dimensione della lista')
            elif start > finish:
                raise Errore('Errore, Start non può essere più grande di finish')
            else:
                for line in my_file:
                    elements = line.split(',')
                    
                    if elements[0] != 'Date':    
                        list.append(elements) 
                    
                list = list[start:finish]    
                my_file.close()
                return list
            
        except FileNotFoundError:
            print('Errore! File non trovato')
            
class NumericalCSVFile(CSVFile):
    
    def get_data(self, *args, **kwargs):
        string_data = super.getdata(*args, **kwargs)
        
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
        
#csv_file = CSVFile("shampoo_sales.csv")
#data = csv_file.get_data(2,7)
#print(data)