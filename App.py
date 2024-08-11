from Parte_F import Parte_F
from Mision import menu_misiones
from funciones_menuABCD import carga_api, Match_Menu_Parte1
import os 

class App:

    def __init__(self) -> None:
         self.peliculas, self.seres_vivos, self.personajes, self.planetas, self.lista_peliculas_saga, self.lista_seres_vivos, self.lista_personajes, self.lista_planetas, self.lista_vehiculos, self.lista_startships = carga_api()

    def menu_principal(self):
        while True: 
            print('''
              
             REPUBLICA BOLIVARIANA DE VENEZUELA 
                UNIVERSIDAD METROPOLITANA 
                   FACULTAD INGENIERIA 
                 ALGORITMOS Y PROGRAMACION 
              
    |--------------------------------------------------|
                  STAR WARS METROPEDIA              
    |--------------------------------------------------|
    1) StarWiki (Peliculas, Especies, Planetas, Personajes)
    2) Estadisticas de naves espaciales
    3) Emprende tu propia mision
    4) Salir del programa
    |--------------------------------------------------|
              
        ''')

            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                opcion = int(input("Ingrese el número de la opción: "))
            except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
        
            if opcion == 1:
                Match_Menu_Parte1(self.peliculas, self.seres_vivos, self.personajes, self.planetas, self.lista_peliculas_saga, self.lista_seres_vivos, self.lista_personajes, self.lista_planetas)
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
        |--------------------------------------------------|                      
                           ADIOS 
                             Y
                    QUE LA FUERZA TE ACOMPAÑE
        |--------------------------------------------------|                 
                        ''')
                break


def main():
    app = App()
    app.menu_principal()

if __name__ == "__main__":
    main()
    