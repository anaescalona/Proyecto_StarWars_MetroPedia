class Species:
    def __init__(self,classification, designation, average_lifespan, average_height, hair_colors,skin_colors,eye_colors,homeworld, language, created,edited,name,url,people = []):
        self.classification = classification
        self.designation = designation
        self.average_lifespan = average_lifespan
        self.average_height = average_height
        self.hair_colors = hair_colors
        self.skin_colors = skin_colors
        self.eye_colors = eye_colors
        self.homeworld = homeworld
        self.language = language
        self.created = created
        self.edited = edited
        self.name = name
        self.url = url
        self.people = people
        self.episode_id = [] 

    def mostrar_especie(self):
        print('')
        print(f'------------Nombre: {self.name}------------')
        print(f' \n-> Altura: {self.average_height} \n-> Clasificación: {self.classification} \n-> Planeta de Origen:  {self.homeworld} \n-> Lengua Materna: {self.language} ') 
        print('---Listado de Episodios en los que aparece---')
        
        for i in self.episode_id:
            print(i)

        print(f'---- Personajes que pertenecen a la Especie -----')
        for people in self.people:
            print(people)
        
        


