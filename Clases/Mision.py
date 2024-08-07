class Mision:
    def __init__(self, name, planet, spacecraft, weapons, personas):
        self.m_name=name
        self.planet=planet
        self.spacecraft=spacecraft
        self.weapons=weapons
        self.personas=personas

    def modify(self):
        self.m_name=input()
        self.planet=input()
        self.spacecraft=input()
        self.weapons=input()
        self.personas=input()
    
    def construir(self):
        
        print(f'Bienvenido, Escoja su equipo tactico para la mision...')

  
        while True:
            m_name=input("""Nombre de la mision:
        ---> """)
            if m_name.count > 0:
                break
            else:
                print('El nombre de la misión debe contener por lo menos un carácter...')

        input("""Planeta de destino:
        ---> """)
        input("""Nave a utilizar:
        ---> """)
        input("""Arma a utilizar:
        ---> """)
        input("""Integrantes de la mision:
        ---> """)
