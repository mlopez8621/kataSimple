from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):
    def test_cantElementos(self):
        self.assertEqual(Estadistica().cantElementos(""),[0],"Cadena vacia")

    def test_cantElementosUnNumero(self):
        self.assertEqual(Estadistica().cantElementos("1"),[1],"Un Numero")

    def test_cantElementosDosNum(self):
        self.assertEqual(Estadistica().cantElementos("1,2"),[2],"Numeros 1 y 2")

    def test_cantElementosNNum(self):
        self.assertEqual(Estadistica().cantElementos("1,2,3,4,5,6,7"), [7], "N numeros")

    def test_cantElementosNNum_Menor(self):
        self.assertEqual(Estadistica().menor(""),[0,0],"N numeros-menor")