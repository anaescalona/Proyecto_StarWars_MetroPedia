import os
import csv
from Planets import Planets 
from Movil import Starships
from Weapon import Weapon
from People import People
class Mision:
    def __init__(self, name, planet, starship, weapons, characters):
        self.name=name
        self.planet=planet
        self.starship=starship
        self.weapons=weapons
        self.characters=characters
          
    def construir(self):

        os.system('cls' if os.name == 'nt' else 'clear')

        print('Bienvenido al menú para creación de misiones ...')

        contador_misiones=1

        lista_misiones=[]

        while True:

    #ESCOGER NOMBRE DE MISION

            while True:
                
                m_name=input("""\nEscribe el nombre para la misión:
    ---> """)
                if len(m_name) > 0 or m_name != ' ':
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
                    print('Ingrese un número o valor válido...\n')

            os.system('cls' if os.name == 'nt' else 'clear')

            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:
                        if row['id']== option_planet:
                            planeta=Planets(row['diameter'],row['rotation_period'],row['orbital_period'],row['gravity'],row['population'],row['climate'],row['terrain'],row['surface_water'],'','',row['name'],'')


            print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado el planeta "{planeta.name}"
    |----------------------------------------------------------------------------------------------|             
    ''')

            
    #ESCOGER NAVE PARA LA MISION

            print('\nEscoge la página donde está la nave que utilizará en la misión:\n')

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
                    print('Ingrese un número o nombre válido...\n')
            
            os.system('cls' if os.name == 'nt' else 'clear')

            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['name']== option_starship:
                        nave=Starships(row['model'],row['manufacturer'], row['cost_in_credits'], row['length'], row['crew'], row['passengers'], row['max_atmosphering_speed'], row['hyperdrive_rating'], row['MGLT'], row['cargo_capacity'], row['consumables'],'','', row['name'],'', row['starship_class'],row['pilots'])


            print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado la nave "{nave.name}"
    |----------------------------------------------------------------------------------------------|             
    ''')


    #ESCOGER 7 ARMAS PARA LA MISION

            contador=1
            print(f'\nEscoge, de la lista, el arma que utilizará en la misión (disponible {8-contador} armas):\n')

            armas_elegidas=[]

            while True:

                while True:
                    archivo = os.path.join('csv', 'weapons.csv')
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

                if contador == 1:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma1=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma1.mostrar_att()
                    
                    armas_elegidas.append(arma1.name)

                if contador == 2:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma2=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma2.mostrar_att()
                    
                    armas_elegidas.append(arma2.name)

                if contador == 3:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma3=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma3.mostrar_att()
                    
                    armas_elegidas.append(arma3.name)

                if contador == 4:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma4=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma4.mostrar_att()
                    
                    armas_elegidas.append(arma4.name)

                if contador == 5:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma5=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma5.mostrar_att()
                    
                    armas_elegidas.append(arma5.name)

                if contador == 6:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma6=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma6.mostrar_att()
                    
                    armas_elegidas.append(arma6.name)

                if contador == 7:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_weapon:
                                arma7=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma7.mostrar_att()
                    
                    armas_elegidas.append(arma7.name)

                    break

                response=input('''
    Si desea avanzar pulse enter, si desea elegir otra arma escribe "1"
    ---> ''')
                if response == "":
                    break

                elif response == "1":
                    contador+=1
                    print(f'\nEscoge, de la lista, el arma que utilizará en la misión (disponible {8-contador} armas):\n')

                else:
                    print("Comando no reconocido.")

            os.system('cls' if os.name == 'nt' else 'clear')

            if len(armas_elegidas) > 1:

                print(f'''
    |----------------------------------------------------------------------------------------------|
    Se han registrados las armas:
    ''')    
                for i in armas_elegidas:
                    print(f'''
            "{i}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
            elif len(armas_elegidas) == 1:
                print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado el arma "{armas_elegidas[0]}"
    |----------------------------------------------------------------------------------------------|             
    ''')    
            else:
                print('No se han registrado armas...')
            
    #ESCOGER INTEGRANTES PARA LA MISION

            contador=1
            print(f'\nEscoge, de la lista, al integrante que te acompañará en la misión (disponible {8-contador} integrantes):\n')

            integrantes_elegidos=[]

            while True:

                while True:
                    archivo = os.path.join('csv', 'characters.csv')
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)
                        
                        lista_personajes=[]
                        for row in reader:
                            lista_personajes.append(row['name'])

                    paginar_lista(lista_personajes)

                    option_character=input("""\nEscriba el nombre del personaje que te va a acompañar:
    ---> """)
                    if option_character in lista_personajes:
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...\n')
                
                os.system('cls' if os.name == 'nt' else 'clear')

                if contador == 1:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona1=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona1.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona1.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 2:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona2=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona2.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona2.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 3:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona3=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona3.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona3.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 4:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona4=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona4.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona4.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 5:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona5=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona5.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona5.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 6:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona6=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona6.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona6.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 7:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['name']== option_character:
                                persona7=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona7.name)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona7.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                    break

                response=input('''
    Si desea avanzar pulse enter, si desea elegir otro integrante escribe "1"
    ---> ''')
                if response == "":
                    break

                elif response == "1":
                    contador+=1
                    print(f'\nEscoge, de la lista, al integrante que te acompañará en la misión (disponible {8-contador} integrantes):\n')

                else:
                    print("Comando no reconocido.")

            os.system('cls' if os.name == 'nt' else 'clear')

            if len(integrantes_elegidos) > 1:

                print(f'''
    |----------------------------------------------------------------------------------------------|
    Se han registrados como los integrantes a:
    ''')    
                for i in integrantes_elegidos:
                    print(f'''
            "{i}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
            elif len(integrantes_elegidos) == 1:
                print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{integrantes_elegidos[0]}"
    |----------------------------------------------------------------------------------------------|             
    ''')    
            else:
                print('No se han registrado integrantes...')
            



            mision=Mision(m_name,planeta,nave,armas_elegidas,integrantes_elegidos)

            lista_misiones.append(mision)


            print(f'''
    |----------------------------------------------------------------------------------------------|
    ¡Se ha registrado la misión exitosamente!
    |----------------------------------------------------------------------------------------------|
                        ''')

            respuesta=input(f"""
    Si desea avanzar pulse enter, si desea registar otra misión escribe "1": (quedan {5-contador_misiones} misiones disponibles para registrar)
    ---> """)
            
            contador_misiones+=1
            
            if respuesta == "":
                os.system('cls' if os.name == 'nt' else 'clear')

                nombre_misiones = [mision.name for mision in lista_misiones]

                print(f'''
    |----------------------------------------------------------------------------------------------|
    Las siguientes misiones se han registrado exitosamente:
    ''')    
                for i in nombre_misiones:
                    print(f'''
            "{i}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')

                break
            
            elif respuesta == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Puede registar los datos para la nueva misión ...')

            elif contador_misiones == 5:

                os.system('cls' if os.name == 'nt' else 'clear')

                nombre_misiones = [mision.name for mision in lista_misiones]

                print(f'''
    |----------------------------------------------------------------------------------------------|
    Las siguientes misiones se han registrado exitosamente:
    ''')    
                for i in nombre_misiones:
                    print(f'''
            "{i}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
                break

            else:
                print("Comando no reconocido.")

        return lista_misiones
    
    def modificar(self, lista_misiones):

        os.system('cls' if os.name == 'nt' else 'clear')

        nombre_misiones = [mision.name for mision in lista_misiones]

        print(f'''
        
        Bienvenido al menú para modificar misiones...
    |----------------------------------------------------------------------------------------------|
    Las siguientes misiones están registradas :
    ''')    
        for i in nombre_misiones:
            print(f'''
            "{i}"''') 
        print(f'''
    |----------------------------------------------------------------------------------------------|''')


def mostrar_pagina(lista, pagina, elementos_por_pagina=10):
    inicio = pagina * elementos_por_pagina
    fin = inicio + elementos_por_pagina
    
    for indice,i in enumerate(range(inicio, min(fin, len(lista)))):
        print(f'{indice+1} - {lista[i]}')

def paginar_lista(lista):
    elementos_por_pagina = 10
    pagina = 0
    total_paginas = (len(lista) - 1) // elementos_por_pagina + 1

    while True:

        print('\nEscribe "1" para abrir la siguiente pagina o pulse enter para seleccionar: \n')
        print(f"Página {pagina + 1} de {total_paginas}")
        mostrar_pagina(lista, pagina, elementos_por_pagina)

        comando =  input("""
---> """)
        
        if comando == '1':
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

def prueba():
    archivo = os.path.join('csv', 'starships.csv')
    with open(archivo, mode='r') as file:
        reader = csv.DictReader(file)
                
        lista_naves=[]
        for row in reader:
            lista_naves.append(row['name'])

    paginar_lista(lista_naves)

