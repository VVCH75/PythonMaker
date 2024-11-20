import unittest
import tests_12_1
import tests_12_2

MegaTest = unittest.TestSuite()
MegaTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
MegaTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(MegaTest)