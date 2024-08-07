from Mision import Mision

class Con_m:
    def construir(self):
        
        print(f'Bienvenido, Escoja su equipo tactico para la mision...')

  
        while True:
            m_name=input("""Nombre de la mision:
        ---> """)
            if len(m_name) > 0:
                break
            else:
                print('El nombre de la misión debe contener por lo menos un caracter...')
                print()

        print('Escoge el planeta de la mision:')

        dic_planeta=Mision.cargar_csv('planets.csv')
        while True:
            option_planet=input("""Escriba el numero del Planeta de destino:
            ---> """)
            if option_planet in ['1','2','3','4','5','6','7','8','9',"10",'11','12','13']:
                break
            else:
                print('Ingrese un número válido...')
                
        for row in dic_planeta['id']== option_planet:
                planeta=row['name']

        input("""Nave a utilizar:
        ---> """)
        input("""Arma a utilizar:
        ---> """)
        input("""Integrantes de la mision:
        ---> """)
        Mision(m_name,planeta,)

def main():
    mision = Con_m()
    mision.construir()
main()