from A_Peliculas import A_Peliculas
from B_Seres_vivos import B_Seres_vivos
from C_Planetas import C_Planetas
from D_Personajes import D_Personajes


# CARGAR LAS PELICULAS
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

# OPERANDOS DE LOS METODOS
seres_vivos.MatchPlanetas(lista_planetas)
seres_vivos.MatchPeople(lista_personajes)
seres_vivos.MatchEpisodes(lista_peliculas_saga)

planetas.MatchPeliculas_Planetas_Personajes(lista_peliculas_saga, lista_personajes)

personajes.MatchPersonajes_Especies(lista_seres_vivos)
personajes.MatchPlanetas(lista_planetas)
personajes.MatchPeliculas_Personajes(lista_peliculas_saga)
personajes.MatchVehicles()
personajes.MatchStartships()





print('------------ REPUBLICA BOLIVARIANA DE VENEZUELA -----------')
print('------------ UNIVERSIDAD METROPOLITANA --------------------')
print('-----------  FACULTAD INGENIERIA --------------------------')
print('------------ ALGORITMOS Y PROGRAMACION --------------------')

while True:
    print('A) Lista de Películas de la saga')
    print('B) Lista de las especies de seres vivos de la saga')
    print('C) Lista de planetas')
    print('D) Buscar personaje')
    print('F) Salir del programa')
    opcion = input('Ingrese la letra de las opciones mencionadas: ')
    if(opcion == 'A'):
        peliculas.mostrar_peliculas()
    elif(opcion == 'B'):
        seres_vivos.show_species()
    elif(opcion == 'C'):
        planetas.show_planetas()
    elif(opcion == 'D'):
        busqueda = input("Ingrese el nombre del personaje que desees buscar: ")
        personajes.getCharactersByName(busqueda)
    elif(opcion == 'F'):
        print('SALIENDO DEL PROGRAMA ...')
        break
    else:
        print('Opcion Invalida')

