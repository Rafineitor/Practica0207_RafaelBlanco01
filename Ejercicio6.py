#Listin telefonico

import os

a = input("Ingrese el nombre del fichero: ")

def crear_fich(a):
    file = open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/'+a+'.txt','w')

def consultar(a):
    nombre = input("Ingrese el nombre del cliente a consultar: ")
    file = open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/'+a+'.txt','r')
    linea = file.readlines()
    for i in linea:
        b = i.split(",")
        if b[0] == nombre:
            print("El telefono de",b[0], "es", b[1])

def añadir(a):
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    file = open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/'+a+'.txt','a')
    file.write(nombre+","+telefono+"\n")


crear_fich(a)

while True:
    menu = int(input("""Ingrese una de las siguientes opciones:
                     1) Añadir teléfono de cliente nuevo.
                     2) Consultar teléfono de cliente existente.
                     3) Eliminar teléfono de cliente existente."""))

    if menu == 1:
        añadir(a)
    
    if menu == 2:
        consultar(a)
    
    if menu == 3:
        eliminar(a)