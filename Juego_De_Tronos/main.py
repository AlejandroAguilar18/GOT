from Persona import Persona
from Dragones import Dragones
from Guerrero import Guerrero
from Regiones import Regiones
import  random

lista_amorios=[] ## Personas
def inicializacion():
    personas = []
    guerreros = []
    dragones = []
    regiones = Regiones()
    numPersonas = int(input("Cuantas personas quieres inicializar: "))
    for i in range(numPersonas):
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        estado = "Vivo"
        regionOrigen = regiones.AsignarRegion()
        subdito = regiones.Conquistado(regionOrigen)
        numHijos = int(input("Numero de Hijos: "))
        nomHijos = []
        for i in range(numHijos):
            nomHijos.append(input(f"Nombre Hijo {i}:"))
        tristezas = input("¿Que te deprime?: ")
        personas.append(Persona(nombre,edad,estado,regionOrigen,subdito,numHijos,nomHijos,tristezas))
    for i in personas:
        print(i)

    x=int(input("Cuantos guerreros quieres generar: "))
    for i in range(0, x):
        print(f"Generarás {x} guerreros, necesito sus datos: ")
        nombre = input("Nombre: ")
        edad = (input("Edad: "))
        estado = "vivo"
        region = regiones.AsignarRegion()
        subdito = "Si"
        numHijos = int(input("¿Cuantos hijos tiene?: "))
        nombreHijos=[]
        if numHijos>0:
            for i in range(0, numHijos):
                nom=input(f"Nombre Hijo {i}:")
                nombreHijos.append(nom)
        else:
            numHijos=("No tiene hijos")
        tristezas=input("Tristezas: ")
        numMuertes=input("¿Cuantas muertes tienes?: ")
        especialidad=input("¿Cual es tu especialidad?: ")
        print(f"¿Que cargo eres?\nwachiman(1),bachiloca(2),tombo(3),militar(4)")
        cargo=int(input("Cargo:  "))
        interes=input("Estás interesado en la reina? responde SI o NO: ")
        if interes.upper()=="SÍ" or interes.upper()=="SI":
            interesReina=True
        else:
            interesReina=False
        guerreros.append(Guerrero(nombre,edad,estado,region,subdito,numHijos,nombreHijos,tristezas,numMuertes,especialidad,cargo,interesReina))
        
    for i in range(0,len(guerreros)):
        print(guerreros[i])

    numDeagones=int(input("Cuantos dragones quieres iniciar: "))
    for i in range(numDeagones):
        nombre= input("nombre: ")
        edad= int(input("edad: "))
        fuerza= int(input("fuerza: "))
        color= input("color: ")
        numMuertos=int(input("numero de muertos: "))
        comidaFav=input("comida favorita: ")
        dragones.append(Dragones(nombre,edad, fuerza, color, numMuertos, comidaFav))

    for i in range(0,len(dragones)):
        print(dragones[i])
    return(personas,guerreros,dragones,regiones)


def main():

    personas,guerreros,dragones,regiones=inicializacion()
    ##funcion que por cada persona le pregunte a la reina si tuvo un amorio (recorra listas personas)
    ##lista amorios