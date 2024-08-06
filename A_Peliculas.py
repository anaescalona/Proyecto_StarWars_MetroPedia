import requests as rq
from Clases.Films import Films

lista_peliculas_saga = []

def Extraer_info():

    """Esta función permite extraer la informacion de la extension de la api "swapi" en films y guardar la informacion correspondiente como objeto Films

    Returns:
        lista_peliculas_saga(list): lista con informacion sobre las peliculas de la saga
    """

    peliculas = rq.get('https://www.swapi.tech/api/films/')
    peliculas = peliculas.json()

    for i in peliculas['result']:
        lista_peliculas_saga.append(Films(i['properties']['characters'], i['properties']['planets'], i['properties']['starships'], i['properties']['vehicles'], i['properties']['species'], i['properties']['created'], i['properties']['edited'], i['properties']['producer'], i['properties']['title'], i['properties']['episode_id'], i['properties']['director'], i['properties']['release_date'], i['properties']['opening_crawl'], i['properties']['url']))

    return lista_peliculas_saga


def mostrar_peliculas():
    """Esta función permite imprimir cada una de las peliculas con su respectiva informacion en el formato deseado

    """
    for j in lista_peliculas_saga:
        j.mostrar_pelicula()
        
