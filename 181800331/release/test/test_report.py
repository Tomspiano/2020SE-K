import unittest
import os
import sys

sys.path.append('../')
from main import duplicate_check

pre = '../../sample/report/'
smp_path = ''.join([pre, 'query.txt'])
sum_path = '../../output/report.txt'


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('------------------------------')

    def tearDown(self) -> None:
        print('done!')
        print('------------------------------')

    @staticmethod
    def test_1():
        ori_path = ''.join([pre, 'orig1.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test1: {:.2f}\n'.format(sim))

    @staticmethod
    def test_2():
        ori_path = ''.join([pre, 'orig2.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test2: {:.2f}\n'.format(sim))

    @staticmethod
    def test_3():
        ori_path = ''.join([pre, 'orig3.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test3: {:.2f}\n'.format(sim))

    @staticmethod
    def test_4():
        ori_path = ''.join([pre, 'orig4.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test4: {:.2f}\n'.format(sim))

    @staticmethod
    def test_5():
        ori_path = ''.join([pre, 'orig5.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test5: {:.2f}\n'.format(sim))


if __name__ == '__main__':
    unittest.main()
