from Mision import menu_misiones
from funciones_menuABCD import carga_api, Match_Menu_Parte1
from menu_EFG import menu_efg

class App:

    def __init__(self):
        '''
        Inicializa la clase `App` y carga los datos desde la API.

        Llama a la función `carga_api` para obtener los datos necesarios para el funcionamiento de la aplicación.
        '''

        self.peliculas, self.seres_vivos, self.personajes, self.planetas, self.lista_peliculas_saga, self.lista_seres_vivos, self.lista_personajes, self.lista_planetas, self.lista_vehiculos, self.lista_startships = carga_api()

    def menu_principal(self):
        """
        Muestra el menú principal y gestiona la navegación entre diferentes opciones.

        Dependiendo de la opción seleccionada, se invoca la función correspondiente.
        """
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
    2) Estadisticas StarWars
    3) Emprende tu propia mision
    4) Salir del programa
    |--------------------------------------------------|
              
        ''')

            try:
                opcion = int(input("Ingrese el número de la opción: "))
            except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
        
            if opcion == 1:
                Match_Menu_Parte1(self.peliculas, self.seres_vivos, self.personajes, self.planetas, self.lista_peliculas_saga, self.lista_seres_vivos, self.lista_personajes, self.lista_planetas)
                continue
            elif opcion == 2:
                menu_efg()
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
    