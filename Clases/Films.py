class Films:
    def __init__(self,characters, planets,starships,vehicles,species,created,edited,producer,title,episode_id,director,release_date,opening_crawl,url):
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
        print('')
        print(f'------------Titulo: {self.title}------------')
        print(f' \n-> Episodio: {self.episode_id} \n-> Fecha de Lanzamiento: {self.release_date} \n-> Nombre del Director:  {self.director} \n-> "Opening Crawl": {self.opening_crawl} ')
   
