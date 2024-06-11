def eliminar_libro(biblioteca):
    control = True
    while control:
        titulo = input('Ingrese el título del libro a eliminar: ').lower()
        if not titulo:
            print('El campo no puede quedar vacío!!')
        else:
            control = False

    for libro in biblioteca:
        if libro['titulo'] == titulo:
            biblioteca.remove(libro)
            print('Libro eliminado con éxito!!')
            return
    print('No se encontró el libro con el título especificado!')