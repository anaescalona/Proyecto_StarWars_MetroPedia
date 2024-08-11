from Parte_E import Parte_E
from Parte_F import Parte_F
from Parte_G import Parte_G

def menu_fgh():
    while True: 
            print('''
                    
    |--------------------------------------------------|
            Bienvenido a Estadisticas StarWars              
    |--------------------------------------------------|
    Aquí podras ver una serie de estadisticas diferentes
                  
    1) Grafico de Cantidad de personajes nacidos en cada planeta
    2) Graficos comparativos de naves epaciales
    3) Estadisticas sobre naves
    4) Volver al Menu principal
    |--------------------------------------------------|
              
        ''')

            try:
                opcion = int(input("Ingrese el número de la opción: "))
            except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
        
            if opcion == 1:
                parte_e=Parte_E()
                parte_e.mostrar_grafico()
                continue
            elif opcion == 2:
                parte_f = Parte_F()
                parte_f.menu()
                continue
            elif opcion == 3:
                parte_g=Parte_G
                parte_g.mostrar_estadisticas()
                continue
            elif opcion == 4:
                print('Volviendo al Menu principal...')
                break

menu_fgh()