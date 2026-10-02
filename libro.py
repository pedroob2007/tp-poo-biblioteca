class Libro:
    """Representa un libro de la biblioteca."""

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self._disponible = True

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self._disponible:
            raise ValueError("El libro ya se encuentra prestado.")
        self._disponible = False

    def devolver(self):
        if self._disponible:
            raise ValueError("El libro ya está disponible (no estaba prestado).")
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"
