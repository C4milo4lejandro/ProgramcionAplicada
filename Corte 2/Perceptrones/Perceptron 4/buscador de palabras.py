#!pip install gensim
#Se deja la línea para importar lo necesario para cada vez que se vuelva a correr

import gensim.downloader
#librería para procesamiento de lenguaje

G_GW_50 = gensim.downloader.load("glove-wiki-gigaword-50")
#Los vectores realizados en un algoritmo con textos de wikipedia y gigaword, son 50 renglones

algebra = G_GW_50.get_vector('king')
algebra
