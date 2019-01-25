import allure
class Test_Abc:
    @allure.step(title="这是第一个测试用例aa")
    def test_aa(self):
        print("---->test_aa")
        assert True
    @allure.step(title="这是第二个测试用例bb")
    def test_bb(self):
        print("---->test_bb")
        assert True