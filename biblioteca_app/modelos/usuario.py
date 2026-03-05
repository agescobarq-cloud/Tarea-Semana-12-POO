from typing import List
from modelos.libro import Libro


class Usuario:
    def __init__(self, id_usuario: str, nombre: str):
        self.id_usuario = id_usuario.strip()
        self.nombre = nombre.strip()
        # Lista de libros actualmente prestados
        self.libros_prestados: List[Libro] = []

    def prestar_libro(self, libro: Libro) -> None:
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro: Libro) -> bool:
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return True
        return False

    def tiene_libro_prestado(self, isbn: str) -> bool:
        return any(libro.isbn == isbn for libro in self.libros_prestados)

    def __str__(self) -> str:
        return f"ID: {self.id_usuario} | {self.nombre} | Libros prestados: {len(self.libros_prestados)}"

    def __repr__(self) -> str:
        return f"Usuario(id={self.id_usuario!r}, nombre={self.nombre!r})"