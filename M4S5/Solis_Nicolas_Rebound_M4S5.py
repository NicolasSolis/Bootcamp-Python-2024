class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Método heredado de B")

class C (B, A): #(B, A) para que salga print Clase B // (A, B) para que salga print Clase A
    def metodo_c(self):
        print("Método es de clase C")

c = C()
c.metodo_a()
c.metodo_b()
c.metodo_c()