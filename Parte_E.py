import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from Clases.People import People


class Parte_E:
    def __init__(self):
        """
        Inicializa la Parte_E, cargando los datos desde el archivo CSV y creando objetos People.
        
        :param filename: Ruta del archivo CSV que contiene los datos de los personajes.
        """
        self.filename = 'csv/characters.csv'  
        self.people = []
        self.cargar_characters()

    def cargar_characters(self):
        """
        Carga los datos del archivo CSV y crea objetos People para cada fila de datos.
        Los datos se almacenan en la lista 'people'.
        """
        with open(self.filename, 'r') as csvfile:
            lector = csv.reader(csvfile)
            next(lector)  
            for columna in lector:
                id = columna[0]
                name = columna[1]
                species = columna[2]  
                gender = columna[3]
                height = columna[4]
                mass = columna[5]
                hair_color = columna[6]
                eye_color = columna[7]
                skin_color = columna[8]
                birth_year = columna[9]
                homeworld = columna[10]
                year_died = columna[11]  
                description = columna[12]  
                
                person = People(height, mass, hair_color, skin_color, eye_color, birth_year, gender, created='', edited='', name=name, homeworld=homeworld, id=id, url='')
                self.people.append(person)

    def contar_personaje_por_planeta(self):
        """
        Cuenta la cantidad de personajes nacidos en cada planeta, excluyendo los personajes cuyo planeta es "Unknown".
        
        :return: Un diccionario con los planetas como claves y la cantidad de personajes como valores.
        """
        planet_counts = defaultdict(int)
        for person in self.people:
            if person.homeworld and person.homeworld.lower() != 'unknown':  
                planet_counts[person.homeworld] += 1
        return dict(planet_counts)

    def mostrar_grafico(self):
        """
        Genera un gráfico que muestra la cantidad de personajes nacidos en cada planeta.
        """
        planet_counts = self.contar_personaje_por_planeta()
        
        if not planet_counts:
            print("No hay datos de personajes.")
            return

        planets = list(planet_counts.keys())
        counts = list(planet_counts.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(planets, counts, color='skyblue')
        plt.xlabel("Planeta")
        plt.ylabel("Cantidad de Personajes")
        plt.title("Cantidad de Personajes Nacidos en Cada Planeta")
        plt.xticks(rotation=90)  
        plt.tight_layout()  
        plt.show()

def main():
    """
    Función principal que inicia el programa para generar el gráfico de personajes por planeta.
    """
    
    people_graph = Parte_E()
    people_graph.mostrar_grafico()

if __name__ == "__main__":
    main()