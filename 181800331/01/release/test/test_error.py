import unittest
import os

pre = '../../sample/error/'
rst = '../../output/error/'
ori_path = pre + 'query.txt'
sum_path = rst + 'summary.txt'


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('------------------------------')

    def tearDown(self) -> None:
        print('done!')
        print('------------------------------')

    def test_command(self):
        print('testing command format error:')
        os.system('python ../main.py ' + ori_path)

    def test_input_path(self):
        smp_path = './path/error.txt'
        rst_path = rst + 'input_path.txt'

        print('testing path error:')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

    def test_output_path(self):
        smp_path = pre + 'noise.txt'
        rst_path = './path/output_path.txt'

        print('testing path error:')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

    def test_noise(self):
        smp_path = pre + 'noise.txt'
        rst_path = rst + 'noise.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r:
            self.assertEqual(eval(r.read().strip()), 0.0, msg='Error! They have nothing in common!')

    def test_same(self):
        smp_path = ori_path
        rst_path = rst + 'same.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r:
            self.assertEqual(eval(r.read().strip()), 1.0, msg='Error! They are the same documents!')

    def test_blank(self):
        smp_path = pre + 'blank.txt'
        rst_path = rst + 'blank.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r:
            self.assertEqual(eval(r.read().strip()), 0.0, msg='Error! One of the documents is blank!')

    def test_blank2(self):
        ori_path = pre + 'blank.txt'
        smp_path = pre + 'blank.txt'
        rst_path = rst + 'blank2.txt'

        print('testing ' + os.path.basename(smp_path) + ' and ' + os.path.basename(ori_path) + ':')
        os.system('python ../main.py ' + ori_path + ' ' + smp_path + ' ' + rst_path)

        with open(rst_path, 'r', encoding='utf-8') as r:
            self.assertEqual(eval(r.read().strip()), 1.0, msg='Error! They are blank documents!')


if __name__ == '__main__':
    unittest.main()
