class Dragones:
    def __init__(self,nombre,edad,fuerza,color,mumMuertos,comidaFav):
        self.nombre=nombre
        self.edad=edad
        self.fuerza=fuerza
        self.color=color
        self.numMuertos=mumMuertos
        self.comidaFav=comidaFav
    def Matar(self,personasAsesinadas):
        self.numMuertos+=personasAsesinadas
    def Alimentar(self,Alimento): #Esta saludable XD
        return f"Roar roawr"
    def Ejercitar(self,tiempoVuelo): #Depende del tiempo de vuelo aumentara su fuerza
        if tiempoVuelo<0:
            print("No hay tiempos negativos")
        elif tiempoVuelo==0:
            pass
        elif tiempoVuelo>=0 and tiempoVuelo<12:
            self.fuerza+=2
        elif tiempoVuelo>=12:
            self.fuerza+=4
    def __str__(self):
        return f"El dragon {self.nombre}, es de color {self.color}, tiene {self.edad} años, tiene fuerza de {self.fuerza},\
        ha asesinado a {self.numMuertos} personas y su comida favorita es {self.comidaFav}"