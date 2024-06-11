def anadir_libro(biblioteca):
    while True:
        titulo = input('Ingrese el título del libro: ').lower()
        if not titulo:
            print('El campo no puede quedar vacío!!')
        else:
            break
    
    control = True
    while control:
        autor = input('Ingrese el autor del libro: ').lower()
        if not autor:
            print('El campo no puede quedar vacío!!')
        else:
            control = False
    
    while True:
        try:
            anyo = int(input('Ingrese el año de publicación del libro: '))
            break
        except ValueError:
            print('Introduzca un valor correcto para el año de publicación')
    
    biblioteca.append({'titulo' : titulo , 'autor' : autor , 'año' : anyo})
    print('Libro añadido con éxito!!')