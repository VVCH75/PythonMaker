import runner
import logging
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = runner.Runner(self)
            print('Тест пройден')
            logging.info(f'"test_walk" выполнен успешно')
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner')


    # def test_run(self):
    #     r2 = runner.first
    #     for i in range(10):
    #         r2.run()
    #     self.assertEqual(r2.distance, 100)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
