def mostrar_menu_1(peliculas, seres_vivos, planetas):
    while True:
        print('Bienvenido a la StarWiki')
        print("Seleccione la opcion en la que desea ingresar:")
        print('1) Lista de Películas de la saga')
        print('2) Lista de las especies de seres vivos de la saga')
        print('3) Lista de planetas')
        print('4) Buscar personaje')
        print('5) Volver al menu principal')

        opcion = int(input('Ingrese el numero de la opcion deseada: '))
        if opcion == 1:
            peliculas.mostrar_peliculas()
        elif opcion == 2:
            seres_vivos.show_species()
        elif opcion == 3:
            planetas.show_planetas()
        elif opcion == 4:
            planetas.show_planetas()
        elif opcion == 4:
            print('Volviendo a menu principal...')
            break
        else:
            print('Opcion Invalida')

def mostrar_menu_2(personajes):

                print('Bienvenido al buscador de Personajes')
                busqueda = input("Ingrese el nombre del personaje que desees buscar: ")
                personajes.getCharactersByName(busqueda)