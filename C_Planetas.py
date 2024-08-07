from Clases.Films import Films 
from Clases.People import People
from Clases.Planets import Planets
from A_Peliculas import A_Peliculas
import requests as rq 
class C_Planetas:
    def __init__(self):
        self.planets_list = []

    def getPlanetas(self):
        
        """Esta función permite obtener la informacion de la extensión de la api swapi planets, con la finalidad de encontrar 
        dentro de ella la informacion correspondiente a cada uno y guardarlo como objetos en la lista self.planets_list.

        Returns:
            self.planets_list(list): Lista con información de cada planeta en la saga.
        """
        print('* Atención * : Debido a que el sistema debe consultar diferentes bases de datos, este proceso puede ser demorado. La impresión de los planetas se hace uno a uno luego de que estos sean cargados. Por favor espere...')
        try:
            planetas = rq.get("https://www.swapi.tech/api/planets/") 
            planetas = planetas.json()

            MAX_planetas = int(planetas['total_records'])

            for j in range(1,MAX_planetas+1):
                print("*** CARGANDO PLANETAS ***")
                url = f'https://www.swapi.tech/api/planets/{j}'

                try:

                    planetas_request = rq.get(url)

                    planetas_response = planetas_request.json()

                    diameter = planetas_response['result']['properties']['diameter']
                    rotation_period = planetas_response['result']['properties']['rotation_period']
                    orbital_period = planetas_response['result']['properties']['orbital_period']
                    gravity = planetas_response['result']['properties']['gravity']
                    population = planetas_response['result']['properties']['population']
                    climate = planetas_response['result']['properties']['climate']
                    terrain = planetas_response['result']['properties']['terrain']
                    surface_water = planetas_response['result']['properties']['surface_water']
                    created = planetas_response['result']['properties']['created']
                    edited = planetas_response['result']['properties']['edited']
                    name = planetas_response['result']['properties']['name']
                    url = planetas_response['result']['properties']['url']

                except:
                    print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')
            
                self.planets_list.append(Planets(diameter,rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, created, edited, name, url))
            
        except: 
            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')


        return self.planets_list


    def MatchPeliculas_Planetas_Personajes(self):
        """Esta función permite buscar la coincidencia entre los episodios (utilizando la información del inciso A ), los personajes y los planetas.
        Esto con la finalidad de imprimir la información según el formato deseado. 
        """
        pelicula_saga = A_Peliculas()
        lista_peliculas_saga = pelicula_saga.Extraer_info()
        
        for i in self.planets_list:
            for j in lista_peliculas_saga:
                if (i.url in j.planets):
                    i.episode_id.append(j.title) # EPISODE_ID es un Array
                    for people in j.characters:
                        try: 
                            people_request = rq.get(people)
                            people_response = people_request.json()
                            if(people_response["result"]["properties"]["homeworld"] == i.url):
                                i.people.append(people_response["result"]["properties"]["name"])
                        except: 
                            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')

            i.mostrar_planetas()


def mainC():
    Planeta = C_Planetas()
    Planeta.getPlanetas()
    Planeta.MatchPeliculas_Planetas_Personajes()




 

