import os
import csv
from Planets import Planets 
from Movil import Movil,Starships,Vehicles
class Mision:
    def __init__(self, name, planet, starship, weapons, characters):
        self.m_name=name
        self.planet=planet
        self.starship=starship
        self.weapons=weapons
        self.characters=characters


    def modify(self):
        self.m_name=input()
        self.planet=input()
        self.spacecraft=input()
        self.weapons=input()
        self.personas=input()
    
        
    def construir(self):

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'Bienvenido, Escoja su equipo táctico para la misión...')

#ESCOGER NOMBRE DE MISION

        while True:
            
            m_name=input("""\nEscribe el nombre para la misión:
---> """)
            if len(m_name) > 0:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n El nombre de la misión debe contener por lo menos un caracter...\n')

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'\nSe registrará la misión con el nombre "{m_name}"\n')

        while True:

            continue1=input('''
0 - Continuar. 
1 - Cambiar el nombre de la misión.
---> ''')
        
            os.system('cls' if os.name == 'nt' else 'clear')

        
            if continue1 == '1':

                while True:
            
                    m_name=input("""\nEscribe el nuevo nombre para la misión:
---> """)
                    if len(m_name) > 0:
                        break

                    else:

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print('\n El nombre de la misión debe contener por lo menos un caracter...\n')
                break

            elif continue1 == '0':

                break

            elif continue1 is not '0':

                print('\n Por favor, escriba el número de una de las opciones presentadas...\n')

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'\nSe registrará la misión con el nombre "{m_name}"\n')

#ESCOGER PLANETA DE LA MISION

        print('\nEscoge el planeta de la misión:\n')

        archivo = os.path.join('csv', 'planets.csv')
        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Lee y muestra cada fila como un diccionario, presenta la lista de opciones enumeradas.
            for indice,row in enumerate(reader):
                print(f'{indice+1} - {row['name']}')

        while True:
            option_planet=input("""\nEscriba el numero del Planeta de destino:
---> """)
            if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Ingrese un número válido...')

        os.system('cls' if os.name == 'nt' else 'clear')

        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['id']== option_planet:
                    planeta1=Planets(row['diameter'],row['rotation_period'],row['orbital_period'],row['gravity'],row['population'],row['climate'],row['terrain'],row['surface_water'],'','',row['name'],'')


        print(f'\nEl planeta elegido es "{planeta1.name}"\n')

        while True:

            continue2=input('''
0 - Continuar. 
1 - Cambiar el planeta de la misión.
---> ''')
        
            os.system('cls' if os.name == 'nt' else 'clear')

        
            if continue2 == '1':

                while True:

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)
                        # Lee y muestra cada fila como un diccionario, presenta la lista de opciones enumeradas.
                        for indice,row in enumerate(reader):
                            print(f'{indice+1} - {row['name']}')
            
                    option_planet=input("""\nEscoge el nuevo planeta para la misión:
---> """)
                    if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:

                        with open(archivo, mode='r') as file:
                                    reader = csv.DictReader(file)

                                    for row in reader:
                                        if row['id']== option_planet:
                                            planeta1=Planets(row['diameter'],row['rotation_period'],row['orbital_period'],row['gravity'],row['population'],row['climate'],row['terrain'],row['surface_water'],'','',row['name'],'')

                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...')
                break

            elif continue2 == '0':

                break

            elif continue2 is not '0':

                print('\n Por favor, escriba el número de una de las opciones presentadas...\n')

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'\nEl planeta elegido es "{planeta1.name}"\n')

#ESCOGER NAVE PARA LA MISION

        print('\nEscoge la nave que utilizará en la misión:\n')

        while True:
            archivo = os.path.join('csv', 'starships.csv')
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)
                
                # Lee y muestra cada fila como un diccionario, presenta la lista de opciones enumeradas.
                for indice,row in enumerate(reader):
                    print(f'{indice+1} - {row['name']}')

            option_starship=input("""\nEscriba el numero de la nave a utilizar:
---> """)
            numstr_list = [str(num) for num in range(1, 61)]

            if option_starship in numstr_list:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Ingrese un número válido...\n')
        
        os.system('cls' if os.name == 'nt' else 'clear')

        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['id']== option_planet:
                    nave1=Starships(row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['crew'],row['passengers'],row['max_atmosphering_speed'],row['hyperdrive_rating'],row['MGLT'],row['cargo_capacity'],row['consumables'],'','',row['name'],'',row['starship_class'],row['pilots'])


        print(f'\nLa nave que utilizará es "{nave1.name}"\n')


#ESCOGER 7 ARMAS PARA LA MISION

        input("""Arma a utilizar:
---> """)
        input("""Integrantes de la mision:
---> """)
        Mision(m_name,planeta1,)

def main():
    mision = Mision(None,None,None,None,None)
    mision.construir()
main()