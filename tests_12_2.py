from runner1 import Tournament, Runner
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Tournament.all_results = {}

    def setUp(self):
        self.r1 = Runner('Усейн', 10)
        self.r2 = Runner('Андрей', 9)
        self.r3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in Tournament.all_results:
            print(Tournament.all_results[key])
        pass

    def test_run(self):
        result = Tournament(90, self.r1, self.r3).start()
        Tournament.all_results[1] = result
    def test_run1(self):
        result = Tournament(90, self.r2, self.r3).start()
        Tournament.all_results[2] = result
    def test_run2(self):
        result = Tournament(90, self.r1, self.r2, self.r3).start()
        Tournament.all_results[3] = result

if __name__ == '__main__':
    unittest.main()
