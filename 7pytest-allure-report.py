import allure
import pytest

@allure.feature('登录模块')   # 标注模块/class
class TestLogin():
    def test_success(self):
        """this test succeeds"""
        assert True

    @allure.story('登录失败')   # 标注方法/测试用例，在feature之下，父子关系
    def test_failure(self):
        with allure.step('点击用户名'):    #标注具体的测试步骤
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('点击登录之后失败'):
            assert '1' == 1
            print('登录失败')

        """this test fails"""
        pass


    def test_skip(self):
        """this test is skipped"""
        pytest.skip('for a reason!')


    def test_broken(self):
        raise Exception('oops')

    @allure.link('http://www.baidu.com')
    def test_with_link(self):
        print('加了连接的测试')
        pass