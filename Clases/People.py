class People: 
    def __init__(self, height,mass,hair_color,skin_color,eye_color,birth_year,gender,created,edited,name,homeworld,url):
        """Inicializa la clase People. Es el constructor de la clase. Es importante destacar que dentro de este metodo se encuentran añadidos 
        self.episode_id = []
        self.especie = ''
        self.starships = []
        self.vehicles = []

        Siendo estos utilizados en los apartados relacionados a la API

        Args:
            height (str): atributo de la clase People
            mass (str): atributo de la clase People
            hair_color (str): atributo de la clase People
            skin_color (str): atributo de la clase People
            eye_color (str): atributo de la clase People
            birth_year (str): atributo de la clase People
            gender (str): atributo de la clase People
            created (str): atributo de la clase People
            edited (str): atributo de la clase People
            name (str): atributo de la clase People
            homeworld (str): atributo de la clase People
            url (str): atributo de la clase People
        """
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
        """Permite imprimir la informacion en el formato deseado.
        """
        print('----------------------------------------------------')
        print(f'->Nombre del Personaje : {self.name}')
        print(f'->Nombre del Planeta de Origen: {self.homeworld}')
        print('---Lista de Episodios en los que aparecen---')
        for j in self.episode_id:
            print(j)

        print(f'->Género: {self.gender}')

        if self.especie == '':
            print(f'Especie: El personaje no se encuentra dentro de una clasificación de especie')
        else:
            print(f'->Especie: {self.especie}')
            
        print('---Lista de Naves que Utiliza---')
        if len(self.starships) > 0:
            for i in self.starships:
                print(i)
            print('')
        else: 
            print('Este personaje no utiliza ninguna nave ')
            print('')

        print('---Lista de Vehiculos que utiliza---')
        if len(self.vehicles) > 0:
            for k in self.vehicles:
                print(k)
            print('')
        else: 
            print('Este personaje no utiliza ningun vehiculo ')
            print('')

        print('----------------------------------------------------')