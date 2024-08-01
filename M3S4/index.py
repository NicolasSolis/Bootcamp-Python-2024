
""" a = b = c = 200
print(a, b, c) """

""" s = "esta es una variable global"

def f():
    #Variable local
    s = "esta es una variable local"
f()
print(s) """

""" mi_variable = 10 #variable global

def funcion():
    otra_variable = 5#local
    mi_variable = 15 #modificar mi_variable
    print(otra_variable) #Bien

funcion()
print(mi_variable)
print(otra_variable) #mal, esta variable es local """


""" #Datos numéricos (no terminé la diapo)
i = 5 #type(i) = <class 'int'>
f = 3.0 #type(f) = <class 'float'>
c = 2 + 3j #type(c) = <class 'complex'> """


""" print (0**0)
print (pow(0,0)) """


""" #Convertir str a int | float | complex
print((int('145')))
print((float('-145.344')))
print((complex('23-2j')))

#Convertir de int a float
print((float(38)))

#Convertir de float a int
print((int(34.99))) """


""" num_a = int(-223.5)
print(num_a)

num_b = int(4.1 * 53)
print(num_b)
"""
""" from math import sqrt
num_c = int(sqrt(2))
print(num_c)
"""
""" # 256 base 10 --> 0x100 base 16
print(hex(256))

print(bin(0o12))

print(oct()) """

""" num_g = float(57)
print(num_g) """

texto_3 = '''entre triple
comillas simple'''
texto_4 = """Entre triple
    comillas doble"""
texto_5 = 'ser ' + 'o no ser'
texto_6 = 'aro' * 5

print(texto_3)
print(texto_4)
print(texto_5)
print(texto_6)

print("ser o no ser\a")
