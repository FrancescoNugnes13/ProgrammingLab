class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    #Istanzio il nome del file in cui sono presenti i dati
    def __init__(self,name):
        self.name = name
    #Classe get_data che ritornerà una lista di liste contenenti i dati delle misurazioni
    def get_data(self):
        #Apro il file "data.csv"i
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            raise ExamException('Errore in apertura del file: "{}"'.format(e))
            
        #Lista di appoggio per manipolare i dati
        elements = []
        #Lista che verrà usata per ritornare i dati
        list = []
        #Ciclo for che assegna a line ogni volta un elemento diverso di my_file
        prev_element = None
        
        for line in my_file:
                #Divido line in 2 parti sulla virgola per dividere  i giorni dalle temperature
            elements = line.split(',')
            
            #Escludo la prima colonna in cui è presente l'intestazione
            if elements[0] != 'epoch':    
                    #Elimino il carattere \n dal secondo elemento di "elements"
                
                try:
                    elements[1] = elements[1].strip('\n')    
                    elements[0] = float(elements[0])
                    if isinstance(elements[0], float):
                        elements[0] = int(elements[0])
                            
                    elements[1] = float(elements[1])
                except:
                    continue
                if prev_element is not None and elements[0] < prev_element:
                    raise ExamException("Errore! I dati non sono in ordine crescente")
                prev_element = elements[0]
                    #Assegno a list i dati una volta formattati 
                list.append(elements)    
        for i in range(len(list)):
            for j in range(len(list)):
                    if list[i][0] == list[j][0] and i != j:
                        raise ExamException("Errore! Sono presenti time stamps duplicati")
        #print(list)            
        my_file.close()
        return list


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
#print(time_series)

#Funzione che calcolerà la differenza massima di temperatura di un giorno
def compute_daily_max_difference(time_series):
    temp_difference = []
    one_day_data = []
    
    for i in range(len(time_series) - 1):    
        current_day = time_series[i][0] - (time_series[i][0] % 86400)
        next_day = time_series[i+1][0] - (time_series[i+1][0] % 86400)    
        if  current_day == next_day:
            one_day_data.append(time_series[i][1])        
        else:
            one_day_data.append(time_series[i][1])
            max_temp = max(one_day_data)
            min_temp = min(one_day_data)       
            if len(one_day_data) == 1:
                temp_difference.append(None)
                one_day_data.clear()           
            else:
                temp_difference.append(round(max_temp-min_temp, 2))
                if i != len(time_series) - 2:
                    one_day_data.clear()    
                    
    if len(one_day_data) == 1 and not (i == len(time_series ) - 1):
        temp_difference.append(None)    
    elif i == len(time_series ) - 1:
        one_day_data.append(time_series[i][1])
        one_day_data.append(time_series[i+1][1]) 
        current_day = time_series[i][0] - (time_series[i][0] % 86400)
        next_day = time_series[i+1][0] - (time_series[i+1][0] % 86400)   
        
        if current_day != next_day:
            temp_difference.append(None)
        else:
            max_temp = max(one_day_data)
            min_temp = min(one_day_data)
            temp_difference.append(round(max_temp-min_temp, 2))    
    return temp_difference    
    
max_temp = compute_daily_max_difference(time_series)
#print(max_temp) 