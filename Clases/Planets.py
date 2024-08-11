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
              self.episode_id = []
              self.people = []
    
    def mostrar_planetas(self):
        print('')
        print(f'------------Nombre: {self.name}------------')
        print(f' \n-> Periodo de Orbita: {self.orbital_period} \n-> Periodo de Rotación : {self.rotation_period} \n-> Cantidad de Habitantes:  {self.population} \n-> Tipo de clima: {self.climate}')
        print('----Lista de Episodios en los que aparecen----')
        if len(self.episode_id) == 0:
             print('Este planeta no aparece en algún episodio de la saga')
        else: 
            for j in self.episode_id:
             print(j)

        print(f'---- Listado de Personajes Originarios del Planeta ----')
        if(len(self.people) == 0):
             print("No hay personajes en este planeta")
        else:
            unique_items = []
            seen = set()
            for people in self.people:
                if people not in seen:
                    unique_items.append(people)
                    seen.add(people)

            for people in unique_items:
                print(people)


           
