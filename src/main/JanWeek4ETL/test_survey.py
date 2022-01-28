"""Anonymous Survey类的测试案例"""
import unittest
from survey import AnonymousServey
class TestAnonymousSurvey(unittest.TestCase):
    # def test_store_single_response(self):
    #     """单个测试的答案被存储"""
    #     do_ = "which thing will you first choose to do?"
    #     my_servey = AnonymousServey(do_)
    #     my_servey.store_response('Python Coding')
    #     self.assertIn('Python Coding',my_servey.responses)
    # def test_store_three_response(self):
    #     """新增功能，连续存储三个答案"""
    #     do_ = "Which three important things will you first choose to do in the morning?"
    #     servey = AnonymousServey(do_)
    #     Things_list = ['Python_code','Word_Link','Fitness']
    #     for i in Things_list:
    #         servey.store_response(i)
    #     for j in Things_list:
    #         self.assertIn(j,servey.responses)
    def setUp(self):
        """创建setUp函数实现优化"""
        do_ = "which thing will you first choose to do?"
        self.my_servey = AnonymousServey(do_)
        self.Things_list = ['Python_code','Word_Link','Fitness']
    def test_store_single_response(self):
        """单个测试的答案被存储,判断是否相同"""
        self.my_servey.store_response(self.Things_list[0])
        self.assertIn(self.Things_list[0],self.my_servey.responses)
    def test_store_three_response(self):
        """新增功能，连续存储三个答案"""
        for i in self.Things_list:
            self.my_servey.store_response(i)
        for j in self.Things_list:
            self.assertIn(j,self.my_servey.responses)
"""测试所选取的对象"""
if __name__ == '__main__':
        unittest.main()