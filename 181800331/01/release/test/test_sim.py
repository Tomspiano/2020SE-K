import unittest
import os

pre = '../../sample/sim_0.8/'
rst = '../../output/sim_0.8/'
ori_path = pre + 'orig.txt'
sum_path = rst + 'summary.txt'


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('------------------------------')

    def tearDown(self) -> None:
        print('done!')
        print('------------------------------')

    @staticmethod
    def test_add():
        smp_path = pre + 'orig_0.8_add.txt'
        rst_path = rst + 'add.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('add   : ' + r.read())

    @staticmethod
    def test_del():
        smp_path = pre + 'orig_0.8_del.txt'
        rst_path = rst + 'del.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('del   : ' + r.read())

    @staticmethod
    def test_dis_1():
        smp_path = pre + 'orig_0.8_dis_1.txt'
        rst_path = rst + 'dis_1.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_1 : ' + r.read())

    @staticmethod
    def test_dis_3():
        smp_path = pre + 'orig_0.8_dis_3.txt'
        rst_path = rst + 'dis_3.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_3 : ' + r.read())

    @staticmethod
    def test_dis_7():
        smp_path = pre + 'orig_0.8_dis_7.txt'
        rst_path = rst + 'dis_7.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_7 : ' + r.read())

    @staticmethod
    def test_dis_10():
        smp_path = pre + 'orig_0.8_dis_10.txt'
        rst_path = rst + 'dis_10.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_10: ' + r.read())

    @staticmethod
    def test_dis_15():
        smp_path = pre + 'orig_0.8_dis_15.txt'
        rst_path = rst + 'dis_15.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('dis_15: ' + r.read())

    @staticmethod
    def test_mix():
        smp_path = pre + 'orig_0.8_mix.txt'
        rst_path = rst + 'mix.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('mix   : ' + r.read())

    @staticmethod
    def test_rep():
        smp_path = pre + 'orig_0.8_rep.txt'
        rst_path = rst + 'rep.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('rep   : ' + r.read())


if __name__ == '__main__':
    unittest.main()
