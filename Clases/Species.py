class Species:
    def __init__(self,classification, designation, average_lifespan, average_height, hair_colors,skin_colors,eye_colors,homeworld, language, created,edited,name,url,people = []):
        """Inicializa la clase People. Es el constructor de la clase. Es importante destacar que dentro de este metodo se encuentran añadidos 
        self.episode_id = []

        Siendo este utilizado en los apartados relacionados a la API

        Args:
            classification (str): atributo de la clase Species
            designation (str): atributo de la clase Species
            average_lifespan (str): atributo de la clase Species
            average_height (str): atributo de la clase Species
            hair_colors (str): atributo de la clase Species
            skin_colors (str): atributo de la clase Species
            eye_colors (str): atributo de la clase Species
            homeworld (str): atributo de la clase Species
            language (str): atributo de la clase Species
            created (str): atributo de la clase Species
            edited (str): atributo de la clase Species
            name (str): atributo de la clase Species
            url (str): atributo de la clase Species
            people (list): atributo de la clase Species
        """
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
        """Imprime la información en el formato deseado.
        """
        print('')
        print(f'------------Nombre: {self.name}------------')
        print(f' \n-> Altura: {self.average_height} \n-> Clasificación: {self.classification} \n-> Planeta de Origen:  {self.homeworld} \n-> Lengua Materna: {self.language} ') 
        print('---Listado de Episodios en los que aparece---')
        
        for i in self.episode_id:
            print(i)

        print(f'---- Personajes que pertenecen a la Especie -----')
        for people in self.people:
            print(people)
        
        


