import os
import csv
from Clases.Movil import Starships
from Clases.Weapon import Weapon
from Clases.People import People
from Clases.Planets import Planets
class Mision:
    def __init__(self, name, planet, starship, weapons, characters):
        self.name=name
        self.planet=planet
        self.starship=starship
        self.weapons=weapons
        self.characters=characters
          
    def construir():

        os.system('cls' if os.name == 'nt' else 'clear')

        print('¡Bienvenido al menú para creación de misiones!\n')

        contador_misiones=0

        lista_misiones=[]

        mision_registrada=False

        while True:

    #ESCOGER NOMBRE DE MISION
            
            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER NOMBRE PARA LA MISIÓN
                         
    Escribe "salir" si desea abandandonar el menú de creación de misiones.
    Escribe cualquier caracter si desea continuar.
                   
    
    ---> """)
            
            if salida == "salir":

                break

            while True:
                
                os.system('cls' if os.name == 'nt' else 'clear')

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

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER PLANETA PARA LA MISIÓN
                         
    Escribe "salir" si desea abandandonar el menú de creación de misiones.
    Escribe cualquier caracter si desea continuar.
    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida == "salir":

                break
            
            os.system('cls' if os.name == 'nt' else 'clear')

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

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER NAVE PARA LA MISIÓN
                         
    Escribe "salir" si desea abandandonar el menú de creación de misiones.
    Escribe cualquier caracter si desea continuar.
    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida == "salir":

                break

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'\nEscoge, de la lista, la nave que utilizará en la misión:\n')

            while True:
                archivo = os.path.join('csv', 'starships.csv')
                with open(archivo, mode='r') as file:
                    reader = csv.DictReader(file)
                    
                    lista_naves=[]
                    for row in reader:
                        lista_naves.append(row['name'])

                pagina=paginar_lista(lista_naves)

                pagina*=10

                option_starship=int(input("""\nEscriba el número de la nave a utilizar:
    ---> """))

                if option_starship > 0 and option_starship < 11:

                    option_starship+=pagina
                    
                    option_starship=str(option_starship)

                    break

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Ingrese un número válido...\n')
            
            os.system('cls' if os.name == 'nt' else 'clear')

            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['id']== option_starship:
                        nave=Starships(row['model'],row['manufacturer'], row['cost_in_credits'], row['length'], row['crew'], row['passengers'], row['max_atmosphering_speed'], row['hyperdrive_rating'], row['MGLT'], row['cargo_capacity'], row['consumables'],'','', row['name'],'', row['starship_class'],row['pilots'])


            print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado la nave "{nave.name}"
    |----------------------------------------------------------------------------------------------|             
    ''')


    #ESCOGER HASTA 7 ARMAS PARA LA MISION

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER ARMAS PARA LA MISIÓN
                         
    Escribe "salir" si desea abandandonar el menú de creación de misiones.
    Escribe cualquier caracter si desea continuar.
    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida == "salir":

                break

            os.system('cls' if os.name == 'nt' else 'clear')

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

                    pagina=paginar_lista(lista_armas)

                    pagina*=10

                    option_weapon=int(input("""\nEscriba el número del arma a utilizar:
    ---> """))
                    if option_weapon > 0 and option_weapon < 11:

                        option_weapon+=pagina
                        
                        option_weapon=str(option_weapon)

                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...\n')
                
                os.system('cls' if os.name == 'nt' else 'clear')

                if contador == 1:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma1=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma1.mostrar_att()
                    
                    armas_elegidas.append(arma1)

                if contador == 2:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma2=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma2.mostrar_att()
                    
                    armas_elegidas.append(arma2)

                if contador == 3:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma3=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma3.mostrar_att()
                    
                    armas_elegidas.append(arma3)

                if contador == 4:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma4=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma4.mostrar_att()
                    
                    armas_elegidas.append(arma4)

                if contador == 5:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma5=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma5.mostrar_att()
                    
                    armas_elegidas.append(arma5)

                if contador == 6:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma6=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma6.mostrar_att()
                    
                    armas_elegidas.append(arma6)

                if contador == 7:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma7=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma7.mostrar_att()
                    
                    armas_elegidas.append(arma7)

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
            "{i.name}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
            elif len(armas_elegidas) == 1:
                print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado el arma "{armas_elegidas[0].name}"
    |----------------------------------------------------------------------------------------------|             
    ''')    
            else:
                print('No se han registrado armas...')
            
    #ESCOGER HASTA 7 INTEGRANTES PARA LA MISION

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER INTEGRANTES DE LA MISIÓN
                         
    Escribe "salir" si desea abandandonar el menú de creación de misiones.
    Escribe cualquier caracter si desea continuar.
    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida == "salir":

                break

            os.system('cls' if os.name == 'nt' else 'clear')

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

                    pagina=paginar_lista(lista_personajes)

                    pagina*=10

                    option_character=int(input("""\nEscribe el número del personaje a seleccionar:
    ---> """))
                    if option_character > 0 and option_character < 11:

                        option_character+=pagina
                        
                        option_character=str(option_character)
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...\n')
                
                os.system('cls' if os.name == 'nt' else 'clear')

                if contador == 1:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona1=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona1)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona1.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 2:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona2=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona2)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona2.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 3:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona3=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona3)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona3.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 4:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona4=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona4)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona4.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 5:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona5=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona5)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona5.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 6:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona6=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona6)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona6.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 7:
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona7=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                    integrantes_elegidos.append(persona7)

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
            "{i.name}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
            elif len(integrantes_elegidos) == 1:
                print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{integrantes_elegidos[0].name}"
    |----------------------------------------------------------------------------------------------|             
    ''')    
            else:
                print('No se han registrado integrantes...')
            
            mision=Mision(m_name,planeta,nave,armas_elegidas,integrantes_elegidos)

            lista_misiones.append(mision)

            contador_misiones+=1

            if contador_misiones == 5:

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


            print(f'''
    |----------------------------------------------------------------------------------------------|
    ¡Se ha registrado la misión exitosamente!
    |----------------------------------------------------------------------------------------------|
                        ''')

            respuesta=input(f"""
    |----------------------------------------------------------------------------------------------|
                                    FIN DEL MENÚ DE CREACIÓN DE MISIONES
                         
    Escribe "salir" si desea abandandonar el menú de creación de misiones.
    Escribe cualquier caracter si desea registrar otra misión.
    
    (quedan {5-contador_misiones} misiones disponibles para registrar)

    ---> """)
            
            if respuesta == "salir":

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
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Puede registar los datos para la nueva misión ...')
        
        mision_registrada=True

        return lista_misiones,mision_registrada
    
    def modificar(lista_misiones):

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            #SALIDA DEL MENÚ DE MODIFICAR MISIÓN

            salida=input("""
        ¡Bienvenido al menú para modificar misiones!
                         
    |----------------------------------------------------------------------------------------------|
                                    MODIFICAR MISIONES
                         
    Escribe "salir" si desea abandandonar el menú de modificación de misiones.
    Escribe cualquier caracter si desea continuar.
                   
    
    ---> """)
            
            if salida == "salir":

                break

            os.system('cls' if os.name == 'nt' else 'clear')


            #ELECCIÓN DE LA MISIÓN A MODIFICAR

            while True:

                nombre_misiones = [mision.name for mision in lista_misiones]

                while True:

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Las siguientes misiones están registradas :
            ''')    
                    for i in nombre_misiones:
                        print(f'''
        "{i}"''') 
                    print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
                    respuesta=input(f"""
            Escribe el nombre de la misión que desea modificar:
            ---> """)
                
                    for mision in lista_misiones:

                        #VALIDACIÓN DE RESPUESTA

                        if respuesta==mision.name:
                            m_modificada=mision
                        
                        
                    if respuesta in nombre_misiones:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Escribe el nombre de la misión a modificar correctamente, puede hacer uso de copiar y pegar.")

                #ELECCIÓN DEL ATRIBUTO DE MISION A MODIFICAR

                while True:

                    print(f'''
        |----------------------------------------------------------------------------------------------|
        Haz seleccionado la misión "{m_modificada.name}"
        |----------------------------------------------------------------------------------------------|

                1 - Modificar nombre.
                2 - Modificar planeta.
                3 - Modificar nave.
                4 - Modificar armas.
                5 - Modificar integrantes.
                6 - Regresar.
                                    ''')
                    
                    response=input("""Escribe el número de la opción que quiere ejecutar:
            ---> """)
                    
                    #VALIDACIÓN DE RESPUESTA.

                    if response in ["1","2","3","4","5","6"]:
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("Comando no reconocido.")

                #MODIFICAR NOMBRE A MISION

                if response == '1':

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
        |----------------------------------------------------------------------------------------------|
                            Modificar Nombre de misión "{m_modificada.name}"
            
        Escriba el nuevo nombre para la misión:''')
                        
                    new_name = input('''
            ---> ''')
                    m_modificada.name=new_name

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
        |----------------------------------------------------------------------------------------------|
        Se ha modificado el nombre de la misión, el nuevo nombre es "{m_modificada.name}"
        |----------------------------------------------------------------------------------------------|''')

                #MODIFICAR PLANETA A MISION

                elif response == '2':

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
            |----------------------------------------------------------------------------------------------|
                                    Modificar Planeta de la misión "{m_modificada.name}"

                ---> El planeta registrado es "{m_modificada.planet.name}"
        ''')
                    while True:
                        
                        archivo = os.path.join('csv', 'planets.csv')

                        with open(archivo, mode='r') as file:
                            reader = csv.DictReader(file)

                                # Lee y muestra cada fila como un diccionario, presenta la lista de opciones enumeradas.
                            for indice,row in enumerate(reader):
                                    print(f'{indice+1} - {row['name']}')

                        new_planet=input("""\nEscriba el numero del nuevo Planeta de destino (puede escribir "regresar" para retroceder)::
                ---> """)
                        if new_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:

                            os.system('cls' if os.name == 'nt' else 'clear')

                            with open(archivo, mode='r') as file:
                                reader = csv.DictReader(file)

                                for row in reader:
                                    if new_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:
                                        if row['id']== new_planet:
                                            planeta=Planets(row['diameter'],row['rotation_period'],row['orbital_period'],row['gravity'],row['population'],row['climate'],row['terrain'],row['surface_water'],'','',row['name'],'')

                            m_modificada.planet=planeta

                            print(f'''
            |----------------------------------------------------------------------------------------------|
            Se ha modificado el Planeta de la misión, el nuevo Planeta es "{planeta.name}"
            |----------------------------------------------------------------------------------------------|
            ''')

                            break

                        elif new_planet =="regresar":
                            break

                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ingrese un número o valor válido...\n')
                    
                #MODIFICAR NAVE A MISION

                elif response == '3':
                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
            |----------------------------------------------------------------------------------------------|
                                    Modificar nave de la misión "{m_modificada.name}"

                ---> La nave registrada es "{m_modificada.starship.name}"
        ''')

                    while True:

                        archivo = os.path.join('csv', 'starships.csv')
                        with open(archivo, mode='r') as file:
                            reader = csv.DictReader(file)
                                
                            lista_naves=[]
                            for row in reader:
                                lista_naves.append(row['name'])

                        pagina=paginar_lista(lista_naves)

                        pagina*=10

                        option_starship=int(input("""\nEscriba el número de la nueva nave (puede escribir "regresar" para retroceder):
        ---> """))

                        if option_starship > 0 and option_starship < 11:

                            option_starship+=pagina
                            
                            option_starship=str(option_starship)

                            os.system('cls' if os.name == 'nt' else 'clear')

                            with open(archivo, mode='r') as file:
                                reader = csv.DictReader(file)

                                for row in reader:
                                    if row['id']== option_starship:
                                        nave=Starships(row['model'],row['manufacturer'], row['cost_in_credits'], row['length'], row['crew'], row['passengers'], row['max_atmosphering_speed'], row['hyperdrive_rating'], row['MGLT'], row['cargo_capacity'], row['consumables'],'','', row['name'],'', row['starship_class'],row['pilots'])

                            m_modificada.starship=nave


                            print(f'''
                |----------------------------------------------------------------------------------------------|
                Se ha modificado la nave de la misión, la nueva nave es "{nave.name}"
                |----------------------------------------------------------------------------------------------|
                ''')
                            break

                        elif option_starship == "regresar":

                            break

                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ingrese un número válido...\n')
                    
                #MODIFICAR ARMAS A MISION

                elif response == '4':
                    os.system('cls' if os.name == 'nt' else 'clear')

                    while True:
                        armas_elegidas=m_modificada.weapons

                        print(f'''
                |----------------------------------------------------------------------------------------------|
                                Modificar armas de la misión "{m_modificada.name}"
                                                
                ---> Las armas registradas son:
                    ''')
                        for i in armas_elegidas:
                            print(f'''
                    "{i.name}" ''')

                        respuesta=input('''

            1 - Eliminar arma
            2 - Agregar arma
            0 - Regresar
                                        
        (Hay un límite de 7 armas, si desea cambiar un arma, primero elimínela y luego agregue el nuevo arma.)
            
            Escribe el número de la opción a ejecutar:
                ---> ''') 
                    
                        #OPCION ELIMINAR ARMA

                        if respuesta == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')

                            while True:

                                print(f'''
                |----------------------------------------------------------------------------------------------|
                                Eliminar armas de la misión "{m_modificada.name}"
                                                
                ---> Las armas registradas son:
                    ''')
                                for i in armas_elegidas:
                                    print(f'''
                    "{i.name}" ''')
                        
                                arma_eliminar=input('''
            Escribe el nombre del arma a eliminar (puede escribir "regresar" para retroceder):
                ---> ''') 
                                for arma in armas_elegidas:
                                    if arma_eliminar == arma.name:
                                        arma_eliminar=arma
                        
                                if arma_eliminar in armas_elegidas:
                                    armas_elegidas.remove(arma_eliminar)

                                    os.system('cls' if os.name == 'nt' else 'clear')

                                    print(f'''
        |-------------------------------------------------------------------------------------------------------------------------|
        Se ha registrado el cambio en la lista de armas, se ha eliminado la siguiente arma "{arma_eliminar.name}"
        |-------------------------------------------------------------------------------------------------------------------------|
                ''')
                                    break

                                elif arma_eliminar=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('Por favor ingrese el nombre de un arma registrada.')

                        #OPCION AGREGAR ARMA (AVISO DE MAXIMO DE ARMAS REGISTRADAS)

                        elif respuesta == '2' and len(armas_elegidas)>=7:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ya existen 7 armas registradas, por favor elimine algún arma primero.\n')
                        
                        #OPCION AGREGAR ARMA

                        elif respuesta == '2' and len(armas_elegidas)<7:

                            os.system('cls' if os.name == 'nt' else 'clear')

                            while True:

                                print(f'''
                |----------------------------------------------------------------------------------------------|
                                Agregar armas de la misión "{m_modificada.name}"
                                        
                                        ''')
                                
                                while True:
                                    archivo = os.path.join('csv', 'weapons.csv')
                                    with open(archivo, mode='r') as file:
                                        reader = csv.DictReader(file)
                                        
                                        lista_armas=[]
                                        for row in reader:
                                            lista_armas.append(row['name'])

                                    pagina=paginar_lista(lista_armas)

                                    pagina*=10

                                    new_weapon=int(input("""\nEscriba el número de la nueva arma (puede escribir "regresar" para retroceder):
        ---> """))
                                    if new_weapon in ['1','2','3','4','5','6','7','8','9','10']:
                                        new_weapon=int(new_weapon)

                                    elif new_weapon == 'regresar':
                                        break

                                    if new_weapon > 0 and new_weapon < 11:

                                        new_weapon+=pagina
                                        
                                        new_weapon=str(new_weapon)

                                        break

                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print('Ingrese un número válido...\n')

                                if new_weapon=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                os.system('cls' if os.name == 'nt' else 'clear')

                                with open(archivo, mode='r') as file:
                                    reader = csv.DictReader(file)

                                    for row in reader:
                                        if row['id']== new_weapon:
                                            arma=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                                arma.mostrar_att()
                                
                                armas_elegidas.append(arma)

                                if len(armas_elegidas)>=7:
                                    print('Se encuentran registradas 7 armas para la misión.')
                                    break

                        #OPCION REGRESAR

                        elif respuesta == '0':
                            break

                #MODIFICAR INTEGRANTES DE MISION

                elif response == '5':
                     
                    os.system('cls' if os.name == 'nt' else 'clear')

                    while True:
                        integrantes_elegidos=m_modificada.characters

                        print(f'''
                |----------------------------------------------------------------------------------------------|
                                Modificar integrantes de la misión "{m_modificada.name}"
                                                
                ---> Los integrantes registrados son:
                    ''')
                        for i in integrantes_elegidos:
                            print(f'''
                    "{i.name}" ''')

                        respuesta=input('''

            1 - Eliminar personaje
            2 - Agregar personaje
            0 - Regresar
                                        
        (Hay un límite de 7 integrantes, si desea cambiar un integrante, primero elimínela y luego agregue al nuevo personaje.)
            
            Escribe el número de la opción a ejecutar:
                ---> ''') 
                    
                        #OPCION ELIMINAR INTEGRANTE

                        if respuesta == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')

                            while True:

                                print(f'''
                |----------------------------------------------------------------------------------------------|
                                Eliminar integrantes de la misión "{m_modificada.name}"
                                                
                ---> Los integrantes registrados son:
                    ''')
                                for i in integrantes_elegidos:
                                    print(f'''
                    "{i.name}" ''')
                        
                                integrante_eliminar=input('''
            Escribe el nombre del personaje a eliminar (puede escribir "regresar" para retroceder):
                ---> ''') 
                                for persona in integrante_eliminar:
                                    if integrante_eliminar == persona.name:
                                        integrante_eliminar=persona
                        
                                if integrante_eliminar in integrantes_elegidos:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    integrantes_elegidos.remove(integrante_eliminar)
                                    print(f'''
        |-------------------------------------------------------------------------------------------------------------------------|
        Se ha registrado el cambio en la lista de integrantes, se ha eliminado al integrante "{integrante_eliminar.name}"
        |-------------------------------------------------------------------------------------------------------------------------|
                ''')
                                    break

                                elif integrante_eliminar=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('Por favor ingrese el nombre de un integrante registrado.')

                        #OPCION AGREGAR INTEGRANTE (AVISO DE MAXIMO DE INTEGRANTES REGISTRADOS)

                        elif respuesta == '2' and len(integrantes_elegidos)>=7:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ya hay 7 integrantes en la misión, por favor elimine a alguno primero para agregar un personaje nuevo.\n')
                        
                        #OPCION AGREGAR INTEGRANTE

                        elif respuesta == '2' and len(integrantes_elegidos)<7:

                            os.system('cls' if os.name == 'nt' else 'clear')

                            while True:

                                print(f'''
                |----------------------------------------------------------------------------------------------|
                                Agregar integrantes para la misión "{m_modificada.name}"
                                        
                                        ''')
                                
                                while True:
                                    archivo = os.path.join('csv', 'characters.csv')
                                    with open(archivo, mode='r') as file:
                                        reader = csv.DictReader(file)
                                        
                                        lista_personas=[]
                                        for row in reader:
                                            lista_personas.append(row['name'])

                                    pagina=paginar_lista(lista_personas)

                                    pagina*=10

                                    new_character=input("""\nEscriba el número del nuevo personaje (puede escribir "regresar" para retroceder):
        ---> """)
                                    if new_character in ['1','2','3','4','5','6','7','8','9','10']:
                                        new_character=int(new_character)

                                    elif new_character == 'regresar':
                                        break

                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print('Ingrese un número válido...\n')


                                    if new_character > 0 and new_character < 11:

                                        new_character+=pagina
                                        
                                        new_character=str(new_character)

                                        break

                                if new_character=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                os.system('cls' if os.name == 'nt' else 'clear')

                                with open(archivo, mode='r') as file:
                                    reader = csv.DictReader(file)

                                    for row in reader:
                                        if row['id']== new_character:
                                            persona=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],row['id'],'')

                                integrantes_elegidos.append(persona)

                                print(f'''
        |-------------------------------------------------------------------------------------------------------------------------|
        Se ha registrado el cambio en la lista de integrantes, se ha agregado al integrante "{persona.name}"
        |-------------------------------------------------------------------------------------------------------------------------|
                ''')

                                if len(integrantes_elegidos)>=7:
                                    print('Ya se encuentran registrados 7 integrantes para la misión.')
                                    break

                        #OPCION REGRESAR

                        elif respuesta == '0':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break

                    #REGRESAR AL MENÚ DE SELECCIÓN DE MISIONES PARA MODIFICAR

                elif response == '6':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

        return lista_misiones

    def guardar(lista_misiones):
        print("por crear")

    def cargar():
        print("Por hacer")

def menu_misiones():

    mision_creada=False

    while True:

        #ELECCION DEL MENU A EJECUTAR.

        while True:
            print(f'''
|----------------------------------------------------------------------------------------------|
                ¡Bienvenido al menú de misiones del Star Wars Metropedia!
|----------------------------------------------------------------------------------------------|

            1 - Crear misiones.
            2 - Modificar misiones.
            3 - Guardar misiones.
            4 - Cargar misiones.
            5 - Salir.
                  
(Si ya ha creado misiones y selecciona "Crear misiones" estará eliminando las misiones construidas anteriormente.)
                                ''')
                
            response=input("""Escribe el número de la opción que quiere ejecutar:
