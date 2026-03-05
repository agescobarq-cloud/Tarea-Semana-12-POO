class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Título y autor se almacenan como TUPLA (inmutable)
        self.titulo_autor = (titulo.strip(), autor.strip())
        self.categoria = categoria.strip()
        self.isbn = isbn.strip()  # clave única

    @property
    def titulo(self) -> str:
        return self.titulo_autor[0]

    @property
    def autor(self) -> str:
        return self.titulo_autor[1]

    def __str__(self) -> str:
        return f"ISBN: {self.isbn} | {self.titulo} - {self.autor} ({self.categoria})"

    def __repr__(self) -> str:
        return f"Libro(titulo={self.titulo!r}, autor={self.autor!r}, categoria={self.categoria!r}, isbn={self.isbn!r})"