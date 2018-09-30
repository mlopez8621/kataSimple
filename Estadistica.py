
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
        elif len(cadena)==1:
            return [1,1]
        else:
            return [2,1]