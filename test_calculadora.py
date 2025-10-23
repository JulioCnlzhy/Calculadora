# test_calculadora.py
import unittest
import calculadora

class TestSumar(unittest.TestCase):
    def test_sumar_positivos(self):
        resultado = calculadora.sumar(3, 4)
        self.assertEqual(resultado, 7)
        print("✅ sumar_positivos -> OK")

    def test_sumar_negativos(self):
        resultado = calculadora.sumar(-2, -3)
        self.assertEqual(resultado, -5)
        print("✅ sumar_negativos -> OK")

    def test_sumar_mixto(self):
        resultado = calculadora.sumar(-2, 3)
        self.assertEqual(resultado, 1)
        print("✅ sumar_mixto -> OK")


class TestRestar(unittest.TestCase):
    def test_restar_positivos(self):
        resultado = calculadora.restar(10, 5)
        self.assertEqual(resultado, 5)
        print("✅ restar_positivos -> OK")

    def test_restar_negativos(self):
        resultado = calculadora.restar(-4, -2)
        self.assertEqual(resultado, -2)
        print("✅ restar_negativos -> OK")

    def test_restar_mixto(self):
        resultado = calculadora.restar(5, -3)
        self.assertEqual(resultado, 8)
        print("✅ restar_mixto -> OK")


class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_positivos(self):
        resultado = calculadora.multiplicar(4, 3)
        self.assertEqual(resultado, 12)
        print("✅ multiplicar_positivos -> OK")

    def test_multiplicar_negativos(self):
        resultado = calculadora.multiplicar(-2, -3)
        self.assertEqual(resultado, 6)
        print("✅ multiplicar_negativos -> OK")

    def test_multiplicar_mixto(self):
        resultado = calculadora.multiplicar(-2, 4)
        self.assertEqual(resultado, -8)
        print("✅ multiplicar_mixto -> OK")


class TestDividir(unittest.TestCase):
    def test_dividir_positivos(self):
        resultado = calculadora.dividir(10, 2)
        self.assertEqual(resultado, 5)
        print("✅ dividir_positivos -> OK")

    def test_dividir_negativos(self):
        resultado = calculadora.dividir(-9, -3)
        self.assertEqual(resultado, 3)
        print("✅ dividir_negativos -> OK")

    def test_dividir_mixto(self):
        resultado = calculadora.dividir(-8, 2)
        self.assertEqual(resultado, -4)
        print("✅ dividir_mixto -> OK")

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            calculadora.dividir(5, 0)
        print("✅ dividir_por_cero -> OK")
