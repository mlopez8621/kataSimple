
class Estadistica:
    def cantElementos(self,cadena):
        if cadena == "":
            return [0]
        else:
            cadenaStr = cadena.split(",")
            return [len(cadenaStr)]

    def menor(self, cadena):
        if cadena == "":
            return [0,0]
        else:
            return [1,1]