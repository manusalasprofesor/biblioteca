def mostrar_libros(biblioteca):
    if biblioteca:
        print('Libros en la Biblioteca')   
        for libro in biblioteca:
            print(f'- Título: {libro['titulo'].capitalize()}, Autor: {libro['autor'].title()}, Año de publicación: {libro['año']}')
    else:
        print('No hay libros en la biblioteca!!')