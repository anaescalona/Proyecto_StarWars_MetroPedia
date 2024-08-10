
import requests as rq 
from Clases.Movil import Vehicles, Starships
from Clases.People import People

class D_Personajes():

    def __init__(self):
        self.lista_personajes = []
        self.resultados_list = []
        self.lista_vehiculos = []
        self.lista_starships = []


    def GetPeople(self):
        """Este método permite obtener la información proveniente de la extensión de la Swapi People.
           De esta manera logrando obtener informacion acerca de los personajes al ingresar en la base de datos de cada uno y 
           almacenando esta informacion en la lista self.lista self.lista_personajes como objeto People. 
           

        Returns:
            self.lista_personajes(list): lista de los personajes de la saga, luego de haber extraído la información y almacenarlo como objetos.
        """
        try: 

            personajes = rq.get("https://www.swapi.tech/api/people/") 
            personajes = personajes.json()

            MAX_personajes = int(personajes['total_records'])

            #se escribe MAX_personajes + 2 debido a que la api dice: total records 82. Sin embargo, existe un personaje nro 83.

            for j in range(1, MAX_personajes + 2):
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

                        self.lista_personajes.append(People(height,mass,hair_color,skin_color,eye_color,birth_year,gender,created,edited,name,homeworld,url))

                    except:
                        continue 
        except:
            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')

        return self.lista_personajes

    def getCharactersByName(self, name):

        """Este método permite hacer el proceso de busqueda de los personajes por su nombre y 
        aún así el usuario no ingrese el nombre completo, el sistema podrá hallarlo. Es importante destacar, 
        que el sistema añade los personajes que hacen coincidencia con la busqueda en la lista "self.resultados_list"

        Args:
            name (str): Nombre del personaje (o parte del nombre) que se hará coincidir con los que se encuentran en la lista self.lista_personajes
        """
        self.resultados_list = [] #reinicia la lista

        for personajes in self.lista_personajes:
            if( str(name).lower() in str(personajes.name).lower() ):
                self.resultados_list.append(personajes)

        if(len(self.resultados_list) <= 0):
            print("Lo sentimos, no se encuentra el personaje") 
        else:
            for data in self.resultados_list:
                data.mostrar_personajes()


    
    def MatchPlanetas(self, lista_planetas):
        """Este método permite buscar la coincidencia entre los personajes y el planeta de origen. 

        Args:
            lista_planetas (list): lista de planetas obtenidos en la clase C_Planetas
        """

        for personas in self.lista_personajes:
            for planeta in lista_planetas:
                if(personas.homeworld == planeta.url):
                    personas.homeworld = planeta.name


    def MatchPeliculas_Personajes(self, lista_peliculas_saga):
        """Este método permite buscar la coincidencia entre los personajes de la saga y las peliculas en las que aparecen

        Args:
            lista_peliculas_saga (lista): lista de peliculas de la saga obtenidas en la clase A_Peliculas.

        Returns:
            self.lista_personajes: lista de personajes luego de haber encontrado la coincidencia 
        """

        for personajes in self.lista_personajes:
            for peliculas in lista_peliculas_saga:
                if (personajes.url in peliculas.characters):
                    personajes.episode_id.append(peliculas.title)

        return self.lista_personajes
    
    def MatchPersonajes_Especies(self, lista_seres_vivos):
        """Este método permite encontrar la coincidencia entre los los personajes y la especie a la que pertenecen.

        Args:
            lista_seres_vivos (list): lista de seres vivos extraída de la clase B_Seres_Vivos

        Returns:
            self.lista_personajes(list): lista de seres vivos una vez realizado el proceso de hacer coincidir ambas informaciones.
        """

        for personajes in self.lista_personajes:
            for species in lista_seres_vivos:
                for people in species.people:
                    if(personajes.name == people):
                        personajes.especie = species.name

        return self.lista_personajes
        
    def getVehicles(self):
        """Este método permite obtener mediante la Api "Swapi" Vehicles las informaciones correspondientes a los pilotos,
          para hacer coincidir el nombre del piloto (el personaje ) con el vehiculo. Y de esta manera obtener el nombre del vehiculo que este utiliza. 

        Returns:
            self.lista_vehiculos: lista de vehiculos luego de haber extraido la información y almacenarla como objeto vehicles.
        """
        try: 
            request_vehicles = rq.get("https://www.swapi.tech/api/vehicles/")
            response_vehicles = request_vehicles.json()
            MAX_VEHICLES = response_vehicles["total_records"]

            for i in range(1, MAX_VEHICLES+1):
                try:
                    request_vehicle = rq.get(f'https://www.swapi.tech/api/vehicles/{i}')
                    response_vehicle = request_vehicle.json()

                    vehiculos =  response_vehicle['result']

                    model = vehiculos["properties"]["model"]
                    manufacturer = vehiculos["properties"]["manufacturer"]
                    cost_in_credits = vehiculos["properties"]["cost_in_credits"]
                    length = vehiculos["properties"]["length"]
                    crew = vehiculos["properties"]["crew"]
                    passengers = vehiculos["properties"]["passengers"]
                    max_atmosphering_speed = vehiculos["properties"]["max_atmosphering_speed"]
                    cargo_capacity = vehiculos["properties"]["cargo_capacity"]
                    consumables = vehiculos["properties"]["consumables"]
                    name = vehiculos["properties"]["name"]
                    url = vehiculos["properties"]["url"]
                    pilots = vehiculos["properties"]["pilots"]
                    vehicle_class = vehiculos["properties"]["vehicle_class"]
                    films = vehiculos["properties"]["films"]

                    self.lista_vehiculos.append(Vehicles(model ,manufacturer ,cost_in_credits,length, crew, passengers, max_atmosphering_speed, cargo_capacity,consumables,name, url,vehicle_class, films,pilots ))
                    print('** VEHICULO CARGADO ***')

                except:
                    continue
        except:
            print("No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet")

        return self.lista_vehiculos
                           

    def getStarships(self): 
        """Este método permite obtener mediante la Api "Swapi" Starships las informaciones correspondientes a los pilotos,
          para hacer coincidir el nombre del piloto (el personaje ) con la nave. Y de esta manera obtener el nombre de la nave que este utiliza. 

        Returns:
            self.lista_starships: lista de naves luego de haber extraido la información y almacenarla como objeto starships.
        """
 
        try:
            request_starships = rq.get("https://www.swapi.tech/api/starships/")
            response_starships = request_starships.json()
            MAX_starships = response_starships["total_records"]

            for j in range(1, MAX_starships+1):
                try: 
                    request_starship= rq.get(f'https://www.swapi.tech/api/starships/{j}')
                    response_starship = request_starship.json()

                    starship = response_starship['result']

                    model = starship["properties"]["model"]
                    manufacturer = starship["properties"]["manufacturer"]
                    cost_in_credits = starship["properties"]["cost_in_credits"]
                    length = starship["properties"]["length"]
                    crew = starship["properties"]["crew"]
                    passengers = starship["properties"]["passengers"]
                    max_atmosphering_speed = starship["properties"]["max_atmosphering_speed"]
                    hyperdrive_rating = starship["properties"]["hyperdrive_rating"]
                    MGLT = starship["properties"]["MGLT"]
                    cargo_capacity = starship["properties"]["cargo_capacity"]
                    consumables = starship["properties"]["consumables"]
                    name = starship["properties"]["name"]
                    url = starship["properties"]["url"]
                    pilots = starship["properties"]["pilots"]
                    starship_class = starship["properties"]["starship_class"]

                    self.lista_starships.append(Starships(model ,manufacturer ,cost_in_credits,length, crew, passengers, max_atmosphering_speed,hyperdrive_rating,MGLT, cargo_capacity,consumables,name, url,starship_class,pilots ))
                    print('** STARTSHIPS CARGADA ***')

                except:
                    continue

        except:
            print('No se pudo consultar la informacion a la Api, por favor consulte su conexión a internet')
        
        return self.lista_starships
    
    def MatchVehicles(self):
        """Este método permite buscar la coincidencia entre los personajes y los vehiculos que estos manejan.

        Returns:
            self.lista_personajes: lista de los personajes luego de haber encontrado la coincidencia de los vehiculos que manejan los personajes.
        """
        for personajes in self.lista_personajes:
            for vehiculos in self.lista_vehiculos:
                
                for data in vehiculos.pilots:
                    if(personajes.url == data):
                        personajes.vehicles.append(vehiculos.name)

        return self.lista_personajes
    
    def MatchStartships(self):
        """Este método permite buscar la coincidencia entre los personajes y los vehiculos que estos manejan.

        Returns:
            self.lista_personajes: lista de los personajes luego de haber encontrado la coincidencia de las naves que manejan los personajes.
        """
        for personajes in self.lista_personajes:
            for startships in self.lista_starships:

                for data in startships.pilots:
                    if(personajes.url == data):
                        personajes.starships.append(startships.name)

        return self.lista_personajes
                      
             
    def mostrar_informacion(self):
        """Este método permite mostrar la información requerida sobre cada personaje
        """
        for j in self.resultados_list:
           j.mostrar_personajes()