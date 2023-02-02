def sum_list(nums):
    sum = 0
    if len(nums) == 0:
        return None
    else: 
        for num in nums:
            sum = sum + num 
    
    return sum    

list = []
risultato = sum_list(list)
print('La somma è: {}'.format(risultato))