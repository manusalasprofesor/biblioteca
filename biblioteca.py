from modulos.screen import clear_screen, pause_screen
from modulos.add_book import anadir_libro
from modulos.search_book import buscar_libros_por_autor
from modulos.delete_book import eliminar_libro
from modulos.show_book import mostrar_libros

# Programa principal
def gestionar_biblioteca(biblioteca):
    
    while True:
        clear_screen()
        print('''
            Menú de opciones:
            1. Añadir un nuevo libro
            2. Mostrar todos los libros
            3. Buscar libros por autor
            4. Eliminar un libro
            5. Salir
        ''')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            # pass
            clear_screen()
            anadir_libro(biblioteca)
            pause_screen()
        elif opcion == '2':
            # pass
            clear_screen()
            mostrar_libros(biblioteca)
            pause_screen()
        elif opcion == '3':
            # pass
            clear_screen()
            buscar_libros_por_autor(biblioteca)
            pause_screen()
        elif opcion == '4':
            # pass
            clear_screen()
            eliminar_libro(biblioteca)
            pause_screen()
        elif opcion == '5':
            print('Terminando el programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida')
            pause_screen()

if __name__ == '__main__':
    biblioteca = []
    gestionar_biblioteca(biblioteca)