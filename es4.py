class CsvFile():

    def __getdata__(self, name):
        self.name = name
        elements = []
        values = []
        my_file = open(name, 'r')
        
        for line in my_file:
            if elements != 'Date,Sales':
                values.append(elements)
                print("elements: {}", values)
                
        my_file.close()
        return values


