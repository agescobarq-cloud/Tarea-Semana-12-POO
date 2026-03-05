from typing import Dict, List, Optional
from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    def __init__(self):
        # Diccionario: ISBN → Libro   (únicos por ISBN)
        self.libros_disponibles: Dict[str, Libro] = {}
        
        # Conjunto de IDs de usuarios únicos
        self.ids_usuarios: set[str] = set()
        
        # Diccionario: id_usuario → Usuario
        self.usuarios: Dict[str, Usuario] = {}

    # ── Gestión de libros ────────────────────────────────────────
    def agregar_libro(self, titulo: str, autor: str, categoria: str, isbn: str) -> bool:
        if isbn in self.libros_disponibles:
            print(f"Ya existe un libro con ISBN {isbn}")
            return False
        
        libro = Libro(titulo, autor, categoria, isbn)
        self.libros_disponibles[isbn] = libro
        print(f"Libro agregado: {libro}")
        return True

    def quitar_libro(self, isbn: str) -> bool:
        if isbn not in self.libros_disponibles:
            print(f"No se encontró libro con ISBN {isbn}")
            return False
        
        # Verificar que no esté prestado
        for usuario in self.usuarios.values():
            if usuario.tiene_libro_prestado(isbn):
                print(f"No se puede eliminar: el libro {isbn} está prestado.")
                return False
        
        del self.libros_disponibles[isbn]
        print(f"Libro {isbn} eliminado del catálogo.")
        return True

    # ── Gestión de usuarios ──────────────────────────────────────
    def registrar_usuario(self, id_usuario: str, nombre: str) -> bool:
        if id_usuario in self.ids_usuarios:
            print(f"Ya existe un usuario con ID {id_usuario}")
            return False
        
        usuario = Usuario(id_usuario, nombre)
        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)
        print(f"Usuario registrado: {usuario}")
        return True

    def dar_baja_usuario(self, id_usuario: str) -> bool:
        if id_usuario not in self.usuarios:
            print(f"No existe usuario con ID {id_usuario}")
            return False
        
        if self.usuarios[id_usuario].libros_prestados:
            print(f"No se puede dar de baja: el usuario tiene libros prestados.")
            return False
        
        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"Usuario {id_usuario} dado de baja.")
        return True

    # ── Préstamos y devoluciones ─────────────────────────────────
    def prestar_libro(self, id_usuario: str, isbn: str) -> bool:
        if id_usuario not in self.usuarios:
            print(f"Usuario {id_usuario} no encontrado.")
            return False
        
        if isbn not in self.libros_disponibles:
            print(f"Libro {isbn} no encontrado en el catálogo.")
            return False
        
        libro = self.libros_disponibles[isbn]
        
        if self.usuarios[id_usuario].tiene_libro_prestado(isbn):
            print(f"El usuario ya tiene prestado el libro {isbn}.")
            return False
        
        # Simulamos que se presta (eliminamos de disponibles)
        del self.libros_disponibles[isbn]
        self.usuarios[id_usuario].prestar_libro(libro)
        print(f"Libro prestado → {libro.titulo} a {self.usuarios[id_usuario].nombre}")
        return True

    def devolver_libro(self, id_usuario: str, isbn: str) -> bool:
        if id_usuario not in self.usuarios:
            print(f"Usuario {id_usuario} no encontrado.")
            return False
        
        usuario = self.usuarios[id_usuario]
        
        # Buscamos el libro en los prestados del usuario
        libro_prestado = next((lib for lib in usuario.libros_prestados if lib.isbn == isbn), None)
        
        if not libro_prestado:
            print(f"El usuario no tiene prestado el libro {isbn}.")
            return False
        
        usuario.devolver_libro(libro_prestado)
        # Volvemos a agregar al catálogo disponible
        self.libros_disponibles[isbn] = libro_prestado
        print(f"Libro devuelto: {libro_prestado.titulo} por {usuario.nombre}")
        return True

    # ── Búsquedas ────────────────────────────────────────────────
    def buscar_por_titulo(self, texto: str) -> List[Libro]:
        texto = texto.lower().strip()
        return [lib for lib in self.libros_disponibles.values() if texto in lib.titulo.lower()]

    def buscar_por_autor(self, texto: str) -> List[Libro]:
        texto = texto.lower().strip()
        return [lib for lib in self.libros_disponibles.values() if texto in lib.autor.lower()]

    def buscar_por_categoria(self, categoria: str) -> List[Libro]:
        categoria = categoria.lower().strip()
        return [lib for lib in self.libros_disponibles.values() if lib.categoria.lower() == categoria]

    # ── Listados ─────────────────────────────────────────────────
    def listar_libros_disponibles(self) -> None:
        if not self.libros_disponibles:
            print("No hay libros disponibles.")
            return
        print("\nLibros disponibles:")
        for libro in self.libros_disponibles.values():
            print(f"  - {libro}")

    def listar_libros_prestados_usuario(self, id_usuario: str) -> None:
        if id_usuario not in self.usuarios:
            print(f"Usuario {id_usuario} no encontrado.")
            return
        
        usuario = self.usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"{usuario.nombre} no tiene libros prestados.")
            return
        
        print(f"\nLibros prestados a {usuario.nombre}:")
        for libro in usuario.libros_prestados:
            print(f"  - {libro}")