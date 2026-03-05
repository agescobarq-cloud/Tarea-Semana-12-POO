from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    print("\n" + "="*50)
    print("   SISTEMA DE BIBLIOTECA DIGITAL")
    print("="*50)
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libros")
    print("8. Listar libros disponibles")
    print("9. Listar libros prestados de un usuario")
    print("0. Salir")
    print("="*50)


def main():
    biblioteca = BibliotecaServicio()

    # Datos de ejemplo (opcional, para pruebas rápidas)
    biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "978-0307474728")
    biblioteca.agregar_libro("1984", "George Orwell", "Distopía", "978-0451524935")
    biblioteca.agregar_libro("El principito", "Antoine de Saint-Exupéry", "Infantil", "978-0156012195")
    biblioteca.registrar_usuario("U001", "María Pérez")
    biblioteca.registrar_usuario("U002", "Juan López")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("¡Gracias por usar el sistema!")
            break

        elif opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            id_usuario = input("ID de usuario: ")
            nombre = input("Nombre: ")
            biblioteca.registrar_usuario(id_usuario, nombre)

        elif opcion == "4":
            id_usuario = input("ID de usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID de usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID de usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            print("\nBuscar por:")
            print("  a) Título")
            print("  b) Autor")
            print("  c) Categoría")
            sub_op = input("→ ").lower()
            texto = input("Texto a buscar: ").strip()

            if sub_op == "a":
                resultados = biblioteca.buscar_por_titulo(texto)
            elif sub_op == "b":
                resultados = biblioteca.buscar_por_autor(texto)
            elif sub_op == "c":
                resultados = biblioteca.buscar_por_categoria(texto)
            else:
                print("Opción inválida.")
                continue

            if not resultados:
                print("No se encontraron resultados.")
            else:
                print("\nResultados:")
                for libro in resultados:
                    print(f"  - {libro}")

        elif opcion == "8":
            biblioteca.listar_libros_disponibles()

        elif opcion == "9":
            id_usuario = input("ID de usuario: ")
            biblioteca.listar_libros_prestados_usuario(id_usuario)

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()