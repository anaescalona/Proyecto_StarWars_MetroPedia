import os
import csv
from Planets import Planets 
from Movil import Movil,Starships,Vehicles
from Weapon import Weapon
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
            if len(m_name) > 0 or m_name is not ' ':
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n El nombre de la misión debe contener por lo menos un caracter...\n')

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'''
|----------------------------------------------------------------------------------------------|
La mision está registrada con el nombre "{m_name}"
|----------------------------------------------------------------------------------------------|             
''')


#ESCOGER PLANETA DE LA MISION

        print('\nEscoge el planeta de la misión:\n')

        archivo = os.path.join('csv', 'planets.csv')

        while True:

            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)
                        
                # Lee y muestra cada fila como un diccionario, presenta la lista de opciones enumeradas.
                for indice,row in enumerate(reader):
                    print(f'{indice+1} - {row['name']}')

            option_planet=input("""\nEscriba el numero del Planeta de destino:
---> """)
            if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Ingrese un número válido...\n')

        os.system('cls' if os.name == 'nt' else 'clear')

        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['id']== option_planet:
                    planeta1=Planets(row['diameter'],row['rotation_period'],row['orbital_period'],row['gravity'],row['population'],row['climate'],row['terrain'],row['surface_water'],'','',row['name'],'')

        print(f'''
|----------------------------------------------------------------------------------------------|
Se ha registrado el planeta "{planeta1.name}"
|----------------------------------------------------------------------------------------------|             
''')

        
#ESCOGER NAVE PARA LA MISION

        print('\nEscoge, de la lista, la nave que utilizará en la misión:\n')

        while True:
            archivo = os.path.join('csv', 'starships.csv')
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)
                
                lista_naves=[]
                for row in reader:
                    lista_naves.append(row['name'])

            paginar_lista(lista_naves)

            option_starship=input("""\nEscriba el nombre de la nave a utilizar:
---> """)

            if option_starship in lista_naves:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Ingrese un número válido...\n')
        
        os.system('cls' if os.name == 'nt' else 'clear')

        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row['name']== option_starship:
                    nave1=Starships(row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['crew'],row['passengers'],row['max_atmosphering_speed'],row['hyperdrive_rating'],row['MGLT'],row['cargo_capacity'],row['consumables'],'','',row['name'],'',row['starship_class'],row['pilots'])


        print(f'''
|----------------------------------------------------------------------------------------------|
Se ha registrado la nave "{nave1.name}"
|----------------------------------------------------------------------------------------------|             
''')


#ESCOGER 7 ARMAS PARA LA MISION

        contador=1
        print(f'\nEscoge, de la lista, el arma que utilizará en la misión (disponible {8-contador} armas):\n')
        for i in range(1,8):
            
            armas_elegidas=[]

            while True:
                archivo = os.path.join('csv', 'Weapons.csv')
                with open(archivo, mode='r') as file:
                    reader = csv.DictReader(file)
                    
                    lista_armas=[]
                    for row in reader:
                        lista_armas.append(row['name'])

                paginar_lista(lista_armas)

                option_weapon=input("""\nEscriba el nombre del arma a utilizar:
---> """)
                if option_weapon in lista_armas:

                    break

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Ingrese un número válido...\n')
            
            os.system('cls' if os.name == 'nt' else 'clear')

            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['name']== option_weapon:
                        armas_elegidas.append(Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films']))
                        arma=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

            arma.mostrar_att()

            if contador == 7:
                break

            response=input('''
Si desea avanzar pulse enter, si desea elegir otra arma escribe "0"
---> ''')
            if response == "":
                break

            elif response == "0":
                contador+=1
                print(f'\nEscoge, de la lista, el arma que utilizará en la misión (disponible {8-contador} armas):\n')

            else:
                print("Comando no reconocido.")

        print(armas_elegidas)

        input("""Integrantes de la mision:
---> """)
        Mision(m_name,planeta1,)

def mostrar_pagina(lista, pagina, elementos_por_pagina=15):
    inicio = pagina * elementos_por_pagina
    fin = inicio + elementos_por_pagina
    
    for indice,i in enumerate(range(inicio, min(fin, len(lista)))):
        print(f'{indice+1} - {lista[i]}')

def paginar_lista(lista):
    elementos_por_pagina = 15
    pagina = 0
    total_paginas = (len(lista) - 1) // elementos_por_pagina + 1

    while True:
        print('\nEscribe "atras" para retroceder, "sig" para avanzar o pulse enter para seleccionar: \n')
        print(f"Página {pagina + 1} de {total_paginas}")
        mostrar_pagina(lista, pagina, elementos_por_pagina)

        comando =  input("""
---> """)
        
        if comando == 'atras':
            if pagina > 0:
                pagina -= 1
        elif comando == 'sig':
            if pagina < total_paginas - 1:
                pagina += 1
        elif comando == '':
            break
        else:
            print("Comando no reconocido.")


def main():
    mision = Mision(None,None,None,None,None)
    mision.construir()
main()