from Persona import Persona
class Guerrero(Persona):

    cargos=["wachiman","bachiloca","tombo","militar"] #Cargos a los cuales puede acceder

    def __init__(self,nombre="No especificado",edad="No especificado",estado="No especificado",region="No especificado",subdito="No especificado",numHijos="No especificado",nombreHijos="No especificado",tristezas="No especificado",numMuertes="No especificado",
            especialidad="No especificado",cargo="No especificado",interesReina="No especificado"):
        Persona.__init__(self,nombre,edad,estado,region,subdito,numHijos,nombreHijos,tristezas)
        self.numMuertes=numMuertes
        self.especialidad=especialidad
        self.cargo = self.cargos[cargo-1]
        self.interesReina=interesReina
        if int(self.numMuertes)>=600:  #Dependiendo se las muestres va adespertar el interes de la reina o no
            self.interesReina=True
        else:
            self.interesReina=False

    def Matar(self,numero): #Aumenta el numero de muertes
            self.numMuertes+=numero

    def CambiarCargo(self): #Aumentara o disminuira su cargo de acuerdo a su numero de muertes
        if self.numMuertes<0:
            print("No puede tener muertes negativas")
        elif self.numMuertes>=0 and self.numMuertes<150:
            self.cargo=self.cargos[0]
            return f"Su nuevo cargo es {self.cargo}"
        elif self.numMuertes>=150 and self.numMuertes<300:
            self.cargo=self.cargos[1]
            return f"Su nuevo cargo es {self.cargo}"
        elif self.numMuertes>=300 and self.numMuertes<450:
            self.cargo=self.cargos[2] 
            return f"Su nuevo cargo es {self.cargo}"        
        elif self.numMuertes>=450:
            self.cargo=self.cargos[3]
            return f"Su nuevo cargo es {self.cargo}"   

    def _str_(self):
            return f"El guerrero {self.nombre} tiene {self.edad} años, ha matado a {self.numMuertes}, su especialidad es {self.especialidad}\
                tiene el cargo de {self.cargo} y el interes de la reina es={self.interesReina}"


