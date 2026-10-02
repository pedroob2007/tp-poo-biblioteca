class Biblioteca:
    """Coordina los libros y los socios, y gestiona préstamos y devoluciones."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = {}   # isbn -> Libro (búsqueda O(1))
        self.socios = {}   # dni -> Socio (búsqueda O(1))

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            raise ValueError("Ya existe un libro registrado con este ISBN.")
        self.libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self.socios:
            raise ValueError("Ya existe un socio registrado con este DNI.")
        self.socios[socio.dni] = socio

    def prestar(self, isbn, dni):
        if isbn not in self.libros:
            raise ValueError("El libro no está registrado en la biblioteca.")
        if dni not in self.socios:
            raise ValueError("El socio no está registrado en la biblioteca.")

        libro = self.libros[isbn]
        socio = self.socios[dni]

        if not libro.disponible:
            raise ValueError("El libro solicitado no se encuentra disponible.")
        if not socio.puede_pedir():
            raise ValueError("El socio ha alcanzado el límite máximo de libros prestados.")

        # Todas las validaciones pasaron: recién ahora se modifica el estado
        libro.prestar()
        socio.agregar_libro(libro)

    def devolver(self, isbn, dni):
        if isbn not in self.libros:
            raise ValueError("El libro no está registrado en la biblioteca.")
        if dni not in self.socios:
            raise ValueError("El socio no está registrado en la biblioteca.")

        libro = self.libros[isbn]
        socio = self.socios[dni]

        socio.quitar_libro(libro)  # falla si el socio no tiene el libro
        libro.devolver()

    def libros_disponibles(self):
        return [libro for libro in self.libros.values() if libro.disponible]
