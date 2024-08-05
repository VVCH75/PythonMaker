import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r1 = runner.Runner('Ходок')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = runner.Runner('Бегун')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = runner.Runner("Ходок2")
        r4 = runner.Runner('Бегун2')
        for i in range(10):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)