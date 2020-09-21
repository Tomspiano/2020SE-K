import unittest
import os
import sys

sys.path.append('../')
from main import duplicate_check

pre = '../../sample/sim_0.8/'
ori_path = ''.join([pre, 'orig.txt'])
sum_path = '../../output/sim.txt'


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('------------------------------')

    def tearDown(self) -> None:
        print('done!')
        print('------------------------------')

    @staticmethod
    def test_add():
        smp_path = ''.join([pre, 'orig_0.8_add.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('add   : {:.2f}\n'.format(sim))

    @staticmethod
    def test_del():
        smp_path = ''.join([pre, 'orig_0.8_del.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('del   : {:.2f}\n'.format(sim))

    @staticmethod
    def test_dis_1():
        smp_path = ''.join([pre, 'orig_0.8_dis_1.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_1 : {:.2f}\n'.format(sim))

    @staticmethod
    def test_dis_3():
        smp_path = ''.join([pre, 'orig_0.8_dis_3.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_3 : {:.2f}\n'.format(sim))

    @staticmethod
    def test_dis_7():
        smp_path = ''.join([pre, 'orig_0.8_dis_7.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_7 : {:.2f}\n'.format(sim))

    @staticmethod
    def test_dis_10():
        smp_path = ''.join([pre, 'orig_0.8_dis_10.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_10: {:.2f}\n'.format(sim))

    @staticmethod
    def test_dis_15():
        smp_path = ''.join([pre, 'orig_0.8_dis_15.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_15: {:.2f}\n'.format(sim))

    @staticmethod
    def test_mix():
        smp_path = ''.join([pre, 'orig_0.8_mix.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('mix   : {:.2f}\n'.format(sim))

    @staticmethod
    def test_rep():
        smp_path = ''.join([pre, 'orig_0.8_rep.txt'])

        print(' '.join(['testing', os.path.basename(smp_path), 'and', os.path.basename(ori_path)]) + ':')
        sim = duplicate_check([ori_path, smp_path])

        with open(sum_path, 'a', encoding='utf-8') as s:
            s.write('rep   : {:.2f}\n'.format(sim))


if __name__ == '__main__':
    unittest.main()
