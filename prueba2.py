import csv

with open('planets.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    # Lee y muestra cada fila como un diccionario
    for row in reader:
        print(row)