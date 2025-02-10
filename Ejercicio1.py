# Fichero tabla de multiplicar

import os

n = int(input("Introduce un numero del 1 al 10: "))
numero = [1,2,3,4,5,6,7,8,9,10]

def tabla_mult (n):
    for i in range(len(numero[0:10])+1):
        a = i*n
        texto=str(n)+"*"+str(i)+"="+str(a)
        escr_mult(texto)
    return

def fich_mult(n):
    file = open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/tabla'+str(n)+'.txt','w')
    file.write(str(n))

def escr_mult(n):
    a=str(n)
    file = open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/tabla'+a[0]+'.txt','a')
    file.write("\n")
    file.write(n)
    
fich_mult(n)
tabla_mult(n)