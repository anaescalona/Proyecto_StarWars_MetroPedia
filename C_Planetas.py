from Clases.Films import Films 
from Clases.People import People
from Clases.Planets import Planets
from A_Peliculas import A_Peliculas
import requests as rq 
class C_Planetas:
    def __init__(self):
        self.planets_list = []

    def getPlanetas(self):

        planetas = rq.get("https://www.swapi.tech/api/planets/") 
        planetas = planetas.json()

        MAX_planetas = int(planetas['total_records'])

        for j in range(1,MAX_planetas+1):

            url = f'https://www.swapi.tech/api/planets/{j}'

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

        
            self.planets_list.append(Planets(diameter,rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, created, edited, name, url))
            print(f"PLANETA REGISTRADO EXITOSAMENTE")

        return self.planets_list


    def MatchPeliculas_Planetas_Personajes(self):
        pelicula_saga = A_Peliculas()
        lista_peliculas_saga = pelicula_saga.Extraer_info()
        
        for i in self.planets_list:
            for j in lista_peliculas_saga:
                if (i.url in j.planets):
                    i.episode_id.append(j.title) # EPISODE_ID es un Array
                    for people in j.characters:
                        people_request = rq.get(people)
                        people_response = people_request.json()
                        if(people_response["result"]["properties"]["homeworld"] == i.url):
                            i.people.append(people_response["result"]["properties"]["name"])
            i.mostrar_planetas()


    def show_planetas(self):
        for j in self.planets_list:
            j.mostrar_planetas()


def mainC():
    Planeta = C_Planetas()
    Planeta.getPlanetas()
    Planeta.MatchPeliculas_Planetas_Personajes()
    Planeta.show_planetas()




 

