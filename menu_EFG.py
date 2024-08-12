from Parte_E import Parte_E
from Parte_F import Parte_F
from Parte_G import Parte_G

def menu_efg():
    """
    Función principal que gestiona el menú interactivo para la aplicación de estadísticas Star Wars.

    Dependiendo de la opción seleccionada por el usuario, se invoca el método correspondiente en las instancias 
    de las clases Parte_E, Parte_F, o Parte_G.

    El menú se mantiene en un bucle hasta que el usuario elige volver al menú principal.
    """
        
    parte_e = Parte_E()  
    parte_f = Parte_F()  
    parte_g = Parte_G()  

    while True: 
        print('''
        |--------------------------------------------------|
               ¡Bienvenido a Estadísticas StarWars!              
        |--------------------------------------------------|
        Aquí podrás ver una serie de estadísticas diferentes

        1) Gráfico de Cantidad de personajes nacidos en cada planeta.
        2) Gráficos comparativos de naves espaciales.
        3) Estadísticas sobre naves espaciales.
        4) Volver al Menú principal.
        |--------------------------------------------------|
        ''')

        try:
            opcion = int(input("Ingrese el número de la opción: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue

        if opcion == 1:
            parte_e.mostrar_grafico()
        elif opcion == 2:
            parte_f.menu()
        elif opcion == 3:
            parte_g.menu()
        elif opcion == 4:
            print('Volviendo al Menú principal...')
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

