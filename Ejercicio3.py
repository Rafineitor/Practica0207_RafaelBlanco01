#Linea del fichero

#Fichero tabla de multiplicar 2

import os

n = int(input("Ingrese un numero del 1 al 10: "))
m = int(input("Ingrese otro numero del 1 al 10: "))

if os.path.isfile('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/tabla'+str(n)+'.txt'):
    file = open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/tabla'+str(n)+'.txt','r')
    linea = file.readlines()
    print("El fichero si existe")
    print(linea[m])
else:
    print("El fichero no existe")