import unittest

import HtmlTestRunner

# 查询当前目录下所有以test_开头的py文件
test_dir = './'
suite = unittest.defaultTestLoader.discover(test_dir, 'test_*.py')

# 执行并生成测试报告
runner = HtmlTestRunner.runner.HTMLTestRunner()
runner.run(suite)