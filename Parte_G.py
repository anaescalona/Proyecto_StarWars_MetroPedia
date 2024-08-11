import csv
import numpy as np
import pandas as pd
from scipy import stats
from Clases.Movil import Starships

class Parte_G:
    def __init__(self):
        """
        Inicializa Parte_G con los datos de las naves estelares desde un archivo CSV.
        """
        self.filename = 'csv/starships.csv'
        self.starships = []
        self.cargar_naves()

    def cargar_naves(self):
        """
        Carga los datos del archivo CSV y crea objetos Starships para cada fila de datos del CSV.
        """
        with open(self.filename, 'r') as csvfile:
            lector = csv.reader(csvfile)
            next(lector)  # Salta el encabezado
            for columna in lector:
                model = columna[2]
                manufacturer = columna[3]
                cost_in_credits = float(columna[4]) if columna[4] else 0.0
                length = float(columna[5]) if columna[5] else 0.0
                crew = int(columna[7]) if columna[7] else 0
                passengers = int(columna[8]) if columna[8] else 0
                max_atmosphering_speed = float(columna[6]) if columna[6] else 0.0
                hiperdrive_rating = float(columna[11]) if columna[11] else 0.0
                MGLT = float(columna[12]) if columna[12] else 0.0
                cargo_capacity = float(columna[9]) if columna[9] else 0.0
                consumables = columna[10] if columna[10] else ''
                name = columna[1]
                starship_class = columna[13]
                pilots = [pilot.strip() for pilot in columna[14].split(',')] if columna[14] else []

                starship = Starships(model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hiperdrive_rating, MGLT, cargo_capacity, consumables, name, '', starship_class, pilots)
                self.starships.append(starship)

    def obtener_estadisticas_por_clase(self):
        """
        Calcula estadísticas básicas para las naves agrupadas por clase.
        """
        data_by_class = {}

        for ship in self.starships:
            starship_class = ship.starships_class
            # Asegúrate de que starship_class sea una cadena
            if not isinstance(starship_class, str):
                print(f"Advertencia: starship_class no es una cadena. Valor: {starship_class}")
                continue

            if starship_class not in data_by_class:
                data_by_class[starship_class] = {
                    'Clasif Hiperimpulsor': [],
                    'MGLT': [],
                    'Veloc Máx en Atmósfera': [],
                    'Costo (en créditos)': []
                }
            
            if ship.hiperdrive_rating > 0:
                data_by_class[starship_class]['Clasif Hiperimpulsor'].append(ship.hiperdrive_rating)
            if ship.MGLT > 0:
                data_by_class[starship_class]['MGLT'].append(ship.MGLT)
            if ship.max_atmosphering_speed > 0:
                data_by_class[starship_class]['Veloc Máx en Atmósfera'].append(ship.max_atmosphering_speed)
            if ship.cost_in_credits > 0:
                data_by_class[starship_class]['Costo (en créditos)'].append(ship.cost_in_credits)

        return data_by_class

    def calcular_estadisticas(self, values):
        """
        Calcula estadísticas básicas de una lista de valores.
        """
        if not values:
            return {
                'Promedio': '---',
                'Moda': '---',
                'Máximo': '---',
                'Mínimo': '---'
            }

        promedio = np.mean(values) if len(values) > 0 else '---'

        # Calcular la moda
        moda = '---'
        try:
            mode_result = stats.mode(values)
            if isinstance(mode_result.mode, np.ndarray):
                moda = mode_result.mode[0] if len(mode_result.mode) > 0 else '---'
            else:
                moda = mode_result.mode
        except Exception as e:
            moda = '---'
            print(f"Error calculando la moda: {e}")

        maximo = np.max(values) if len(values) > 0 else '---'
        minimo = np.min(values) if len(values) > 0 else '---'

        return {
            'Promedio': promedio,
            'Moda': moda,
            'Máximo': maximo,
            'Mínimo': minimo
        }

    def mostrar_estadisticas(self, categoria):
        """
        Muestra las estadísticas de las naves estelares por clase para una categoría específica.
        """
        estadisticas = self.obtener_estadisticas_por_clase()

        data = {
            'Clase de Nave': [],
            'Promedio': [],
            'Moda': [],
            'Máximo': [],
            'Mínimo': []
        }

        # Ajustar los nombres de las categorías para que coincidan con los utilizados en el DataFrame
        nombre_categoria = {
            'Clasif Hiperimpulsor': 'Clasif Hiperimpulsor',
            'MGLT': 'MGLT',
            'Veloc Máx en Atmósfera': 'Veloc Máx en Atmósfera',
            'Costo (en créditos)': 'Costo (en créditos)'
        }

        for ship_class, data_stats in estadisticas.items():
            values = data_stats.get(categoria, [])
            stats_values = self.calcular_estadisticas(values)

            data['Clase de Nave'].append(ship_class)
            data['Promedio'].append(stats_values.get('Promedio', '---'))
            data['Moda'].append(stats_values.get('Moda', '---'))
            data['Máximo'].append(stats_values.get('Máximo', '---'))
            data['Mínimo'].append(stats_values.get('Mínimo', '---'))

        df = pd.DataFrame(data)
        print(f"\nEstadísticas de Naves por Clase para {nombre_categoria.get(categoria, categoria)}:")
        print(df.to_string(float_format=lambda x: f'{x:.2f}' if isinstance(x, (int, float)) else x))

    def menu(self):
        """
        Función principal que maneja el menú para la selección de estadísticas.
        """
        while True:
            print('''
        |-----------------------------------------------------------|
          Bienvenido al Comparador Estadístico de Naves Espaciales
        |-----------------------------------------------------------|
        A continuación podrá seleccionar la categoría de datos para 
        visualizar estadísticas:

        1) Clasificación de Hiperimpulsor
        2) MGLT
        3) Velocidad Máxima en Atmósfera
        4) Costo en Créditos
        5) Volver al anterior menu
        |-----------------------------------------------------------|
    ''')
            try:
                opcion_categoria = int(input("Ingrese una opción: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue

            if opcion_categoria == 5:
                print("\nVolviendo al menu de Estadisticas Starwars\n")
                break

            categoria = ''
            if opcion_categoria == 1:
                categoria = 'Clasif Hiperimpulsor'
            elif opcion_categoria == 2:
                categoria = 'MGLT'
            elif opcion_categoria == 3:
                categoria = 'Veloc Máx en Atmósfera'
            elif opcion_categoria == 4:
                categoria = 'Costo (en créditos)'
            else:
                print("Opción inválida")
                continue

            self.mostrar_estadisticas(categoria)
            
            input('\nPara volver presione la tecla "Enter"')
            print()

def main():
    comparador = Parte_G()  
    comparador.menu()

if __name__ == "__main__":
    main()
