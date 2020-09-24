import unittest
import os

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.discover(os.getcwd()))

    # f = open('result_all.txt', 'w')
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # f.close()
