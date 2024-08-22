class Libro:
    def __init__(self, autor: str, titulo: str) -> None:
        self.autor = autor
        self.titulo = titulo

class Libro_2(Libro):
    def __init__(self, autor: str, titulo: str, anno_de_publicacion: int) -> None:
        super().__init__(autor, titulo) #esto es lo que se trae de la clase padre, se me olvida
        self.anno_de_publicacion = anno_de_publicacion
    
    def __str__(self):
        return f'Nombre del Autor: {self.autor} \n Titulo del libro: {self.titulo}'

libro_1 = Libro('Dan Brown', 'Infierno')
libro_2 = Libro_2('Dan Brown', 'El Código Da Vinci', 2003)

print(libro_1.__dict__)
print(libro_2.__dict__)