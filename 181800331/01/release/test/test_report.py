import unittest
import os

pre = '../../sample/report/'
rst = '../../output/report/'
smp_path = pre + 'query.txt'
sum_path = rst + 'summary.txt'


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('------------------------------')

    def tearDown(self) -> None:
        print('done!')
        print('------------------------------')

    @staticmethod
    def test_1():
        ori_path = pre + 'orig1.txt'
        rst_path = rst + 'report1.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test1: ' + r.read())

    @staticmethod
    def test_2():
        ori_path = pre + 'orig2.txt'
        rst_path = rst + 'report2.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test2: ' + r.read())

    @staticmethod
    def test_3():
        ori_path = pre + 'orig3.txt'
        rst_path = rst + 'report3.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test3: ' + r.read())

    @staticmethod
    def test_4():
        ori_path = pre + 'orig4.txt'
        rst_path = rst + 'report4.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test4: ' + r.read())

    @staticmethod
    def test_5():
        ori_path = pre + 'orig5.txt'
        rst_path = rst + 'report5.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r, open(sum_path, 'a', encoding='utf-8') as s:
            s.write('test5: ' + r.read())


if __name__ == '__main__':
    unittest.main()