---> """)
            #VALIDACION DE RESPUESTA.
            if response in ['1','2','3','4','5']:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Escribe un comando válido.")

        if response=='1':
            lista_misiones,mision_registrada=Mision.construir()
            if mision_registrada == True:
                mision_creada=True
            
        
        elif response=='2' and mision_creada==True:
            Mision.modificar(lista_misiones)
            lista_misiones=lista_misiones

        elif response == '2' and mision_creada==False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No posee ninguna misión creada, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión.')

        elif response == '3' and mision_creada==True:
            Mision.guardar(lista_misiones)

        elif response == '3' and mision_creada==False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No posee ninguna misión creada, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión.')

        elif response=='4':
            Mision.cargar(lista_misiones)

        elif response == '5':
            break
        
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

        print('\nEscribe "1" para ir la siguiente pagina, "0" para ir a la página anterior o pulse enter para seleccionar: \n')
        print(f"Página {pagina + 1} de {total_paginas}")
        mostrar_pagina(lista, pagina, elementos_por_pagina)

        comando =  input("""
---> """)
        
        if comando == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            if pagina < total_paginas - 1:
                pagina += 1
        
        elif comando == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            if pagina > 0:
                pagina -= 1

        elif comando == '':
            break
        else:
            print("Comando no reconocido.")
    return pagina


def prueba():
    Mision.cargar()


