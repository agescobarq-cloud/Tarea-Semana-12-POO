# Sistema de Gestión de Biblioteca Digital

Proyecto desarrollado para la **Semana 12** de la asignatura de Programación Orientada a Objetos.  
Implementa un sistema de biblioteca digital utilizando **arquitectura por capas** (modelos, servicios y punto de entrada), respetando estrictamente la separación de responsabilidades.

## Objetivo del proyecto

Crear un sistema de gestión de biblioteca digital que aplique correctamente:

- Programación Orientada a Objetos (POO)
- Arquitectura en capas (models – servicios – main)
- Encapsulamiento
- Buenas prácticas de diseño y separación de lógica de negocio

## Estructura del proyecto

biblioteca_app/
├── models/                    # Solo entidades / datos (sin lógica de negocio)
│   ├── libro.py
│   └── usuario.py
├── servicios/                 # Lógica de negocio y reglas del sistema
│   └── biblioteca_servicio.py
├── main.py                    # Punto de entrada + menú interactivo en consola
└── README.md

## Tecnologías y requisitos cumplidos

- Lenguaje: **Python 3**
- Estructuras de datos obligatorias utilizadas:
  - `tuple` → para almacenar título + autor (inmutable)
  - `list` → lista de libros prestados por usuario
  - `dict` → catálogo de libros disponibles (clave: ISBN)
  - `set` → control de IDs de usuarios únicos
- Separación estricta entre:
  - Modelos (solo atributos y getters básicos)
  - Servicios (toda la lógica de negocio)
  - Interfaz (menú en `main.py`)

## Funcionalidades implementadas

1. Agregar libro al catálogo  
2. Quitar libro del catálogo (solo si no está prestado)  
3. Registrar usuario  
4. Dar de baja usuario (solo si no tiene libros prestados)  
5. Prestar libro a un usuario  
6. Devolver libro  
7. Buscar libros por:
   - Título (parcial)
   - Autor (parcial)
   - Categoría (exacta)
8. Listar todos los libros disponibles  
9. Listar libros prestados a un usuario específico
