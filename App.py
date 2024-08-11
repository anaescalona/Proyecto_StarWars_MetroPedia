from A_Peliculas import A_Peliculas
from B_Seres_vivos import B_Seres_vivos
from C_Planetas import C_Planetas
from D_Personajes import D_Personajes
from prueba_menu import mostrar_menu_1
from prueba_menu import mostrar_menu_2
from Parte_E import Parte_E
from Parte_F import Parte_F
from Mision import Mision, menu_misiones

class App:


    def menu_principal(self):
        while True: 
            print('''
              
             REPUBLICA BOLIVARIANA DE VENEZUELA 
                UNIVERSIDAD METROPOLITANA 
                   FACULTAD INGENIERIA 
                 ALGORITMOS Y PROGRAMACION 
              
    --------------------------------------------------
                STAR WARS METROPEDIA              
    --------------------------------------------------
    1) StarWiki (Peliculas, Especies, Planetas, Personajes)
    2) Estadisticas de naves espaciales
    3) Emprende tu propia mision
    4) Salir del programa
    --------------------------------------------------
              
        ''')

            try:
                    opcion = int(input("Ingrese el número de la opción: "))
            except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
        
            if opcion == 1:
                continue
            elif opcion == 2:
                parte_f = Parte_F()
                parte_f.menu()
                continue
            elif opcion == 3:
                menu_misiones()
                continue
            elif opcion == 4:
                print('''
        --------------------------------------------------                      
                          ADIOS 
                            Y
                    QUE LA FUERZA TE ACOMPAÑE
        --------------------------------------------------                    
                        ''')
                break


def main():
    app = App()
    app.menu_principal()

if __name__ == "__main__":
    main()
    