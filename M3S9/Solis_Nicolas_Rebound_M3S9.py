""" Loop de input para valores int, puse los cuadrados en el bucle 
    para castigar a la gente por no leer """
while True:
    try:
        b = int(input("Ingrese la base de su rectángulo "))
        h = int(input("Ingrese la altura de su rectángulo "))

    except ValueError as error:
        print('Por favor ingrese las medidas numéricas de su RECTÁNGULO')
        continue

    if h == b:
        print(f'Su figura es un cuadrado de área {h*b}')
    elif b <= 0 or h <= 0:
        print('Base y altura de su rectángulo deben ser positivas')
        continue
    else:
        break

def area(b, h):
    return b * h

area_rectangulo = area(b, h)
if b != h:
    print(f'La base de su rectángulo es {b}, su altura es {h} y el área de su rectángulo es {area_rectangulo}')