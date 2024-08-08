#starships
#vehicles 
import requests as rq 
from Clases.People import People
from A_Peliculas import A_Peliculas
from B_Seres_vivos import B_Seres_vivos
from C_Planetas import C_Planetas

class D_Personajes():

    def __init__(self):
        self.lista_personajes = []


    def GetPeople(self):
        personajes = rq.get("https://www.swapi.tech/api/people/") 
        personajes = personajes.json()

        MAX_personajes = int(personajes['total_records'])


        for j in range(1,MAX_personajes+1):
                print("*** CARGANDO PERSONAJES ***")
                try:
                    url = f'https://www.swapi.tech/api/people/{j}'

        

                    personas_request = rq.get(url)

                    personas_response = personas_request.json()

                    height = personas_response['result']['properties']['height']
                    mass = personas_response['result']['properties']['mass']
                    hair_color = personas_response['result']['properties']['hair_color']
                    skin_color = personas_response['result']['properties']['skin_color']
                    eye_color = personas_response['result']['properties']['eye_color']
                    birth_year = personas_response['result']['properties']['birth_year']
                    gender = personas_response['result']['properties']['gender']
                    created = personas_response['result']['properties']['created']
                    edited = personas_response['result']['properties']['edited']
                    name = personas_response['result']['properties']['name']
                    homeworld = personas_response['result']['properties']['homeworld']
                    url = personas_response['result']['properties']['url']

                    homeworld_request = rq.get(homeworld)
                    homeworld_response = homeworld_request.json()

                    homeworld_name = homeworld_response['result']['properties']['name']
                    self.lista_personajes.append(People(height,mass,hair_color,skin_color,eye_color,birth_year,gender,created,edited,name,homeworld_name,url))

                except:
                    print("Lo sentimos no existe el personaje con el ID: ", j)

    def MatchPeliculas_Personajes_Especie(self):

        pelicula_saga = A_Peliculas()
        lista_peliculas_saga = pelicula_saga.Extraer_info()

        seres_vivos = B_Seres_vivos()
        lista_seres_vivos = seres_vivos.getSpecies()

        for personajes in self.lista_personajes:
            for peliculas in lista_peliculas_saga:
                 if (personajes.url in peliculas.characters):
                      personajes.episode_id.append(peliculas.title)

        for personajes in self.lista_personajes:
            for species in lista_seres_vivos:
                if(personajes.url in species.people):
                    personajes.especie = species.name
                    break

        
    def getVehicles(self):
         
        try: 
            request_vehicles = rq.get("https://www.swapi.tech/api/vehicles/")
            response_vehicles = request_vehicles.json()
            MAX_VEHICLES = response_vehicles["total_records"]


            for people in self.lista_personajes:
                for i in range(1, MAX_VEHICLES+1):
                    try:
                        request_vehicle = rq.get(f'https://www.swapi.tech/api/vehicles/{i}')
                        response_vehicle = request_vehicle.json()

                        name = response_vehicle["result"]["properties"]["name"]
                        pilots = response_vehicle["result"]["properties"]["pilots"]

                        if(len(pilots) > 0):
                            for data in pilots:
                                if(people.url == data):
                                    people.vehicles.append(name)
                                    print("Vehiculo encontrado")
                                    break
                        else: 
                            print('No hay pilotos en este vehiculo')

                    except:
                        print("Lo sentimos no existe el vehiculo con el ID: ", i)
        except:
            print("No hay conexion a internet")
                           

    def getStarships(self):
        try:
            request_starships = rq.get("https://www.swapi.tech/api/starships/")
            response_starships = request_starships.json()
            MAX_starships = response_starships["total_records"]

            for people in self.lista_personajes:
                for j in range(1, MAX_starships+1):

                    try: 
                        request_starship= rq.get(f'https://www.swapi.tech/api/starships/{j}')
                        response_starship = request_starship.json()

                        name = response_starship['result']['properties']['name']
                        pilotos = response_starship['result']['properties']['pilots']

                        if len(pilotos) > 0:

                            for data in pilotos: 
                                if data == people.url:
                                    people.starships.append(name)
                                    print("Starships encontrado")
                                    break

                    except:
                        print('No existe la nave con el ID,', j)


        except:
            print('No hay conexión a internet')

                      
             
    def mostrar_informacion(self):
       for j in self.lista_personajes:
           j.mostrar_personajes()


def mainD():
    Personajes = D_Personajes()
    Personajes.GetPeople()
    Personajes.MatchPeliculas_Personajes_Especie()
    Personajes.getVehicles()
    Personajes.getStarships()

mainD()