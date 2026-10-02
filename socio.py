class Socio:
    """Representa a un socio de la biblioteca (máximo 3 libros a la vez)."""

    MAX_LIBROS = 3

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self._libros = []

    @property
    def libros(self):
        return self._libros

    def puede_pedir(self):
        return len(self._libros) < self.MAX_LIBROS

    def agregar_libro(self, libro):
        if not self.puede_pedir():
            raise ValueError("El socio ya tiene el límite máximo de libros prestados.")
        self._libros.append(libro)

    def quitar_libro(self, libro):
        if libro not in self._libros:
            raise ValueError("El socio no tiene ese libro prestado.")
        self._libros.remove(libro)

    def __str__(self):
        return f"{self.nombre} (DNI {self.dni}) - {len(self._libros)} libro(s) prestado(s)"
