import csv
from Clases.Movil import Starships

class Graficos:
    starships = []
    filename = 'csv/starships.csv'

    def Parte_F(self):
        self.crear_starships()
        
        print("Bienvenido al Comparador de naves de StarWars MetroPedia")
        print("A continuacion podrá elegir las naves que usted desee y sus caracteristicas a comparar:")




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

    
def main():
    app=Graficos()
    app.Parte_F()
main()