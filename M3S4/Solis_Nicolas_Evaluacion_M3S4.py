""" Creación, génesis, nacimiento de variables de personas en un dictionary (diccionario).
        Nota: hay una discusión técnica sobre si son una colección ordenada o no, 
        desde 3.7 indican que son ordenadas, tengo k investigar más."""
persona_1 = {'nombre':'Pedro', 'apellido':'Pérez', 'teléfono':'+569133'}
persona_2 = {'nombre':'Juan', 'apellido':'John', 'teléfono':'+569911'}
persona_3 = {'nombre':'Diego', 'apellido':'Jacques', 'teléfono':'+56224398800'}

#Creación de lista y print
mi_lista = [persona_1, persona_2, persona_3]
print(mi_lista)

#Había una forma de hacerlo como:
#mi_lista = [{'nombre':'Pedro', 'apellido':'Pérez', 'teléfono':'+569133'}, {'nombre':'Juan', 'apellido':'John', 'teléfono':'+569911'}, {'nombre':'Diego', 'apellido':'Jacques', 'teléfono':'+56224398800'}]