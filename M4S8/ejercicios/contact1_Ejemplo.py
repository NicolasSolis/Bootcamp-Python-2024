import os
import re

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def mostrar_contacto(self):
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            nombre = input("\nIngrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")

            while True:
                email = input("Ingrese el correo electrónico: ")
                if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                    break
                else:
                    print("\nError: El correo electrónico no es válido.")
                    eleccion = input("¿Desea volver a intentarlo? (s/n): ").lower()
                    if eleccion != 's':
                        print("\nCancelando la adición del contacto.")
                        return  # Sale de la función si el usuario elige no volver a intentarlo

            contacto = Contacto(nombre, telefono, email)
            self.contactos.append(contacto)
            print("\nContacto agregado correctamente.")
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("\nError: Ingrese datos válidos.")
            input("\nPresione Enter para continuar...")

    def mostrar_contactos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if not self.contactos:
            print("\nNo hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                contacto.mostrar_contacto()
                print("-" * 20)
        input("\nPresione Enter para continuar...")

    def buscar_contacto(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        nombre = input("\nIngrese el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.mostrar_contacto()
                encontrado = True
                break
        if not encontrado:
            print("\nContacto no encontrado.")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    agenda = Agenda()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenú:")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agenda.agregar_contacto()
        elif opcion == "2":
            agenda.mostrar_contactos()
        elif opcion == "3":
            agenda.buscar_contacto()
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción inválida.")
            input("\nPresione Enter para continuar...")

    # Aquí se demuestra la necesidad de archivos
    print("\nLa agenda se ha cerrado.")