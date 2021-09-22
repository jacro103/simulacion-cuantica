import libreria as lc
import unittest

class TestCplxoperations(unittest.TestCase):

    def test(self):
        suma = lc.cplxsum((3, 5),(-2.6, 6.8))
        self.assertAlmostEqual(suma[0], 0.4)
        self.assertAlmostEqual(suma[1], 11.8)



if __name__ == '__main__':
    unittest.main()


import unittest


class TestCplxrest(unittest.TestCase):

        def test(self):
            resta = lc.cplxrest((7, 9), (-4, 8))
            self.assertAlmostEqual(resta[0], 11)
            self.assertAlmostEqual(resta[1], 1)


if __name__ == '__main__':
    unittest.main()

import unittest


class TestCplxrest(unittest.TestCase):

        def test(self):
            multiplicacion = lc.cplxmult((2, 5), (-3, 4))
            self.assertAlmostEqual(multiplicacion[0], -26)
            self.assertAlmostEqual(multiplicacion[1], -7)


if __name__ == '__main__':
    unittest.main()

import unittest


class TestCplxrest(unittest.TestCase):

        def test(self):
            division = lc.cplxdiv((9, 3), (-7, 4))
            self.assertAlmostEqual(division[0], -0.7846153846153846)
            self.assertAlmostEqual(division[1], -0.8769230769230769)


if __name__ == '__main__':
    unittest.main()

import unittest


class TestCplxmol(unittest.TestCase):

        def test(self):
            modulo = lc.cplxmol(3,4)
            self.assertAlmostEqual(modulo, 5.0)



if __name__ == '__main__':
    unittest.main()

import unittest

class TestCplxoperations(unittest.TestCase):

    def test(self):
        conjugado = lc.cplxcon([(6, 3)])
        self.assertAlmostEqual(conjugado[0], 6)
        self.assertAlmostEqual(conjugado[1], -3)

import unittest

class TestCplxpol(unittest.TestCase):

    def test(self):
        polar = lc.cplxpol(4, 7)
        self.assertAlmostEqual(polar[0], 8.06225774829855)
        self.assertAlmostEqual(polar[1], 1.0516502125483738)

if __name__ == '__main__':
    unittest.main()




