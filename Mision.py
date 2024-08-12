import os
import csv
import re
from Clases.Movil import Starships
from Clases.Weapon import Weapon
from Clases.People import People
from Clases.Planets import Planets
class Mision:

    def __init__(self, name, planet, starship, weapons, characters):
        """FUNCION CONSTRUCTOR DE OBJETO MISION

        Atributos:

            name (str): nombre asignado a la mision
            planet (Planets): objeto planetas
            starship (Starships): objeto naves
            weapons (list): lista de objetos arma
            characters (list): lista de objetos personas
        """
        self.name=name
        self.planet=planet
        self.starship=starship
        self.weapons=weapons
        self.characters=characters

    def construir(lista_misiones):

        """FUNCION PARA CREAR MISIONES: Despliega un menu para que el usuario pueda crear misiones con un limite
        de hasta 5 misiones.
        
        return: lista_misiones(list), mision_registrada(bool): la funcion guarda la lista de misiones creadas
        y confirma si se lograron crear misiones con un valor verdadero o falso."""

        os.system('cls' if os.name == 'nt' else 'clear')

        print('¡Bienvenido al menú para creación de misiones!\n')

        contador_misiones=len(lista_misiones)

        mision_registrada=False

        while True:

            if contador_misiones == 5:

                """COMPROBACION DEL LIMITE DE 5 MISIONES"""

                os.system('cls' if os.name == 'nt' else 'clear')

                nombre_misiones = [mision.name for mision in lista_misiones]

                print(f'''
    |----------------------------------------------------------------------------------------------|
    Ya se encuentran registradas 5 misiones:
    ''')    
                for i in nombre_misiones:
                    print(f'''
            "{i}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                
                break

            """ESCOGER NOMBRE PARA MISION"""
            
            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER NOMBRE PARA LA MISIÓN

    Escribe cualquier caracter si desea continuar.                                              
    Escribe "salir" si desea abandandonar el menú de creación de misiones.

                   
    
    ---> """)
                   
            if salida.lower() == "salir":

                """SALIDA AL MENU PRINCIPAL DE MISIONES"""

                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')

            while True:

                m_name=input("""\nEscribe el nombre para la misión:
    ---> """)
                
                """VALIDACION PARA QUE EL NOMBRE SEA CADENA ALFANUMERICA"""

                patron = r'^[a-zA-Z0-9 ]+$'
                if re.match(patron, m_name) and m_name != ' ' and m_name != '  ' and m_name != '   ' and len(m_name)>0:
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\n El nombre de la misión debe contener por lo menos un caracter y ser alfanumérico...\n')

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'''
    |----------------------------------------------------------------------------------------------|
    La mision está registrada con el nombre "{m_name}"
    |----------------------------------------------------------------------------------------------|             
    ''')

            """ESCOGER PLANETA DE LA MISION"""

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER PLANETA PARA LA MISIÓN

    Escribe cualquier caracter si desea continuar.                                                
    Escribe "salir" si desea abandandonar el menú de creación de misiones.

    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida.lower() == "salir":

                """SALIDA AL MENU PRINCIPAL DE MISIONES"""

                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
            os.system('cls' if os.name == 'nt' else 'clear')

            archivo = os.path.join('csv', 'planets.csv')

            while True:
                
                with open(archivo, mode='r') as file:

                    """LECTURA DEL ARCHIVO CSV. DE PLANETAS"""

                    reader = csv.DictReader(file)

                    for indice,row in enumerate(reader):

                        """PRESENTA LA LISTA DE NOMBRES DE PLANETAS EN UNA PAGINA ENUMERADA
                        (la enumeracion coincide con el id del planeta)"""

                        print(f'{indice+1} - {row['name']}')

                option_planet=input("""\nEscriba el numero del Planeta de destino:
    ---> """)
    
                if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:

                    """VALIDACION DE LA RESPUESTA"""

                    break
                
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Ingrese un número o valor válido...\n')

            os.system('cls' if os.name == 'nt' else 'clear')

            with open(archivo, mode='r') as file:

                """CONVERSION DE LA RESPUESTA EN OBJETO PLANETA"""

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

            """ESCOGER NAVE PARA LA MISION"""

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER NAVE PARA LA MISIÓN

    Escribe cualquier caracter si desea continuar.                                                 
    Escribe "salir" si desea abandandonar el menú de creación de misiones.

    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
   
            if salida.lower() == "salir":

                """SALIDA AL MENU PRINCIPAL DE MISIONES"""

                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'\nEscoge, de la lista, la nave que utilizará en la misión:\n')

            while True:

                archivo = os.path.join('csv', 'starships.csv')

                with open(archivo, mode='r') as file:

                    """LECTURA DE ARCHIVO CSV. DE NAVES Y FORMACION DE LISTA NAVES"""

                    reader = csv.DictReader(file)
                    
                    lista_naves=[]
                    for row in reader:
                        lista_naves.append(row['name'])

                """PRESENTA LISTA NAVES EN PAGINAS"""

                pagina=paginar_lista(lista_naves)

                pagina*=10

                option_starship=input("""\nEscriba el número de la nave a utilizar:
    ---> """)
                
                if option_starship in ['1','2','3','4','5','6','7','8','9','10']:

                    """VALIDACION DE RESPUESTA"""

                    option_starship=int(option_starship)

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Ingrese un número válido...\n')

                if isinstance(option_starship,int) and option_starship > 0 and option_starship < 11:

                    """CONVERSION DE RESPUESTA AL ID DE NAVE"""

                    option_starship+=pagina
                    
                    option_starship=str(option_starship)

                    break

            os.system('cls' if os.name == 'nt' else 'clear')

            with open(archivo, mode='r') as file:

                """CONVERSION DE LA RESPUESTA EN OBJETO NAVE"""

                reader = csv.DictReader(file)

                for row in reader:
                    if row['id']== option_starship:
                        nave=Starships(row['model'],row['manufacturer'], row['cost_in_credits'], row['length'], row['crew'], row['passengers'], row['max_atmosphering_speed'], row['hyperdrive_rating'], row['MGLT'], row['cargo_capacity'], row['consumables'],row['name'],'', row['starship_class'],row['pilots'])

            print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado la nave "{nave.name}"
    |----------------------------------------------------------------------------------------------|             
    ''')


            """ESCOGER HASTA 7 ARMAS PARA LA MISION"""

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER ARMAS PARA LA MISIÓN

    Escribe cualquier caracter si desea continuar.                                                  
    Escribe "salir" si desea abandandonar el menú de creación de misiones.

    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida.lower() == "salir":

                """SALIDA AL MENU PRINCIPAL DE MISIONES"""

                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')

            contador=0
            print(f'\nEscoge, de la lista, el arma que utilizará en la misión (disponible {7-contador} armas):\n')

            armas_elegidas=[]

            while True:

                while True:

                    """LECTURA DEL ARCHIVO CSV. DE ARMAS Y FORMA LA LISTA DE ARMAS"""

                    archivo = os.path.join('csv', 'weapons.csv')
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)
                        
                        lista_armas=[]
                        for row in reader:
                            lista_armas.append(row['name'])

                    """ORGANIZA LISTA DE ARMAS EN PAGINAS"""

                    pagina=paginar_lista(lista_armas)

                    pagina*=10

                    option_weapon=input("""\nEscriba el número del arma a utilizar:
    ---> """)
                    
                    if option_weapon in ['1','2','3','4','5','6','7','8','9','10']:

                        """VALIDA LA RESPUESTA"""

                        option_weapon=int(option_weapon)

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...\n')

                    if isinstance(option_weapon,int) and option_weapon > 0 and option_weapon < 11:
                            
                            """TRANSFORMA RESPUESTA EN ID DE ARMA"""

                            option_weapon+=pagina
                            
                            option_weapon=str(option_weapon)

                            break
                
                os.system('cls' if os.name == 'nt' else 'clear')

                if contador == 0:

                    """CREA Y REGISTRA EL PRIMER OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma1=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma1.mostrar_att()
                    
                    armas_elegidas.append(arma1)

                if contador == 1:

                    """CREA Y REGISTRA EL SEGUNDO OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma2=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma2.mostrar_att()
                    
                    armas_elegidas.append(arma2)

                if contador == 2:

                    """CREA Y REGISTRA EL TERCER OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma3=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma3.mostrar_att()
                    
                    armas_elegidas.append(arma3)

                if contador == 3:

                    """CREA Y REGISTRA EL CUARTO OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma4=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma4.mostrar_att()
                    
                    armas_elegidas.append(arma4)

                if contador == 4:

                    """CREA Y REGISTRA EL QUINTO OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma5=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma5.mostrar_att()
                    
                    armas_elegidas.append(arma5)

                if contador == 5:

                    """CREA Y REGISTRA EL SEXTO OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma6=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma6.mostrar_att()
                    
                    armas_elegidas.append(arma6)

                if contador == 6:

                    """CREA Y REGISTRA EL SEPTIMO OBJETO DE ARMA EN LISTA DE ARMAS ELEGIDAS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_weapon:
                                arma7=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                    arma7.mostrar_att()
                    
                    armas_elegidas.append(arma7)

                    break
                
                contador+=1

                """AVANZA A ELEGIR INTEGRANTES"""

                response=input(f'''
    Si desea avanzar pulse enter, si desea elegir otra arma escribe "1".
    
    Puedes registrar {7-contador} armas más.
                               
    ---> ''')
                if response == "":
                    break

                elif response == "1":

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'\nEscoge, de la lista, el arma que utilizará en la misión (disponible {7-contador} armas):\n')

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')

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
            
            """ESCOGER HASTA 7 INTEGRANTES PARA LA MISION"""

            salida=input("""
    |----------------------------------------------------------------------------------------------|
                                    ESCOGER INTEGRANTES DE LA MISIÓN

    Escribe cualquier caracter si desea continuar.                                             
    Escribe "salir" si desea abandandonar el menú de creación de misiones.

    
    (Al salir del menú de creación de misiones no se guardará la información registrada de esta misión)
    
    ---> """)
            
            if salida.lower() == "salir":

                """SALIDA AL MENU PRINCIPAL DE MISIONES"""

                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')

            contador=0
            print(f'\nEscoge, de la lista, al integrante que te acompañará en la misión (disponible {7-contador} integrantes):\n')

            integrantes_elegidos=[]

            while True:

                while True:

                    """LEE ARCHIVO CSV. DE PERSONAJES Y CREA LISTA DE PERSONAJES"""

                    archivo = os.path.join('csv', 'characters.csv')
                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)
                        
                        lista_personajes=[]
                        for row in reader:
                            lista_personajes.append(row['name'])

                    """ORGANIZA LISTA DE PERSONAJES EN PAGINAS"""

                    pagina=paginar_lista(lista_personajes)

                    pagina*=10

                    option_character=int(input("""\nEscribe el número del personaje a seleccionar:
    ---> """))
                    
                    if option_character in ['1','2','3','4','5','6','7','8','9','10']:

                        """VALIDA LA RESPUESTA"""

                        option_character=int(option_character)

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...\n')

                    
                    if isinstance(option_character,int) and option_character > 0 and option_character < 11:

                        """CONVIERTE LA RESPUESTA EN ID DE PERSONAJE"""

                        option_character+=pagina
                        
                        option_character=str(option_character)
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Ingrese un número válido...\n')
                
                os.system('cls' if os.name == 'nt' else 'clear')

                if contador == 0:

                    """REGISTRA AL PRIMER PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona1=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona1)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona1.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 1:

                    """REGISTRA AL SEGUNDO PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona2=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona2)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona2.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 2:

                    """REGISTRA AL TERCER PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona3=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona3)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona3.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 3:

                    """REGISTRA AL CUARTO PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona4=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona4)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona4.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 4:

                    """REGISTRA AL QUINTO PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona5=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona5)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona5.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 5:

                    """REGISTRA AL SEXTO PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona6=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona6)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona6.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                if contador == 6:

                    """REGISTRA AL SEPTIMO PERSONAJE EN LISTA DE INTEGRANTES ELEGIDOS"""

                    with open(archivo, mode='r') as file:
                        reader = csv.DictReader(file)

                        for row in reader:
                            if row['id']== option_character:
                                persona7=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                    integrantes_elegidos.append(persona7)

                    print(f'''
    |----------------------------------------------------------------------------------------------|
    Se ha registrado como integrante a "{persona7.name}"
    |----------------------------------------------------------------------------------------------|
                        ''')

                    break

                contador+=1

                """AVANZA AL FINAL DE CREACION DE MISIONES"""

                response=input(f'''
    Si desea avanzar pulse enter, si desea elegir otro integrante escribe "1".
    
    Puedes registrar {7-contador} integrantes más.

    ---> ''')

                if response == "":
                    break

                elif response == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'\nEscoge, de la lista, al integrante que te acompañará en la misión (disponible {7-contador} integrantes):\n')

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
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
            
            """SE GUARDA EL OBJETO MISION"""

            mision=Mision(m_name,planeta,nave,armas_elegidas,integrantes_elegidos)

            """SE REGISTRA EN LISTA DE MISIONES"""

            lista_misiones.append(mision)

            contador_misiones+=1

            if contador_misiones == 5:

                """LIMITA LA CANTIDAD DE MISIONES A 5"""

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
            
            if respuesta.lower() == "salir":

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

        """FUNCION PARA MODIFICAR MISIONES: Despliega menu donde el usuario puede modificar las
          misiones registradas en lista_misiones
          
          return: lista_misiones(list): regresa la lista de misiones con las modificaciones actualizadas."""
        
        while True:

                os.system('cls' if os.name == 'nt' else 'clear')

                salida=input("""
            ¡Bienvenido al menú para modificar misiones!
                            
        |----------------------------------------------------------------------------------------------|
                                        MODIFICAR MISIONES

        Escribe cualquier caracter si desea continuar.                       
        Escribe "salir" si desea abandandonar el menú de modificación de misiones.

                    
        
        ---> """)
                
                if salida.lower() == "salir":

                    """SALIDA DEL MENÚ DE MODIFICAR MISIÓN"""

                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                os.system('cls' if os.name == 'nt' else 'clear')

                """ELECCIÓN DE LA MISIÓN A MODIFICAR"""

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
                
                    """VALIDACIÓN DE RESPUESTA"""

                    for mision in lista_misiones:

                        if respuesta==mision.name:
                            m_modificada=mision
                        
                    if respuesta in nombre_misiones:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Escribe el nombre de la misión a modificar correctamente, puede hacer uso de copiar y pegar.")

                """ELECCIÓN DEL ATRIBUTO DE MISION A MODIFICAR"""

                while True:

                    print(f'''
        |----------------------------------------------------------------------------------------------|
        Haz seleccionado la misión "{m_modificada.name}"
        |----------------------------------------------------------------------------------------------|

                0 - Eliminar misión.
                1 - Modificar nombre.
                2 - Modificar planeta.
                3 - Modificar nave.
                4 - Modificar armas.
                5 - Modificar integrantes.
                6 - Regresar.
                                    ''')
                    
                    response=input("""Escribe el número de la opción que quiere ejecutar:
            ---> """)
                    
                    if response in ["0","1","2","3","4","5","6"]:

                        """VALIDACIÓN DE RESPUESTA"""

                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("Comando no reconocido.")

                if response == '1':

                    """MODIFICAR NOMBRE A MISION"""

                    os.system('cls' if os.name == 'nt' else 'clear')
                    while True:
                        print(f'''
        |----------------------------------------------------------------------------------------------|
                            Modificar Nombre de misión "{m_modificada.name}"
            
        Escriba el nuevo nombre para la misión:''')
                        
                        new_name = input('''
            ---> ''')
                        
                        """VALIDACION DEL QUE NOMBRE SEA PERMITIDO"""

                        patron = r'^[a-zA-Z0-9 ]+$'
                        if re.match(patron, new_name) and new_name != ' ' and new_name != '  ' and new_name != '   ' and len(new_name)>0:
                            break
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('\n El nombre de la misión debe contener por lo menos un caracter y ser alfanumérico...\n')

                    m_modificada.name=new_name

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
        |----------------------------------------------------------------------------------------------|
        Se ha modificado el nombre de la misión, el nuevo nombre es "{m_modificada.name}"
        |----------------------------------------------------------------------------------------------|''')

                elif response == '2':

                    """MODIFICAR PLANETA A MISION"""

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
            |----------------------------------------------------------------------------------------------|
                                    Modificar Planeta de la misión "{m_modificada.name}"

                ---> El planeta registrado es "{m_modificada.planet.name}"
        ''')
                    while True:

                        """LEE ARCHIVO CSV. DE PLANETA Y CREA LISTA DE PLANETAS"""
                        
                        archivo = os.path.join('csv', 'planets.csv')

                        with open(archivo, mode='r') as file:
                            reader = csv.DictReader(file)

                                # Lee y muestra cada fila como un diccionario, presenta la lista de opciones enumeradas.
                            for indice,row in enumerate(reader):
                                    print(f'{indice+1} - {row['name']}')

                        new_planet=input("""\nEscriba el numero del nuevo Planeta de destino (puede escribir "regresar" para retroceder)::
                ---> """)
                        
                        if new_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:

                            """VALIDA RESPUESTA"""

                            os.system('cls' if os.name == 'nt' else 'clear')

                            """CONVIERTE RESPUESTA EN OBJETO PLANETA"""

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

                        elif new_planet.lower() =="regresar":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break

                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ingrese un número o valor válido...\n')

                elif response == '3':

                    """MODIFICAR NAVE A MISION"""

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print(f'''
            |----------------------------------------------------------------------------------------------|
                                    Modificar nave de la misión "{m_modificada.name}"

                ---> La nave registrada es "{m_modificada.starship.name}"
        ''')

                    while True:

                        """lEE ARCHIVO CSV. DE NAVES, GENERA LISTA DE NAVES Y LA MUESTRA POR PAGINAS"""

                        archivo = os.path.join('csv', 'starships.csv')
                        with open(archivo, mode='r') as file:
                            reader = csv.DictReader(file)
                                
                            lista_naves=[]
                            for row in reader:
                                lista_naves.append(row['name'])

                        pagina=paginar_lista(lista_naves)

                        pagina*=10

                        option_starship=input("""\nEscriba el número de la nueva nave (puede escribir "regresar" para retroceder):
        ---> """)

                        if option_starship in ['1','2','3','4','5','6','7','8','9','10']:

                            """VALIDACION DE RESPUESTA"""

                            option_starship=int(option_starship)

                        elif option_starship.lower() == "regresar":

                            os.system('cls' if os.name == 'nt' else 'clear')

                            break

                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ingrese un número válido...\n')

                        if isinstance(option_starship,int) and option_starship > 0 and option_starship < 11:

                            """CONVERSION DE RESPUESTA AL ID DE NAVE"""

                            option_starship+=pagina
                            
                            option_starship=str(option_starship)

                            os.system('cls' if os.name == 'nt' else 'clear')

                            """CONVIERTE RESPUESTA EN OBJETO NAVE"""

                            with open(archivo, mode='r') as file:
                                reader = csv.DictReader(file)

                                for row in reader:
                                    if row['id']== option_starship:
                                        nave=Starships(row['model'],row['manufacturer'], row['cost_in_credits'], row['length'], row['crew'], row['passengers'], row['max_atmosphering_speed'], row['hyperdrive_rating'], row['MGLT'], row['cargo_capacity'], row['consumables'],row['name'],'', row['starship_class'],row['pilots'])

                            m_modificada.starship=nave


                            print(f'''
                |----------------------------------------------------------------------------------------------|
                Se ha modificado la nave de la misión, la nueva nave es "{nave.name}"
                |----------------------------------------------------------------------------------------------|
                ''')
                            break

                elif response == '4':

                    """MODIFICAR ARMAS A MISION"""

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

                        if respuesta == '1':

                            """OPCION ELIMINAR ARMA"""

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

                                """VALIDA RESPUESTA Y ELIMINA ARMA"""

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

                                elif arma_eliminar.lower()=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('Por favor ingrese el nombre de un arma registrada.')

                        elif respuesta == '2' and len(armas_elegidas)>=7:

                            """OPCION AGREGAR ARMA (AVISO DE MAXIMO DE ARMAS REGISTRADAS)"""

                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ya existen 7 armas registradas, por favor elimine algún arma primero.\n')

                        elif respuesta == '2' and len(armas_elegidas)<7:

                            """OPCION AGREGAR ARMA"""

                            os.system('cls' if os.name == 'nt' else 'clear')

                            while True:

                                print(f'''
                |----------------------------------------------------------------------------------------------|
                                Agregar armas de la misión "{m_modificada.name}"
                                        
                                        ''')
                                
                                while True:

                                    """LEE ARCHIVO CSV. DE ARMAS, CREA LISTA DE ARMAS Y LO MUESTRA POR PAGINAS"""

                                    archivo = os.path.join('csv', 'weapons.csv')
                                    with open(archivo, mode='r') as file:
                                        reader = csv.DictReader(file)
                                        
                                        lista_armas=[]
                                        for row in reader:
                                            lista_armas.append(row['name'])

                                    pagina=paginar_lista(lista_armas)

                                    pagina*=10

                                    new_weapon=input("""\nEscriba el número de la nueva arma (puede escribir "regresar" para retroceder):
        ---> """)

                                    if new_weapon in ['1','2','3','4','5','6','7','8','9','10']:

                                        """VALIDA RESPUESTA"""

                                        new_weapon=int(new_weapon)

                                    elif new_weapon.lower() == 'regresar':
                                        break

                                    if isinstance(new_weapon,int) and new_weapon > 0 and new_weapon < 11:

                                        """CONVIERTE RESPUESTA EN ID DE ARMA"""

                                        new_weapon+=pagina
                                        
                                        new_weapon=str(new_weapon)

                                        break

                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print('Ingrese un número válido...\n')

                                if new_weapon.lower()=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                os.system('cls' if os.name == 'nt' else 'clear')

                                """CONVIERTE LA RESPUESTA EN OBJETO ARMA"""

                                with open(archivo, mode='r') as file:
                                    reader = csv.DictReader(file)

                                    for row in reader:
                                        if row['id']== new_weapon:
                                            arma=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])

                                arma.mostrar_att()
                                
                                armas_elegidas.append(arma)

                                if len(armas_elegidas)>=7:

                                    """VERIFICA LIMITE DE ARMAS"""

                                    print('Se encuentran registradas 7 armas para la misión.')
                                    break

                                break

                        elif respuesta == '0':

                            """OPCION REGRESAR"""

                            break

                elif response == '5':

                    """MODIFICAR INTEGRANTES DE MISION"""
                     
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
                    
                        if respuesta == '1':

                            """OPCION ELIMINAR INTEGRANTE"""

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

                                """VALIDA RESPUESTA Y ELIMINA INTEGRANTE"""

                                for persona in integrante_eliminar:
                                    if integrante_eliminar == persona.name:
                                        integrante_eliminar=persona
                        
                                if integrante_eliminar in integrantes_elegidos:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    integrantes_elegidos.remove(integrante_eliminar)
                                    print(f'''
        |----------------------------------------------------------------------------------------------------------------|
        Se ha registrado el cambio en la lista de integrantes, se ha eliminado al integrante "{integrante_eliminar.name}"
        |----------------------------------------------------------------------------------------------------------------|
                ''')
                                    break

                                elif integrante_eliminar.lower()=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print('Por favor ingrese el nombre de un integrante registrado.')

                        elif respuesta == '2' and len(integrantes_elegidos)>=7:

                            """OPCION AGREGAR INTEGRANTE (AVISO DE MAXIMO DE INTEGRANTES REGISTRADOS)"""

                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Ya hay 7 integrantes en la misión, por favor elimine a alguno primero para agregar un personaje nuevo.\n')
                        
                        elif respuesta == '2' and len(integrantes_elegidos)<7:

                            """OPCION AGREGAR INTEGRANTE"""

                            os.system('cls' if os.name == 'nt' else 'clear')

                            while True:

                                print(f'''
        |----------------------------------------------------------------------------------------------|
                    Agregar integrantes para la misión "{m_modificada.name}"
                                        
                                        ''')
                                
                                while True:

                                    """LEE ARCHIVO CSV. DE PERSONAJES, CREA LISTA DE PERSONAJES Y LO MUESTRA POR PAGINAS"""

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

                                        """VALIDA RESPUESTA"""

                                        new_character=int(new_character)

                                    elif new_character == 'regresar':
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        break

                                    else:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print('Ingrese un número válido...\n')


                                    if isinstance(new_character,int) and new_character > 0 and new_character < 11:

                                        """IGUALA RESPUESTA AL ID DE PERSONAJE"""

                                        new_character+=pagina
                                        
                                        new_character=str(new_character)

                                        break

                                if new_character.lower()=="regresar":
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                os.system('cls' if os.name == 'nt' else 'clear')

                                """CONVIERTE RESPUESTA EN OBJETO PERSONAJE"""

                                with open(archivo, mode='r') as file:
                                    reader = csv.DictReader(file)

                                    for row in reader:
                                        if row['id']== new_character:
                                            persona=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')

                                integrantes_elegidos.append(persona)

                                print(f'''
        |-------------------------------------------------------------------------------------------------------------------|
        Se ha registrado el cambio en la lista de integrantes, se ha agregado al integrante "{persona.name}"
        |-------------------------------------------------------------------------------------------------------------------|
                ''')

                                if len(integrantes_elegidos)>=7:

                                    """VERIFICA LIMITE DE INTEGRANTES"""

                                    print('Ya se encuentran registrados 7 integrantes para la misión.')
                                    break

                                break

                        elif respuesta == '0':

                            """OPCION REGRESAR"""

                            os.system('cls' if os.name == 'nt' else 'clear')
                            break

                    #REGRESAR AL MENÚ DE SELECCIÓN DE MISIONES PARA MODIFICAR

                elif response == '6':

                    """OPCION PARA REGRESAR AL MENU PRINCIPAL DE MISIONES"""

                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

                elif response == "0":

                    """ELIMINA MISIONDE LISTA DE MISIONES"""

                    os.system('cls' if os.name == 'nt' else 'clear')
                    mision_eliminar=m_modificada.name
                    lista_misiones.remove(m_modificada)
                    print(f'''
        |----------------------------------------------------------------------------------------------|
         Se ha eliminado la misión "{mision_eliminar}"
        |----------------------------------------------------------------------------------------------|''')
                    break

        return lista_misiones

    def __str__(self):
        
        """FUNCION PARA CONVERTIR LISTA DE OBJETOS MISION EN CADENA DE TEXTO"""

        lista_armas=[]
        lista_personajes=[]
        for weapon in self.weapons:
            lista_armas.append(weapon.name)
        for personaje in self.characters:
            lista_personajes.append(personaje.name)

        return f"{self.name} , {self.planet.name} , {self.starship.name} , {lista_armas} , {lista_personajes}"

    def guardar(lista_misiones):

        """FUNCION PARA GUARDAR LA LISTA DE MISIONES EN ARCHIVO TXT"""

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            """SALIDA DEL MENÚ DE GUARDAR MISIÓN"""

            salida=input("""
        ¡Bienvenido al menú para guardar misiones!
                         
    |----------------------------------------------------------------------------------------------|
                                    GUARDAR MISIONES

                                         
    Escribe cualquier caracter si desea continuar.
    Escribe "salir" si desea abandandonar el menú de guardar misiones.

                   
    
    ---> """)
            
            if salida.lower() == "salir":

                os.system('cls' if os.name == 'nt' else 'clear')

                break

            os.system('cls' if os.name == 'nt' else 'clear')

            carpeta = 'misiones_guardadas'
            archivo = 'misiones.txt'

            """OBTIENE RUTA DEL ARCHIVO ACTUAL"""

            directorio_actual = os.path.dirname(os.path.abspath(__file__))

            """CONSTRUYE RUTA PARA GUARDAR MISIONES"""

            ruta_carpeta = os.path.join(directorio_actual, carpeta)
            ruta_archivo = os.path.join(ruta_carpeta, archivo)

            """VERIFICA LA EXISTENCIA DE LA CARPETA Y/O CREA LA CARPETA"""

            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)

            """GUARDA LAS MISIONES EN ARCHIVO TXT"""

            with open(ruta_archivo, 'w') as archivo:
                for mision in lista_misiones:
                    archivo.write(str(mision) + '\n')

            print(f'''
        
        ¡Se ha guardado el registro de misiones exitosamente!
        
    |--------------------------------------------------------------------------------------------------|
      Datos guardados en {ruta_archivo}
    |--------------------------------------------------------------------------------------------------|             
    ''')
            break

    def convertir_txt(texto):

        """FUNCION PARA CONVERTIR EL ARCHIVO TXT A OBJETO MISION"""

        """MODIFICA AL ARCHIVO TXT PARA OBTENER ATRIBUTOS DE OBJETOS"""

        name, planet, starship, lista_armas, lista_personajes = texto.split(' , ')

        lista_armas=lista_armas.replace('[','')
        lista_armas=lista_armas.replace(']','')
        lista_armas=lista_armas.replace("'","")

        lista_armas=lista_armas.split(', ')

        lista_personajes=lista_personajes.replace('[','')
        lista_personajes=lista_personajes.replace(']','')
        lista_personajes=lista_personajes.replace("'","")

        lista_personajes=lista_personajes.split(', ')


        armas_elegidas=[]
        integrantes_elegidos=[]

        """SE CONVIERTE NOMBRE DE PLANETA A OBJETO PLANETA"""

        archivo = os.path.join('csv', 'planets.csv')
        with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['name']== str(planet):
                        planet=Planets(row['diameter'],row['rotation_period'],row['orbital_period'],row['gravity'],row['population'],row['climate'],row['terrain'],row['surface_water'],'','',row['name'],'')

        """SE CONVIERTE NOMBRE DE NAVE A OBJETO NAVE"""

        archivo = os.path.join('csv', 'starships.csv')
        with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['name'] == str(starship):
                        starship=Starships(row['model'],row['manufacturer'], row['cost_in_credits'], row['length'], row['crew'], row['passengers'], row['max_atmosphering_speed'], row['hyperdrive_rating'], row['MGLT'], row['cargo_capacity'], row['consumables'],row['name'],'', row['starship_class'],row['pilots'])

        """SE CONVIERTE LA LISTA DE NOMBRES DE ARMAS A LISTA DE OBJETOS ARMAS"""

        for arma in lista_armas:
            archivo = os.path.join('csv', 'weapons.csv')
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['name']== arma:
                        arma1=Weapon(row['id'],row['name'],row['model'],row['manufacturer'],row['cost_in_credits'],row['length'],row['type'],row['description'],row['films'])
                        armas_elegidas.append(arma1)

        weapons=armas_elegidas

        """SE CONVIERTE LA LISTA DE NOMBRES DE PERSONAJES A LISTA DE OBJETOS PERSONAJE"""
    
        for personaje in lista_personajes:
            archivo = os.path.join('csv', 'characters.csv')
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row['name']== personaje:
                        personaje1=People(row['height'],row['weight'],row['hair_color'],row['skin_color'],row['eye_color'],row['year_born'],row['gender'],'','',row['name'],row['homeworld'],'')
                        integrantes_elegidos.append(personaje1)

        characters=integrantes_elegidos

        mision=Mision(name, planet, starship, weapons, characters)

        return mision

    def cargar():

        """FUNCION PARA CARGAR EL ARCHIVO TXT EN LA LISTA DE MISIONES
        
        return: lista_misiones: regresa lista de misiones guardada en archivo txt"""

        while True:

            lista_misiones = []

            os.system('cls' if os.name == 'nt' else 'clear')

            carpeta = 'misiones_guardadas'
            archivo = 'misiones.txt'

            """OBTIENE RUTA DEL ARCHIVO ACTUAL"""
            directorio_actual = os.path.dirname(os.path.abspath(__file__))

            """OBTIENE RUTA DE MISIONES GUARDADAS"""
            ruta_carpeta = os.path.join(directorio_actual, carpeta)
            if os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta):
                ruta_archivo = os.path.join(ruta_carpeta, archivo)

                """LEE EL ARCHIVO TXT Y LO CONVIERTE EN LISTA DE MISIONES"""
                with open(ruta_archivo, 'r') as archivo:
                    for linea in archivo:
                        linea = linea.strip()  # Quitar espacios en blanco y saltos de línea
                        if linea:
                            mision = Mision.convertir_txt(linea)
                            lista_misiones.append(mision)

                nombre_misiones = [mision.name for mision in lista_misiones]

                print(f'''

        ¡Se ha cargado el registro de misiones exitosamente!              
        
    |----------------------------------------------------------------------------------------------|
    Las siguientes misiones han sido registradas:
            ''')    
                for i in nombre_misiones:
                    print(f'''
        "{i}"''') 
                print(f'''
    |----------------------------------------------------------------------------------------------|''')
                break
            else:
                break
        return lista_misiones

def menu_misiones():

    """FUNCION A EJECUTAR PARA ABRIR MENÚ"""

    os.system('cls' if os.name == 'nt' else 'clear')
    
    mision_creada=False

    while True:
        

        """FUNCION A EJECUTAR PARA ABRIR MENÚ"""

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
                  
(Si ya ha creado misiones y selecciona "Crear misiones" estará eliminando las misiones construidas
 anteriormente.)
                  
Nota: Al salir, las misiones registradas serán eliminadas, así que es recomendable guardar misiones
antes.
                                ''')
                
            response=input("""Escribe el número de la opción que quiere ejecutar:
