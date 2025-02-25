#Listin telefonico

import os

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

def eliminar(a):
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    with open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/'+a+'.txt', 'r') as file:
        linea = file.readlines()
    with open('C:/Users/rafae/OneDrive/Documentos/GIT_usuarioEduca/Practica0207_GIT-1/'+a+'.txt','w') as file:
        lista = []
        for i in linea:
            if not i.startswith(nombre):
                lista.append(i)
            lista2 = "".join(lista)
        file.write(lista2)

a = input("Ingrese el nombre del fichero: ")

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

    if menu > 3:
        print("Opción incorrecta. Ingrese la opción nuevamente:")