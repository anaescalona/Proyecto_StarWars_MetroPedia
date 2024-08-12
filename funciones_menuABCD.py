from A_Peliculas import A_Peliculas
from B_Seres_vivos import B_Seres_vivos
from C_Planetas import C_Planetas
from D_Personajes import D_Personajes

def carga_api():

    """Esta funcion permite realizar toda la carga de la informacion proveniente de la SWAPI a manera de objetos. 

    Returns:
        peliculas(variable): Objeto de la clase A_Peliculas
        seres_vivos(variable) : Objeto de la clase B_Seres_vivos
        personajes(variable): Objeto de la clase D_Personajes
        planetas(variable):Objeto de la clase C_Planetas
        lista_peliculas_saga(list): lista con la informacion de las peliculas de la saga.
        lista_planetas(list) :lista con la informacion de los planetas de la saga.
        lista_seres_vivos(list) :lista con la informacion de los seres vivos de la saga.
        lista_personajes(list) :lista con la informacion de los personajes de la saga.
        lista_vehiculos(list) :lista con la informacion de los vehiculos de la saga.
        lista_starships(list) :lista con la informacion de las naves de la saga.


    """

    # CARGAR LAS PELICULAS=
    peliculas = A_Peliculas()
    lista_peliculas_saga = peliculas.Extraer_info()


    # CARGAR LOS SERES VIVOS
    seres_vivos = B_Seres_vivos()
    lista_seres_vivos = seres_vivos.getSpecies()

    # CARGAR LOS PERSONAJES
    personajes = D_Personajes()
    lista_personajes = personajes.GetPeople()

    # CARGAR LOS PLANETAS
    planetas = C_Planetas()
    lista_planetas = planetas.getPlanetas()

    # CARGAR LOS VEHICULOS
    lista_vehiculos = personajes.getVehicles()

    # CARGAR LOS STARSHIPS
    lista_startships = personajes.getStarships()



    return  peliculas, seres_vivos, personajes, planetas, lista_peliculas_saga, lista_seres_vivos, lista_personajes, lista_planetas, lista_vehiculos, lista_startships

def Match_Menu_Parte1(peliculas, seres_vivos, personajes, planetas, lista_peliculas_saga, lista_seres_vivos, lista_personajes, lista_planetas):
     
    """Esta funcion permite operar los diferentes metodos de las clases A, B, C Y D haciendo uso de las listas cargadas de la SWAPI. 
    Una vez ejecutados los metodos muestra un menu para desplegar la informacion requerida en el inciso A,B,C,D

       Args:
        peliculas(variable): Objeto de la clase A_Peliculas
        seres_vivos(variable) : Objeto de la clase B_Seres_vivos
        personajes(variable): Objeto de la clase D_Personajes
        planetas(variable):Objeto de la clase C_Planetas
        lista_peliculas_saga(list): lista con la informacion de las peliculas de la saga.
        lista_planetas(list) :lista con la informacion de los planetas de la saga.
        lista_seres_vivos(list) :lista con la informacion de los seres vivos de la saga.
        lista_personajes(list) :lista con la informacion de los personajes de la saga.

    """
    # OPERANDOS DE METODOS
    
    seres_vivos.MatchPlanetas(lista_planetas)
    seres_vivos.MatchPeople(lista_personajes)
    seres_vivos.MatchEpisodes(lista_peliculas_saga)

    planetas.MatchPeliculas_Planetas(lista_peliculas_saga)
    planetas.MatchPersonajes_Planetas(lista_personajes)

    personajes.MatchPersonajes_Especies(lista_seres_vivos)
    personajes.MatchPlanetas(lista_planetas)
    personajes.MatchPeliculas_Personajes(lista_peliculas_saga)
    personajes.MatchVehicles()
    personajes.MatchStartships()
    


    while True:
        print("|----------------------------------------------------|")
        print('\tBienvenido a la Wiki de StarWars ')
        print('|----------------------------------------------------|')
        print('\t1.- Lista de Películas de la saga')
        print('\t2.- Lista de las especies de seres vivos de la saga')
        print('\t3.- Lista de planetas')
        print('\t4.- Buscar personaje')
        print('\t5.- Volver al Menú principal')
        print('')
        opcion = input('Ingrese el número de las opciones mencionadas: ')
        if(opcion == '1'):
            peliculas.mostrar_peliculas()
        elif(opcion == '2'):
            seres_vivos.show_species()
        elif(opcion == '3'):
            planetas.show_planetas()
        elif(opcion == '4'):
            busqueda = input("Ingrese el nombre del personaje que desees buscar: ")
            personajes.getCharactersByName(busqueda)
        elif(opcion == '5'):
            print('Volviendo al Menú principal...')
            break
        else:
            print('Opcion Invalida')



