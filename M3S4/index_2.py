#class list
lst = [4, -3, 5.66, False, ['Pera','Manzana'], (3,3)]

#<class> 'tuple'
tpl = (4, -3, 5.66, False, ['Pera','Manzana'], (3,3))

#indices
#s[i] - (i+1)-ésimo elemento
print(lst[3])
#s[i:j] - (i+1)-ésimo al (j-1)-ésimo
print(tpl[2:5]) #Del 3er al 4to elemento

#s[i:j:k] - (i+1)-ésimo al (j-1)-ésimo
#       - intercalando k pasos
print(lst[0:5:2]) #1er, 3er y 5to elemento

#s[-i] - i-ésimo elemento (del último al primero)
print(tpl[-1])

#s[i:] - del i-ésimo al último elemento (reversa)
print(lst[2:])

#s[-i:] - los últimos i elementos
print(lst[-2:])

#s[s[-i:-j] - del i-ésimo al j-ésimo elemento (reversa)
print(tpl[-3:-1])

#s[::-i] - todos los elementos al revés
#, de -i en -i
print(lst[::-1])

#s[-i:-j:-k] - elementos invertidos
#, de i a j, cada k posiciones
print(tpl[-1:-5:-2])

numbers = [1, 2, 3 , 4]
index = numbers.index(2)
print(index) #output: 1

#otro ej.
frutas = ['manzana', 'banana', 'naranja', 'pera', 'manzana']
#encuentra el elemento manzana entre índices 0 y 3
indice_manzana = frutas.index('manzana', 0, 3) 
print(indice_manzana)  # Output: 0

variable = 1,
print(type(variable))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # Los duplicados serán removidos
