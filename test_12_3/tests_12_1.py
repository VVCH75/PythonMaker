import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        r1 = runner.Runner('Ходок')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        r2 = runner.Runner('Бегун')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        r3 = runner.Runner("Ходок2")
        r4 = runner.Runner('Бегун2')
        for i in range(10):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)