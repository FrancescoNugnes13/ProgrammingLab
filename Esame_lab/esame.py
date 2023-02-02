class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    
    #Istanzio il nome del file in cui sono presenti i dati
    def __init__(self,name):
        self.name = name
        
    #Classe get_data che ritornerà una lista di liste contenenti i dati delle misurazioni
    def get_data(self):
        
        #Try-except per il controllo di eventuali errori durante l'apertura del file
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            raise ExamException('Errore in apertura del file: "{}"'.format(e))
            
        #Lista di appoggio per manipolare i dati
        elements = []
        #Lista che verrà usata per ritornare i dati
        list = []
        
        prev_element = None
        
        #Ciclo for che assegna a line ogni volta un elemento diverso di my_file
        for line in my_file:
            
            #Divido line in 2 parti sulla virgola per dividere i giorni dalle temperature
            elements = line.split(',')
            
            #Escludo la prima colonna in cui è presente l'intestazione
            if elements[0] != 'epoch':
                #Try-except che ignora tutte le righe in cui non sono presenti valori numerici
                try:
                    elements[1] = elements[1].strip('\n')    
                    elements[0] = float(elements[0])
                    elements[1] = float(elements[1])

                    #Converto a interi tutti i timestamp
                    if isinstance(elements[0], float):
                        elements[0] = int(elements[0])
   
                except:
                    continue

                #if che verifica che tutti i timestamp siano in ordine crescente
                if prev_element is not None and elements[0] < prev_element:
                    raise ExamException("Errore! I dati non sono in ordine crescente")
                prev_element = elements[0]
                
                #Assegno a list i dati una volta formattati 
                list.append(elements)
                
        #for annidato che verifica la presenza di timestamp duplicati
        for i in range(len(list)):
            for j in range(len(list)):
                    if list[i][0] == list[j][0] and i != j:
                        raise ExamException("Errore! Sono presenti timestamp duplicati")
                        
        my_file.close()
        
        return list
        
#Funzione che calcola la differenza massima di temperatura di un giorno
def compute_daily_max_difference(time_series):
    
    #Lista che verrà usata per ritornare i dati
    temp_difference = []
    
    #Lista di appoggio che verrà usata per salvare le temperature di un singolo giorno
    one_day_temp = []

    #For che scorre la lista di liste fermandosi un giro prima per non andare in overflow
    for i in range(len(time_series) - 1):    
        
        #Uso una formula per ricavare l'inizio del giorno presente in time_series[i][0]/[i+1][0]
        current_day = time_series[i][0] - (time_series[i][0] % 86400)
        next_day = time_series[i+1][0] - (time_series[i+1][0] % 86400)    

        #Se i giorni coincidono aggiungo a one_day_temp la temperatura
        if  current_day == next_day:
            one_day_temp.append(time_series[i][1])    

        #Se i giorni non coincidono vuol dire che le misurazioni per quel determinato giorno sono finite e devo 
        #calcolare la differenza
        else:
            one_day_temp.append(time_series[i][1])
            max_temp = max(one_day_temp)
            min_temp = min(one_day_temp)       

            #Se la lunghezza della lista è 1 vuol dire che è presente una sola temperatura per quel determinato 
            #giorno quindi devo aggiungere None alla lista
            if len(one_day_temp) == 1:
                temp_difference.append(None)
                
                #Svuoto la lista
                one_day_temp.clear()           

            #Se la lunghezza non è 1 vado a calcolare la differenza tra il massimo e il minimo limitando il 
            #risultato a 2 cifre decimali
            else:
                temp_difference.append(round(max_temp-min_temp, 2))
                one_day_temp.clear()    

    #Gestisco il caso in cui la lista ha una sola riga al suo interno
    if len(time_series) == 1:
        temp_difference.append(None)
        
    #Vado gli ultimi due elementi della lista in modo equivalente agli altri    
    elif  len(one_day_temp) == 1 and not (i == len(time_series ) - 2):
        temp_difference.append(None)    
        
    elif i == len(time_series ) - 2:
        one_day_temp.append(time_series[i][1])
        one_day_temp.append(time_series[i+1][1]) 
        current_day = time_series[i][0] - (time_series[i][0] % 86400)
        next_day = time_series[i+1][0] - (time_series[i+1][0] % 86400)   
        
        if current_day != next_day:
            temp_difference.append(None)
            
        else:
            max_temp = max(one_day_temp)
            min_temp = min(one_day_temp)
            temp_difference.append(round(max_temp-min_temp, 2))    
            
    return temp_difference    