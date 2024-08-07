class Movil():
    def __init__(self, model,manufacturer,cost_in_credits,length,crew,passengers,max_atmosphering_speed,hyperdrive_rating ,MGLT,cargo_capacity,consumables,name,url,pilots = []):
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.cargo_capacity = cargo_capacity
        self.consumables =  consumables
        self.name = name
        self.pilots = pilots
        self.url = url
        


class Starships(Movil):
        def __init__(self, model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, name,url,starship_class,pilots=[]):
          super().__init__(model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, name, url,pilots)
          self.starships_class = starship_class

class Vehicles(Movil):
        def __init__(self, model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables,name, url,vehicle_class, films = [] ,pilots=[]):
          super().__init__(model, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, name, url ,pilots)
          self.vehicles_class =vehicle_class
          self.films = films 



