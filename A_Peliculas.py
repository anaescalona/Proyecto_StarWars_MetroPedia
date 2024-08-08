import requests as rq
from Clases.Films import Films

class A_Peliculas:

    def __init__(self):
      
        self.lista_peliculas_saga = []

    def Extraer_info(self):

        """Esta función permite extraer la informacion de la extension de la api "swapi" en films y guardar 
        la informacion correspondiente como objeto Films

        Returns:
            self.lista_peliculas_saga(list): lista con informacion sobre las peliculas de la saga
        """
        try:
            peliculas = rq.get('https://www.swapi.tech/api/films/')
            peliculas = peliculas.json()

            for i in peliculas['result']:
                self.lista_peliculas_saga.append(Films(i['properties']['characters'], i['properties']['planets'], i['properties']['starships'], i['properties']['vehicles'], i['properties']['species'], i['properties']['created'], i['properties']['edited'], i['properties']['producer'], i['properties']['title'], i['properties']['episode_id'], i['properties']['director'], i['properties']['release_date'], i['properties']['opening_crawl'], i['properties']['url']))
        except:
             
             print("No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet")
            
        return self.lista_peliculas_saga


    def mostrar_peliculas(self):
        """Esta función permite imprimir cada una de las peliculas con su respectiva informacion en el formato deseado

        """
        for j in self.lista_peliculas_saga:
            j.mostrar_pelicula()


def mainA():
    """Esta función permite realizar las funciones dentro de la clase A_Peliculas para obtener la informacion requerida en el inciso A 
    """
                
    Pelicula = A_Peliculas()
    Pelicula.Extraer_info()
    Pelicula.mostrar_peliculas()


