class People: 
    def __init__(self, height,mass,hair_color,skin_color,eye_color,birth_year,gender,created,edited,name,homeworld,url):
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.created = created
        self.edited = edited
        self.name = name
        self.homeworld = homeworld
        self.url = url
        self.episode_id = []
        self.especie = ''
        self.starships = []
        self.vehicles = []

    def mostrar_personajes(self):
        print(f'-----Nombre del Personaje : {self.name}')
        print(f'Nombre del Planeta de Origen {self.homeworld}')
        print('-----Lista de Episodios en los que aparecen----')
        for j in self.episode_id:
             print(j)
        print(f'Género {self.gender} \nEspecie: {self.especie}')
        print('------Lista de Naves que Utiliza-----')
        for i in self.starships:
            print(i)
        print('---------Lista de Vehiculos que utiliza--------')
        for k in self.vehicles:
            print(k)



