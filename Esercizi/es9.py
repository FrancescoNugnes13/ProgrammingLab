class Errore(Exception):
    pass


class Model():

    def fit(self, data):
        #fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def predict(self, data): 
        prev_value = None
        prediction = 0

        for item in data:
            if not isinstance(item, int):
                raise TypeError('Non è possibile calcolare una previsione su dati non numerici')
            else:
                if prev_value != None:
                    prediction += item - prev_value
                    #print('item: {}'.format(item))
                    prev_value = item
                    #print('prediction: {}'.format(prediction))
                else:
                    prev_value = item
            #print('data_len: {}'.format(len(data)))
        if len(data) <= 1:
            raise Errore("Troppi pochi dati per poter eseguire una previsione")
        else:
            prediction = prediction / (len(data) - 1) + data[-1]
            #print('prediction: {}'.format(prediction))
        return prediction

class FitIncrementModel(IncrementModel):

    def fit(self, data):
        prev_value = None
        prediction = 0
        
        for item in data:
            if prev_value != None:
                prediction += item - prev_value
                #print('item: {}'.format(item))
                prev_value = item
                #print('prediction: {}'.format(prediction))
            else:
                prev_value = item
                
        self.global_avg_increment = prediction / (len(data) - 1)

    def predict(self, data):
        
        prediction_sum = super().predict(data) + self.global_avg_increment

        return prediction_sum


