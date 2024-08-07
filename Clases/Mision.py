import os
import csv
class Mision:
    def __init__(self, name, planet, spacecraft, weapons, personas):
        self.m_name=name
        self.planet=planet
        self.spacecraft=spacecraft
        self.weapons=weapons
        self.personas=personas

    def modify(self):
        self.m_name=input()
        self.planet=input()
        self.spacecraft=input()
        self.weapons=input()
        self.personas=input()
    
        
    def construir(self):
        
        print(f'Bienvenido, Escoja su equipo tactico para la mision...')

  
        while True:
            m_name=input("""Nombre de la mision:
---> """)
            if len(m_name) > 0:
                break
            else:
                print('\n El nombre de la misión debe contener por lo menos un caracter...\n')

        print('Escoge el planeta de la mision:')

        archivo = os.path.join('csv', 'planets.csv')
        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Lee y muestra cada fila como un diccionario
            for indice,row in enumerate(reader):
                print(f'{indice+1} - {row['name']}')

        while True:
            option_planet=input("""Escriba el numero del Planeta de destino:
---> """)
            if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:
                break
            else:
                print('Ingrese un número válido...')

        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id']== option_planet:
                    planeta=row['name']
        print(planeta)
        input("""Nave a utilizar:
---> """)
        input("""Arma a utilizar:
---> """)
        input("""Integrantes de la mision:
---> """)
        Mision(m_name,planeta,)

def main():
    mision = Mision(None,None,None,None,None)
    mision.construir()
main()