import runner
import logging
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = runner.Runner('Вася', -5)
            print('Тест пройден')
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 100)
        except ValueError:
            logging.warning(f'Неверная скорость для Runner"', exc_info=True)


    def test_run(self):
        try:
            r2 = runner.Runner(10)
            logging.info(f'"test_run" выполнен успешно')
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner"', exc_info=True)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')
if __name__ == '__main__':
    pass