import unittest
import app

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(app.hello(), "Hola, Mundo")

if __name__ == '__main__':
    unittest.main()
