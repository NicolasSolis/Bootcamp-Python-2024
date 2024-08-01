#ta difícil de leer, perdón me está costando lo de las listas
mi_lista = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

#se elimina la sublista que parte en 0
#filtrando por las que en índice 0 tienen algo que no sea 0 
mi_lista_filtro = [sublista for sublista in mi_lista if sublista[0] != 0 ]
print(f'Esta es la lista excluyendo la sublista que comienza con "0": {mi_lista_filtro}')

#copié mi mismo código esperando que funcionara algo
#filtrando para quedarse con las sublistas que no contengan 0
mi_lista_filtro_0 = [sublista for sublista in mi_lista if 0 not in sublista ]
print(f'Esta es la lista que excluye las sublistas que contienen "0": {mi_lista_filtro_0}')

mi_diccionario = {'A':[1,2,3], 'B':[0,4,5], 'C':[4,0,1], 'D':[6,5,4]}

print(mi_diccionario['A'][1]) #prueba
print(type(mi_diccionario))

print(f'El diccionario fue lo único que hice de memoria:\n {mi_diccionario}')