import unittest
import os
import sys

sys.path.append('../')
from main import duplicate_check

pre = '../../sample/error/'
ori_path = ''.join([pre, 'query.txt'])


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('------------------------------')

    def tearDown(self) -> None:
        print('done!')
        print('------------------------------')

    @staticmethod
    def test_command():
        print('testing command format error:')
        os.system(' '.join(['python ../main.py', ori_path]))

    @staticmethod
    def test_input_path1():
        smp_path = './path/error.txt'

        print('testing if path exists:')
        duplicate_check([smp_path, ori_path])

    @staticmethod
    def test_input_path2():
        smp_path = '.'

        print('testing if file exists:')
        duplicate_check([ori_path, smp_path])

    @staticmethod
    def test_output_path():
        smp_path = ''.join([pre, 'noise.txt'])
        rst_path = './path/output_path.txt'

        print('testing output path error:')
        os.system(' '.join(['python ../main.py', ori_path, smp_path, rst_path]))

    @staticmethod
    def test_work():
        smp_path = ''.join([pre, 'noise.txt'])
        rst_path = '../../output/work.txt'

        print('testing feasibility:')
        os.system(' '.join(['python ../main.py', ori_path, smp_path, rst_path]))

    def test_noise(self):
        smp_path = ''.join([pre, 'noise.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        self.assertLess(sim, 0.05, msg='Error! They have nothing in common!')

    def test_same(self):
        smp_path = ori_path

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        self.assertEqual(sim, 1.0, msg='Error! They are the same documents!')

    def test_blank(self):
        smp_path = ''.join([pre, 'blank.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        self.assertEqual(sim, 0.0, msg='Error! One of the documents is blank!')

    def test_blank2(self):
        smp_path = ''.join([pre, 'blank.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([smp_path, smp_path])

        self.assertEqual(sim, 1.0, msg='Error! They are blank documents!')


if __name__ == '__main__':
    unittest.main()
