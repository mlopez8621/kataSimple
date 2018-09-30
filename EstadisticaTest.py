from unittest import TestCase
from Estadistica import Estadistica


class EstadisticaTest(TestCase):
    def test_cantElementos(self):
        self.assertEqual(Estadistica().cantElementos(""),[0],"Cadena vacia")

    def test_cantElementosUnNumero(self):
        self.assertEqual(Estadistica().cantElementos("1"),[1],"Un Numero")