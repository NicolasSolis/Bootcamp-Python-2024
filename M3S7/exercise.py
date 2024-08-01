#Ejercicios LMS

#Evaluando múltiples condiciones con while
""" contador = 0
a = 5
b = 10

while contador < a and contador < b: 
    print(f"cuenta: { contador }, a: {a}, b: {b}") #Aunque cuenta hasta 4, se imprimen 5 líneas porque el 'contador' es 0
    contador += 1
"""
#Operador or con while
""" a = 5 
b = 10 
contador = 0 

while contador < a or contador < b: 
    print(f"cuenta: { contador }, a: {a}, b: {b}") 
    contador += 1 """

#Ejercicio 3, recorriendo un diccionario
    #Formas de construir un diccionario (hay más, la tradicional es la 1era)

acciones = {    #es más rápido que todo esto sea en línea
    'AAPL': 187.31, 
    'MSFT': 124.06, 
    'FB': 183.50
    }
acciones_2 = {[('AAPL', 187.31),('MSFT',124.06),('FB', 183.50)]}
acciones_3 = dict(zip(['AAPL','MSFT','FB'],[187.31,124.06,183.50]))
acciones_4 = dict(AAPL=187.31, MSFT=124.06, FB=183.50)
    
    #Se puede asignar variables como a,b = 1,2; por eso tb se puede iterar en diccionarios 
for clave, valor in acciones.items():

    #Formas de hacer print
    print(clave + " : " + str(valor)) #no se puede tirar valor si no es string, es más fácil darle formato
    #print(f'{clave} : {valor}')
    #print(clave, ':',valor)
    #print('{} : {}'.format(clave,valor))
    #print('%s : %.2f' % (clave,valor)) #estilo C, '%.2f' indica que es un float con dos decimales, entero base 10 decimal
