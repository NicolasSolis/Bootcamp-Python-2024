#2. Acciones de limpieza con Finally

try:
    raise ValueError
finally:
    print('Goodbye, world!')