from io import open
import random
archivo = open("BaseRegiones.txt","r")
class Regiones:
    def __init__(self):
        self.regiones =[] 
        while  True:
            lectura = archivo.readline().strip().split(",")
            if lectura[0] == "*":
                break
            self.regiones.append(lectura)
        archivo.close()

    def __str__(self):
        for i in self.regiones:
            print(f"------ID {i[0]}-------")
            print(f"Region:{i[1]}\nClima: {i[2]} \nProducto: {i[3]}\nPoblacion: {i[4]}\nConquistada: {i[5]}")
        return "-------No Hay Mas Regiones--------"

    def AgregarRegion(self):
        print("-----------------Agregar Region---------------------")
        print("----------Ingrese los siguientes datos--------------")
        nombre = input("Nombre: ")
        clima = input("Clima: ")
        producto = input("Producto: ")
        poblacion = input("Poblacion: ")
        conquistado= input("Conquistado: ")
        self.regiones.append([len(self.regiones),nombre, clima, producto,poblacion,conquistado])
        return f"Region Agregada ID{len(self.regiones)-1}"

    def ActualizarHabitantes(self):
        print("-----------------Actualizar Poblacion---------------------")
        while True:
            ID = int(input("Ingrese el ID de la Region: "))
            if ID>0 and ID< len(self.regiones)-1:
                break
            else:
                print("Region no existente,Intente de nuevo")
        dato =input("Ingrese la cantidad actual de poblacion: ")
        self.regiones[ID][4]= dato
    
    def ConquistarRegion(self):
        print("-----------------Conquistar Region---------------------")
        while True:
            ID = int(input("Ingrese el ID de la Region: "))
            if ID>0 and ID< len(self.regiones)-1:
                break
            else:
                print("Region no existente,Intente de nuevo")
        self.regiones[ID][5]= "Si"

    def Conquistado(self,Id):
        if self.regiones[Id][5]=="Si":
            return "Si"
        else: 
            return "No"
    
    def AsignarRegion(self):
        return (random.randint(0,len(self.regiones)-1))

"""reino = Regiones()
reino.ConquistarRegion()
print(reino)"""