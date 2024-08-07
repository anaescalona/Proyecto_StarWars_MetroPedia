from Clases.Planets import Planets
from C_Planetas import C_Planetas
import os

def main():
    Planeta = C_Planetas()
    Planeta.getPlanetas()
    lista_aux=[]
    for i in Planeta.planets_list:
        Planets.show_name(i)
        lista_aux.append(Planets.show_name(i))
    paginar_lista(lista_aux)
main()


def mostrar_pagina(lista, pagina, elementos_por_pagina=10):
    inicio = pagina * elementos_por_pagina
    fin = inicio + elementos_por_pagina
    for indice,i in enumerate(range(inicio, min(fin, len(lista)))):
        print(f'{indice+1} - {lista[i]}')

def paginar_lista(lista):
    elementos_por_pagina = 10
    pagina = 0
    total_paginas = (len(lista) - 1) // elementos_por_pagina + 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Página {pagina + 1} de {total_paginas}")
        mostrar_pagina(lista, pagina, elementos_por_pagina)

        comando = input("Escribe 'atras' para retroceder, 'adelante' para avanzar, 'salir' para salir: ").strip().lower()
        if comando == 'atras':
            if pagina > 0:
                pagina -= 1
        elif comando == 'adelante':
            if pagina < total_paginas - 1:
                pagina += 1
        elif comando == 'salir':
            break
        else:
            print("Comando no reconocido.")

