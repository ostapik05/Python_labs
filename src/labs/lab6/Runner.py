# from shared.interfaces.RunnerInterface import RunnerInterface
# from labs.lab1.tests.test_calculator import main
#
#
# class Runner(RunnerInterface):
#     @staticmethod
#     def run():
#         print("Running unit tests...")
#         main()
from shared.interfaces.RunnerInterface import RunnerInterface
import unittest
import os

class Runner(RunnerInterface):
    @staticmethod
    def run():
        print("Running unit tests...")
        # Визначаємо шлях до тестів
        test_dir = os.path.join(os.getcwd(), "src", "labs", "lab1", "tests")
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover(start_dir=test_dir, pattern="test_*.py")

        # Запускаємо тести
        test_runner = unittest.TextTestRunner(verbosity=2)
        test_runner.run(test_suite)
