# prueba.py
import unittest
import test_calculadora  # Importa el archivo de pruebas

if __name__ == "__main__":
    print("\n=== 🔍 Iniciando pruebas unitarias de calculadora ===\n")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_calculadora)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    print("\n=== ✅ Todas las pruebas finalizaron correctamente ===\n")
