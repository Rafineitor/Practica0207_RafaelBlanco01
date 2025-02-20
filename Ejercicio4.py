#Palabras en URL

import urllib.request
import os

pagina = urllib.request.urlopen("http://textfiles.com/adventure/aencounter.txt")

for line in pagina:
    linea = line.decode("utf-8")
    palabra = linea.replace("*"," ")
    palabra = linea.split(" ")
    palabra = len(palabra)
    print(linea)
    print(palabra)
