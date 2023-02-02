class ExamException(Exception):
  pass  
    
class Diff():
    
    def __init__(self, ratio):
        self.ratio = ratio
        
    def compute(self, lista):
        if len(lista) == 0:
            raise Exception('Errore! La lista è vuota')
        else:
            averageList= []
            differenza = 0
            for i in range(len(lista)-1):
                #print(len(lista))
                somma = (lista[i:i+self.winDow])
                #print(somma)
                averageList.append(somma/self.window)
            return averageList
    
 
moving_average = MovingAverage(2)

lista = []

result = moving_average.compute(lista)

print(result) # Deve stampare a schermo [3.0,6.0,12.0]