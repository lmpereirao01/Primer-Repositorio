###
# Escribe una función que reciba por parámetro una lista de enteros y devuelva dos listas: 
# una con los valores negativos que tuviera y otra con los positivos. 
# Ambas listas deben estar ordenadas ascendentemente
###

def return_lists(number_list):
    positive_numbers = []
    negative_numbers = []
    for num in number_list: 
        if num >= 0: positive_numbers.append(num)
        else: negative_numbers.append(num)
        
    positive_numbers.sort()
    negative_numbers.sort()
        
    print(f"Los números positivos corresponden a: {positive_numbers} \ny los negativos: {negative_numbers}")
        
        
number_list = [1, -5, 6, -9, 0, -14, 32, 7, -1, -6, -3]
return_lists(number_list)

