import csv
from Clases.Movil import Starships
import matplotlib.pyplot as plt

class Graficos:
    starships = []
    filename = 'csv/starships.csv'

    def Parte_F(self):
        self.crear_starships()
        
        print("Bienvenido al Comparador de naves de StarWars MetroPedia")
        print("A continuacion podrá elegir  sus caracteristicas a comparar:\n")

        print("\nSeleccione una opción para crear un gráfico comparativo:")
        print("1. Longitud de la nave")
        print("2. Capacidad de carga")
        print("3. Clasificación de hiperimpulsor")
        print("4. MGLT (Modern Galactic Light Time)")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            self.comparar_longitud()
        elif opcion == 2:
            self.comparar_capacidad_carga()
        elif opcion == 3:
            self.comparar_clasificacion_hiperimpulsor()
        elif opcion == 4:
            self.comparar_MGLT()
        else:
            print("Opción inválida")

    def crear_starships(self):
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
                Graficos.starships.append(starship) 

    def mostrar_starships(self):
        for i, starship in enumerate(Graficos.starships):
            print(f"{i+1}. {starship.name}")

    def comparar_longitud(self):
        self.seleccionar_naves("Longitud de la nave")

    def comparar_capacidad_carga(self):
        self.seleccionar_naves("Capacidad de carga")

    def comparar_clasificacion_hiperimpulsor(self):
        self.seleccionar_naves("Clasificación de hiperimpulsor")

    def comparar_MGLT(self):
        self.seleccionar_naves("MGLT (Modern Galactic Light Time)")

    def seleccionar_naves(self, titulo):
        print(f"\nSeleccione las naves que desea comparar para {titulo}:")
        for i, starship in enumerate(Graficos.starships):
            print(f"{i+1}. {starship.name}")

        naves_seleccionadas = []
        while True:
            seleccion = input("Ingrese el número de la nave (o 'fin' para terminar): ")
            if seleccion.lower() == 'fin':
                break
            try:
                indice = int(seleccion) - 1
                if indice >= 0 and indice < len(Graficos.starships):
                    naves_seleccionadas.append(Graficos.starships[indice])
                else:
                    print("Índice inválido")
            except ValueError:
                print("Entrada inválida")

        if len(naves_seleccionadas) < 2:
            print("Debe seleccionar al menos 2 naves")
            return

        self.mostrar_grafico(titulo, naves_seleccionadas)

    def mostrar_grafico(self, titulo, naves_seleccionadas):
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

        plt.bar(names, values)
        plt.xlabel("Nave")
        plt.ylabel(titulo)
        plt.title(titulo)
        plt.show()

def main():
    graficos = Graficos()
    graficos.Parte_F()

if __name__ == "__main__":
    main()