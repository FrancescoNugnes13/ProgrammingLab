prev_value = None
data = [50,52,60]   
prediction = 0
for item in data:
    if prev_value != None:
        prediction += item - prev_value
        print('item: {}'.format(item))
        prev_value = item
        print('prediction: {}'.format(prediction))
    else:
        prev_value = item
print('data_len: {}'.format(len(data)))
prediction = prediction / (len(data)-1) + data[-1]
print('prediction: {}'.format(prediction))
print('data[0]: {}'.format(data[-1]))