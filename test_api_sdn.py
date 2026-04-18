import unittest
from api_sdn import obtener_dispositivo

class PruebasSDN(unittest.TestCase):

    def test_tipo_dato(self):
        datos = obtener_dispositivo(1)
        self.assertIsInstance(datos, dict)

    def test_integridad_atributos(self):
        datos = obtener_dispositivo(1)
        self.assertIn("id", datos)
        self.assertIn("username", datos)

    def test_valor_esperado(self):
        datos = obtener_dispositivo(1)
        self.assertEqual(datos["id"], 1)
        self.assertEqual(datos["username"], "Bret")

if __name__ == "__main__":
    unittest.main()
