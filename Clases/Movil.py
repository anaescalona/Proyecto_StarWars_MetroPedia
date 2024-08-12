class Movil():
    def __init__(self, model,manufacturer,cost_in_credits,length,crew,passengers,max_atmosphering_speed,cargo_capacity,consumables,name,url,pilots = []):
        """Inicializa la clase Movil. Es el constructor de la clase.

            Args:
                model (str): atributo de la clase Movil
                manufacturer (str):atributo de la clase Movil
                cost_in_credits (str): atributo de la clase Movil
                length (str): atributo de la clase Movil
                crew (str):atributo de la clase Movil
                passengers (str): atributo de la clase Movil
                max_atmosphering_speed (str): atributo de la clase Movil
                cargo_capacity (str): atributo de la clase Movil
                consumables (str): atributo de la clase Movil
                name (str): atributo de la clase Movil
                url (str):atributo de la clase Movil
                pilots (list): atributo de la clase Movil
            """
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.cargo_capacity = cargo_capacity
        self.consumables =  consumables
        self.name = name
        self.pilots = pilots
        self.url = url
        


class Starships(Movil):
        def __init__(self, model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, name,url,starship_class,pilots=[]):
          """Inicializa la clase Starships, tomando en cuenta que existe herencia donde la clase padre es Movil. Este el constructor de la clase al añadir los atributos de 
          starships que no están presentes en la clase padre.

                Args:
                model (str): atributo de la clase Movil
                manufacturer (str):atributo de la clase Movil
                cost_in_credits (str): atributo de la clase Movil
                length (str): atributo de la clase Movil
                crew (str):atributo de la clase Movil
                passengers (str): atributo de la clase Movil
                max_atmosphering_speed (str): atributo de la clase Movil
                hyperdrive_rating (str): atributo de la clase Starships(Movil)
                MGLT (str): atributo de la clase Starships(Movil)
                cargo_capacity (str): atributo de la clase Movil
                consumables (str): atributo de la clase Movil
                name (str): atributo de la clase Movil
                url (str): atributo de la clase Movil
                starship_class (str): atributo de la clase Movil
                pilots (list): atributo de la clase Movil
                """
          super().__init__(model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables, name, url,pilots)
          self.starships_class = starship_class
          self.hiperdrive_rating = hyperdrive_rating
          self.MGLT = MGLT

class Vehicles(Movil):
        def __init__(self, model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables,name, url,vehicle_class, films = [] ,pilots=[]):
          """Inicializa la clase Vehicles, tomando en cuenta que existe herencia donde la clase padre es Movil. Este el constructor de la clase al añadir los atributos de 
          Vehicles que no están presentes en la clase padre.

                Args:
                model (str): atributo de la clase Movil
                manufacturer (str):atributo de la clase Movil
                cost_in_credits (str): atributo de la clase Movil
                length (str): atributo de la clase Movil
                crew (str):atributo de la clase Movil
                passengers (str): atributo de la clase Movil
                max_atmosphering_speed (str): atributo de la clase Movil
                cargo_capacity (str): atributo de la clase Movil
                consumables (str): atributo de la clase Movil
                name (str): atributo de la clase Movil
                url (str):atributo de la clase Movil
                vehicle_class (str): atributo de la clase Vehicles(Movil)
                films (list): atributo de la clase Vehicles(Movil)
                pilots (list, optional): atributo de la clase Movil
                """
          super().__init__(model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables, name, url ,pilots)
          self.vehicles_class = vehicle_class
          self.films = films 



