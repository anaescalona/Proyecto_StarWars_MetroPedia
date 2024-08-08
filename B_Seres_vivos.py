import requests as rq
from Clases.Species import Species
from Clases.People import People
from Clases.Films import Films
from A_Peliculas import A_Peliculas 

class B_Seres_vivos:

    def __init__(self):
        self.especies_list = []
        self.people_list = []

    def getSpecies(self):

        """Esta funcion permite obtener la información de la api de las especies y sus caracteristicas, no obstante para ello debe ingresar al url
        de cada especie para indagar acerca de las caracteristicas de cada una. Esto también ocurre al indagar el planeta de nacimiento.
        Returns:
            self.especies_list(list): lista con información sobre cada una de las especies como objetos. 
        """
        print('*Atención*:Debido a que el sistema debe consultar diferentes bases de datos, este proceso puede ser un poco demorado. Por favor espere...')
        try: 
            request = rq.get("https://www.swapi.tech/api/species/")
            response = request.json()

            MAX_ESPECIES = int(response["total_records"])

            for i in range(1, MAX_ESPECIES+1):
                self.people_list = []
                print("*** CARGANDO ESPECIES ***")
                url = f'https://www.swapi.tech/api/species/{i}'
                try:
                    especies_request = rq.get(url)
                    especies_response = especies_request.json()

                    classification = especies_response["result"]["properties"]["classification"]
                    designation = especies_response["result"]["properties"]["designation"]
                    average_height = especies_response["result"]["properties"]["average_height"]
                    average_lifespan = especies_response["result"]["properties"]["average_lifespan"]
                    hair_colors = especies_response["result"]["properties"]["hair_colors"]
                    skin_colors = especies_response["result"]["properties"]["skin_colors"]
                    eye_colors = especies_response["result"]["properties"]["eye_colors"]
                    language = especies_response["result"]["properties"]["language"]
                    name = especies_response["result"]["properties"]["name"]
                    url = especies_response["result"]["properties"]["url"]
                    created = especies_response["result"]["properties"]["created"]
                    edited = especies_response["result"]["properties"]["edited"]

                    homeworld_url = especies_response["result"]["properties"]["homeworld"]
                    homeworld_request = rq.get(homeworld_url)
                    homeworld_response = homeworld_request.json()

                    homeworld = homeworld_response["result"]["properties"]["name"]

                    for people in especies_response["result"]["properties"]["people"]:
                        try:
                            people_request = rq.get(people)
                            people_response = people_request.json()
                            self.people_list.append(people_response["result"]["properties"]["name"])
                        except: 
                            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')


                    self.especies_list.append(Species(classification, designation, average_lifespan, average_height, hair_colors, skin_colors, eye_colors, homeworld, language, created, edited, name, url, self.people_list))

                except: 
                    print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')

            
        except: 
            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')

        return self.especies_list
        
    def MatchEpisodes(self):
        """Esta función permite buscar la coincidencia entre las especies y los episodios en los que aparecen. 
           Para ello, utiliza la informacion extraída en el inciso A. Luego de realizar este proceso, imprime la informacion en el formato deseado. 
        """

        pelicula_saga = A_Peliculas()
        lista_peliculas_saga = pelicula_saga.Extraer_info()

        for especie in self.especies_list:
            for episode in lista_peliculas_saga:
                if(especie.url in episode.species): 
                    especie.episode_id.append(episode.title)
            especie.mostrar_especie()

            
    
def mainB():
    seres_vivos = B_Seres_vivos()
    seres_vivos.getSpecies()
    seres_vivos.MatchEpisodes()
   
