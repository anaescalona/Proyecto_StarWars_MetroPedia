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

        """Esta funcion permite obtener la información de la api swapi en especies, sus caracteristicas, y guardarlas como objeto.
        Returns:
            self.especies_list(list): lista con información sobre cada una de las especies como objetos. 
        """
        try: 
            request = rq.get("https://www.swapi.tech/api/species/")
            response = request.json()

            MAX_ESPECIES = int(response["total_records"])

 
            for i in range(1, MAX_ESPECIES + 1):
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
                    homeworld = especies_response["result"]["properties"]["homeworld"]
                    people = especies_response["result"]["properties"]["people"]

                    self.especies_list.append(Species(classification, designation, average_lifespan, average_height, hair_colors, skin_colors, eye_colors, homeworld, language, created, edited, name, url, people))

                except: 
                    continue
     
        except: 
            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')

        return self.especies_list
    

    def MatchPlanetas(self, listado_planetas):
        """Este método permite buscar la coincidencia entre las especies y su planeta de origen.

        Args:
            listado_planetas (list): lista con la información de cada uno de los planetas, obtenida en la clase C_Planetas
        """
        for especie in self.especies_list:
            for planeta in listado_planetas:
                if(especie.homeworld == planeta.url):
                    especie.homeworld = planeta.name

    def MatchPeople(self, listado_personajes):
        """Este método permite buscar la coincidencia entre los nombre de los personajes y la especie a la que pertenecen. 

        Args:
            listado_personajes (list): lista de los personajes de la saga, obtenidos en la clase D_Personajes.

        Returns:
            self.especies_list(list): lista con especies luego de haber hecho coincidir los nombres de los personajes con la especie a la que pertencen.
        """
        for especies in self.especies_list:
            self.people_list = []
            
            for personajes in listado_personajes:
                if(personajes.url in especies.people):
                    self.people_list.append(personajes.name)

            especies.people = self.people_list

        return self.especies_list
        
    def MatchEpisodes(self, lista_peliculas_saga):
        """Este método permite buscar la coincidencia entre las especies y los episodios en los que aparecen. 
           

        Args:
            lista_peliculas_saga (list): lista de peliculas de la saga extraída en la clase A_Peliculas
        """
        for especie in self.especies_list:
            for episode in lista_peliculas_saga:
                if(especie.url in episode.species): 
                    especie.episode_id.append(episode.title)

        

    def show_species(self):
        """Imprime la información acerca de las especies en el formato indicado
        """
        for j in self.especies_list:
            j.mostrar_especie()


   
