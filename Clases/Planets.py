class Planets:
    def __init__(self, diameter, rotation_period, orbital_period, gravity,population,climate, terrain,surface_water,created,edited,name,url):
              self.diameter = diameter
              self.rotation_period = rotation_period
              self.gravity = gravity
              self.population = population
              self.climate = climate
              self.terrain = terrain
              self.surface_water = surface_water
              self.created = created 
              self.edited = edited
              self.name = name
              self.url = url 
              self.orbital_period = orbital_period
              self.episode_id = ''
              self.people = []
    
    def mostrar_planetas(self):
        print('')
        print(f'------------Nombre: {self.name}------------')
        print(f' \n-> Periodo de Orbita: {self.orbital_period} \n-> Periodo de Rotación : {self.rotation_period} \n-> Cantidad de Habitantes:  {self.population} \n-> Tipo de clima: {self.climate} \n-> Episodios en los que aparecen: {self.episode_id}')
        print(f'---- Listado de Personajes Originarios del Planeta -----')
        for people in self.people:
            print(people)
           