---> """)
            """VALIDA RESPUESTA"""

            if response in ['1','2','3','4','5']:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Escribe un comando válido.")

        if response=='1':

            """EJECUTA FUNCION CONSTRUIR"""

            try:
                lista_misiones
            except NameError:
                lista_misiones=[]

            lista_misiones,mision_registrada=Mision.construir(lista_misiones)

            if mision_registrada == True:
                mision_creada=True

        elif response=='2' and mision_creada==True and len(lista_misiones)>0:

            """EJECUTA FUNCION MODIFICAR"""

            lista_misiones=Mision.modificar(lista_misiones)
    
        elif response == '2' and mision_creada==False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No posee ninguna misión creada, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión.')

        elif response == '2' and len(lista_misiones)==0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No posee ninguna misión creada, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión.')

        elif response == '3' and mision_creada==True and len(lista_misiones)>0:

            """EJECUTA FUNCION GUARDAR"""

            Mision.guardar(lista_misiones)

        elif response == '3' and mision_creada==False:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No posee ninguna misión creada, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión.')

        elif response == '3' and len(lista_misiones)==0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No posee ninguna misión creada, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión.')

        elif response=='4':

            """EJECUTA FUNCION CARGAR"""

            while True:

                os.system('cls' if os.name == 'nt' else 'clear')
                            
                """SALIDA DEL MENÚ DE CARGAR MISIÓN"""

                salida=input("""
        ¡Bienvenido al menú para cargar misiones!
                         
    |----------------------------------------------------------------------------------------------|
                                        CARGAR MISIONES

    Escribe cualquier caracter si desea realizar la carga de registros previamente guardados.                                           
    Escribe "salir" si desea abandandonar el menú de cargar misiones.
                             
    (Si posee misiones creadas en esta sesión, al cargar misiones estará borrando dichas misiones)
                   
    
    ---> """)
            
                if salida.lower() == "salir":

                    os.system('cls' if os.name == 'nt' else 'clear')

                    break
                lista_misiones=Mision.cargar()

                if lista_misiones!=[]:
                    mision_creada=True
                    break

                elif lista_misiones==[]:
                    print('No existen misiones guardadas previamente, por favor seleccione la opción "Crear misiones" y registre por lo menos una misión. ')
                    break

        elif response == '5':

            """SALIDA DEL MENU"""

            break
        
"""FUNCIONES PARA ORDENAR UNA LISTA EN PAGINAS"""

def mostrar_pagina(lista, pagina, elementos_por_pagina=10):

    """DESPLIEGA EL CONTADOR DE PAGINAS"""

    inicio = pagina * elementos_por_pagina
    fin = inicio + elementos_por_pagina
    
    for indice,i in enumerate(range(inicio, min(fin, len(lista)))):
        print(f'{indice+1} - {lista[i]}')

def paginar_lista(lista):

    """ORGANIZA UNA LISTA EN PAGINAS CON LA OPCION DE AVANZAR O RETROCEDER POR PAGINA"""

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

