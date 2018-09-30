
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
            cadenaStr = cadena.split(",")
            menor = cadenaStr[0]
            for ele in cadenaStr:
                if ele < menor:
                    menor = ele
            cantEle =len(cadenaStr)
            return [cantEle,int(menor)]

    def mayor(self,cadena):
        if cadena == "":
            return [0,0,0]
        elif len(cadena) == 1:
            return [1,1,1]
        else:
            cadenaStr = cadena.split(",")
            menor = cadenaStr[0]
            mayor = cadenaStr[0]
            for ele in cadenaStr:
                if ele < menor:
                    menor = ele
            for ele in cadenaStr:
                if ele > mayor:
                    mayor = ele
            cantEle = len(cadenaStr)
            return [cantEle, int(menor), int(mayor)]
