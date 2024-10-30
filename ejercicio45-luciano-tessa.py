class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}"

class LibroTexto(Libro):
    def __init__(self, titulo, autor, precio, asignatura):
        super().__init__(titulo, autor, precio) #super llama al constructor de la clase libro
        self.asignatura = asignatura

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}, Asignatura: {self.asignatura}"

class LibroLiteratura(Libro):
    def __init__(self, titulo, autor, precio, genero):
        super().__init__(titulo, autor, precio)
        self.genero = genero

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}, Género: {self.genero}"

biblioteca = []

#función para registrar libros
def registrar_libro():
    tipo_libro = input("Presione 1 si es libro de texto. Presiones 2 si es un libro de literatura")
    titulo = input("Título: ")
    autor = input("Autor: ")
    precio = float(input("Precio: $"))
    
    if tipo_libro == "1":
        asignatura = input("Asignatura: ")
        libro = LibroTexto(titulo, autor, precio, asignatura)
    elif tipo_libro == "2":
        genero = input("Género: ")
        libro = LibroLiteratura(titulo, autor, precio, genero)
    else:
        print("Opción no válida.")
        return
    
    biblioteca.append(libro)
    print("El libro se registró con éxito.\n")

def listar_libros():
    if not biblioteca:
        print("No hay libros registrados.\n")
    else:
        for idx, libro in enumerate(biblioteca, 1): # el índice y el elemento de la lista que estás recorriendo.
            print(f"{idx}. {libro.mostrar_info()}") #index utiliza el numero que devuelve enumerate
        print()

def calcular_costo_total():
    if not biblioteca:
        print("No hay libros registrados para calcular el costo.\n")
    else:
        total = sum(libro.precio for libro in biblioteca)
        print(f"El costo total de los libros es: ${total}\n")

#menú
def menu():
    while True:
        print("Sistema de Gestión de Libros")
        print("1 - Registrar Libro")
        print("2 - Listar Libros")
        print("3 - Calcular Costo Total")
        print("4 - Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            listar_libros()
        elif opcion == "3":
            calcular_costo_total()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    menu()
