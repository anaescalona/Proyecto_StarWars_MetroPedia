from Clases.Films import Films 
from Clases.People import People
from Clases.Planets import Planets
from A_Peliculas import A_Peliculas
import requests as rq 
class C_Planetas:
    def __init__(self):
        """Inicializa la clase C_Planetas.
           Contiene una listas de planetas  que se llenarán con la informacion proveniente de la SWAPI.
        """
        self.planets_list = []

    def getPlanetas(self):
        
        """Este método permite obtener la informacion de la extensión de la api swapi planets, con la finalidad de encontrar 
        dentro de ella la informacion correspondiente a cada uno y guardarlo como objetos en la lista self.planets_list.

        Returns:
            self.planets_list(list): Lista con información de cada planeta en la saga.
        """
        try:
            planetas = rq.get("https://www.swapi.tech/api/planets/") 
            planetas = planetas.json()

            MAX_planetas = int(planetas['total_records'])

            for j in range(1,MAX_planetas + 1):
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
                    continue
            
                self.planets_list.append(Planets(diameter,rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, created, edited, name, url))
            
        except: 
            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')


        return self.planets_list


    def MatchPeliculas_Planetas(self, lista_peliculas_saga):
        """Este método permite buscar la coincidencia entre los episodios, los personajes y los planetas. Esto a partir de la informacion extraída 
        en las clases A_peliculas.

        Args:
            lista_peliculas_saga (list): lista de peliculas de la saga extraída en la clase A_Peliculas 
            

        Returns:
            self.planets_list(list): lista con la información requerida de los planetas luego de haber encontrado la coincidencia con las peliculas.
        """
        
        for i in self.planets_list:
            for j in lista_peliculas_saga:
                if (i.url in j.planets):
                    i.episode_id.append(j.title) 
        return self.planets_list
    

    def MatchPersonajes_Planetas(self, lista_personajes):
        """"Este método permite buscar la coincidencia entre los episodios, los personajes y los planetas. Esto a partir de la informacion extraída 
        en las clases D_personajes

        Args:
            lista_personajes (list): lista de personajes de la saga extraída de la clase D_Personajes.

        Returns:
            self.planets_list(list): lista con la información requerida de los planetas luego de haber encontrado la coincidencia con las peliculas.
        """
        for i in self.planets_list:
            for people in lista_personajes:
                if(people.homeworld == i.url):
                    i.people.append(people.name)

        return self.planets_list

    def show_planetas(self):
        """Este método permite imprimir la información en el formato indicado
        """
        for k in self.planets_list:
            k.mostrar_planetas()



 

