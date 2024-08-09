import csv
from Clases.Movil import Starships
import matplotlib.pyplot as plt

class Parte_F:
    def __init__(self, filename):
        """
        Inicializa la clase Parte_F, cargando los datos desde el archivo CSV y crea objetos Starships.
        
        :param filename: Ruta del archivo CSV que contiene los datos de las naves estelares.
        """
        self.filename = filename
        self.starships = []
        self.crear_starships()

    def crear_starships(self):
        """
        Carga los datos del archivo CSV y crea objetos Starships para cada fila de datos.
        Los datos se almacenan en la lista 'starships'.
        """
        with open(self.filename, 'r') as csvfile:
            lector = csv.reader(csvfile)
            next(lector)  
            for columna in lector:
                model = columna[2]
                manufacturer = columna[3]
                cost_in_credits = float(columna[4]) if columna[4] else 0.0
                length = float(columna[5]) if columna[5] else 0.0
                crew = int(columna[7]) if columna[7] else 0
                passengers = int(columna[8]) if columna[8] else 0
                max_atmosphering_speed = float(columna[6]) if columna[6] else 0.0
                hyperdrive_rating = float(columna[11]) if columna[11] else 0.0
                MGLT = float(columna[12]) if columna[12] else 0.0
                cargo_capacity = float(columna[9]) if columna[9] else 0.0
                consumables = columna[10] if columna[10] else '' 
                name = columna[1]
                starship_class = columna[13]
                pilots = [pilot.strip() for pilot in columna[14].split(',')] if columna[14] else []
                
                starship = Starships(model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, name, starship_class, pilots)
                self.starships.append(starship) 

    def get_starships(self):
        """
        Devuelve la lista de naves estelares creadas.
        
        :return: Lista de objetos Starships.
        """
        return self.starships

    def mostrar_grafico(self, titulo, naves_seleccionadas):
        """
        Crea un gráfico comparativo basado en la característica seleccionada para las naves estelares,
        y muestra los valores de cada nave en el gráfico.
        
        :param titulo: El título del gráfico que indica la característica a comparar.
        :param naves_seleccionadas: Lista de naves estelares seleccionadas para la comparación.
        """
        names = [starship.name for starship in naves_seleccionadas]
        values = []
        if titulo == "Longitud de la nave":
            values = [starship.length for starship in naves_seleccionadas]
        elif titulo == "Capacidad de carga":
            values = [starship.cargo_capacity for starship in naves_seleccionadas]
        elif titulo == "Clasificación de hiperimpulsor":
            values = [starship.hyperdrive_rating for starship in naves_seleccionadas]
        elif titulo == "MGLT (Modern Galactic Light Time)":
            values = [starship.MGLT for starship in naves_seleccionadas]

        plt.figure(figsize=(10, 6))
        bars = plt.bar(names, values)
        plt.xlabel("Nave")
        plt.ylabel(titulo)
        plt.title(titulo)
        plt.xticks(rotation=90)
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2,yval+1000,f'{yval:.2f}',ha='center',va='bottom',rotation=90)
        plt.tight_layout()
        plt.show()


    def menu(self):
        """
        Función principal que maneja el menú y las opciones del usuario para crear gráficos comparativos.
        """
        print('\n------------------------------------------------------------')
        print("Bienvenido al Comparador de naves de StarWars MetroPedia")
        print("A continuación podrá elegir sus características a comparar:")

        while True:
            print()
            print("Seleccione una opción para crear un gráfico comparativo:")
            print("1. Longitud de la nave")
            print("2. Capacidad de carga")
            print("3. Clasificación de hiperimpulsor")
            print("4. MGLT (Modern Galactic Light Time)")
            print("5. Salir al menú pricipal")
            print('------------------------------------------------------------')
            try:
                opcion = int(input("Ingrese el número de la opción: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue

            if opcion == 1:
                titulo = "Longitud de la nave"
            elif opcion == 2:
                titulo = "Capacidad de carga"
            elif opcion == 3:
                titulo = "Clasificación de hiperimpulsor"
            elif opcion == 4:
                titulo = "MGLT (Modern Galactic Light Time)"
            elif opcion == 5:
                print("Volver al menú principal")
                break
            else:
                print("Opción inválida")
                continue

            naves_seleccionadas = []
            for starship in self.starships:
                if titulo == "Longitud de la nave" and starship.length != 0:
                    naves_seleccionadas.append(starship)
                elif titulo == "Capacidad de carga" and starship.cargo_capacity != 0:
                    naves_seleccionadas.append(starship)
                elif titulo == "Clasificación de hiperimpulsor" and starship.hyperdrive_rating != 0:
                    naves_seleccionadas.append(starship)
                elif titulo == "MGLT (Modern Galactic Light Time)" and starship.MGLT != 0:
                    naves_seleccionadas.append(starship)

            print(f"\nSeleccione las naves que desea comparar para {titulo}:")
            for i, starship in enumerate(naves_seleccionadas):
                print(f"{i + 1}. {starship.name}")
            seleccionadas = []

            while True:
                seleccion = input("\nIngrese el número de la nave (o 'fin' para terminar, 'todas' para seleccionar todas): ")
                if seleccion.lower() == 'fin':
                    break

                if seleccion.lower() == 'todas':
                    seleccionadas = naves_seleccionadas
                    break

                try:
                    indice = int(seleccion) - 1
                    if 0 < indice < len(naves_seleccionadas):
                        seleccionadas.append(naves_seleccionadas[indice])
                    else:
                        print("Índice inválido")

                except ValueError:
                    print("Entrada inválida")

            if len(seleccionadas) < 2:
                print("Debe seleccionar al menos 2 naves")
                continue

            
            self.mostrar_grafico(titulo, seleccionadas)

            

def main():
    """
    Función principal que inicia el programa.
    """
    filename = 'csv/starships.csv'
    parte_f = Parte_F(filename)
    parte_f.menu()

if __name__ == "__main__":
    main()
