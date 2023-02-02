class ExamException(Exception):
  pass  
    
class MovingAverage():
    
    def __init__(self, window):
        if not isinstance(window, int):  
            raise ExamException('Errore! Finestra non valida')
        elif window == None:
            raise ExamException('Errore')
        elif window <= 0:
            raise ExamException('Errore! La finestra non può essere minore o uguale a zero')
        else:    
            self.window = window
        
    def compute(self, lista):
        try:
            if len(lista) == 0:
                raise ExamException('Errore! La lista è vuota')
            elif not isinstance(lista, int) or not isinstance(lista, float):
               raise ExamException('Errore')
            else:
                    averageList= []
                    somma = 0
                    for i in range(len(lista)-1):
                        #print(len(lista))
                        somma = sum(lista[i:i+self.window])
                        #print(somma)
                        averageList.append(somma/self.window)
                    return averageList
        except TypeError: 
            print('Errore!')
     
