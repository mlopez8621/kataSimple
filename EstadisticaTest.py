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

    def test_cantElementosVacio_Menor(self):
        self.assertEqual(Estadistica().menor(""),[0,0],"N numeros-menor")

    def test_cantElementosUnNum_Menor(self):
        self.assertEqual(Estadistica().menor("1"), [1, 1], "Un numero, menor 1")

    def test_cantElementosDosNum_Menor(self):
        self.assertEqual(Estadistica().menor("1,2"), [2, 1], "Dos numeros, menor 1")

    def test_cantElementosNNum_Menor(self):
        self.assertEqual(Estadistica().menor("1,2,3,4,5,6,7"), [7, 1], "Un numero, menor 1")

    def test_cantElementosVacio_Menor_Mayor(self):
        self.assertEqual(Estadistica().mayor(""), [0, 0, 0], "Cadena vacia, no hay menor, no hay mayor")

    def test_cantElementosUnNum_Menor_Mayor(self):
        self.assertEqual(Estadistica().mayor("1"), [1, 1, 1], "Un Numero, menor uno, mayor uno")

    def test_cantElementosDosNum_Menor_Mayor(self):
        self.assertEqual(Estadistica().mayor("1,2"), [2, 1, 2], "Un Numero, menor uno, mayor uno")

    def test_cantElementosNNum_Menor_Mayor(self):
        self.assertEqual(Estadistica().mayor("1,2,3,4,5,6,7"), [7, 1, 7], "N numeros, menor 1, mayor 7")