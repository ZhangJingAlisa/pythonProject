# 单元测试：测试函数、类、方法等能不能正常运行完成
import pytest

def setup_module(args):
    print("setup_module", args)
def teardown_module(args):
    print("teardown_module", args)

def setup_function(args):
    print("setup_function", args)
def teardown_function(args):
    print("teardown_function", args)

    import pytest

@pytest.fixture(params=[1, 2, 3])
def init_data(request):
    print("test_data   ", request.param)
    return request.param

def test_not_2(init_data):
    print('test_not_2: %s' % init_data)
    assert init_data != 2

def test_a():
    print('test_a')
    return 1 * 0


def test_b():
    print('test_b')
    return 1 / 0


if __name__ == '__main__':
    pytest.main('--alluredir=allure_files_dir')
