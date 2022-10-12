import unittest

# 需要继承unittest的TestCase类
class UnitTest(unittest.TestCase):
    # 方法必须要以test开头
    def test_o1(self):
        print("这是测试方法")
        self.assertIn('a', 'hello')

if __name__ == '__main__':
    # 执行代码
    unittest.main()