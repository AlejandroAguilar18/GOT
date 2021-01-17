from Regiones import Regiones
class Persona:

    def __init__(self,nombre,edad,estado,region,subdito,numHijos,nombreHijos,tristezas):
        self.nombre = nombre
        self.edad = edad
        self.estado = estado
        self.region=region
        self.subdito = "No"
        self.numHijos = numHijos
        self.nombreHijos = nombreHijos
        self.tristezas = tristezas


    def __str__(self):
        return f"{self.nombre} tiene {self.edad} y es de {self.estado}, viene de la región {self.region} y subdito {self.subdito}\
        tiene {self.numHijos} y sus nombres son {self.nombreHijos}, sus tristezas son {self.tristezas}"