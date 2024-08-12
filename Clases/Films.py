class Films:
    def __init__(self,characters, planets,starships,vehicles,species,created,edited,producer,title,episode_id,director,release_date,opening_crawl,url):
        """Inicializa la clase Films. Es el constructor de la clase. 

        Args:
            characters (str): atributo de la clase films 
            planets (str): atributo de la clase films
            starships (str): atributo de la clase films
            vehicles (str): atributo de la clase films
            species (str): atributo de la clase films
            created (str): atributo de la clase films
            edited (str): atributo de la clase films
            producer (str): atributo de la clase films
            title (str): atributo de la clase films
            episode_id (str): atributo de la clase films
            director (str): atributo de la clase films
            release_date (str): atributo de la clase films
            opening_crawl (str): atributo de la clase films
            url (str): atributo de la clase films
        """
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.created = created
        self.edited = edited
        self.producer = producer 
        self.title = title
        self.episode_id = episode_id
        self.director = director 
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.url = url

    def mostrar_pelicula(self):
        """Permite mostrar en el formato indicado la información requerida
        """
        print('')
        print(f'------------Titulo: {self.title}------------')
        print(f' \n-> Episodio: {self.episode_id} \n-> Fecha de Lanzamiento: {self.release_date} \n-> Nombre del Director:  {self.director} \n-> "Opening Crawl": {self.opening_crawl} ')
   
