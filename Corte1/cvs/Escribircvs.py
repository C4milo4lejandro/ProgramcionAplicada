import csv

personas=[
         ['Catagod','Andrea','Garcia','Leon',],
         ['Camilo','Alejandro','Camelo','Cardona',],
         ['Martha','Lucia','Cardona','Coy',],
         ['Wilson','Octavio','Camelo','Mancera',],
]
with open ('personas.csv','w', newline='') as file:
    writer = csv.writer(file,delimiter = ',')
    writer.writerows(personas)
