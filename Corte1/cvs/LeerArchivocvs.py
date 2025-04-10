import csv

with open('personas.csv', 'r') as file:
    reader = csv.reader(file)
    for fila in reader:
        print(fila)
