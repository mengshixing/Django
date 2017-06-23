#'测试驱动开发'（TDD：Test-Driven Development） 单元测试

#引入Python自带的unittest模块
import unittest
from mydict import Mydict

#继承unittest.TestCase
class TestMydict(unittest.TestCase):
    #test开头的方法是测试方法
    def test_init(self):
        print('1')
        d=Mydict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(d,dict)
        
    def test_key(self):
        print('2')
        d=Mydict()
        d['key']='value'
        self.assertEqual(d.key, 'value')
        
    def test_attr(self):
        print('3')
        d=Mydict();
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    
    def test_keyerror(self):
        print('4')
        d=Mydict()
        with self.assertRaises(KeyError):
            value=d['empty']
    
    def test_attrerror(self):
        print('5')
        d=Mydict()
        with self.assertRaises(AttributeError):
            value=d.empty
            
    #setUp与tearDown.会在每个测试方法的前后运行,
    #常用来连接/断开数据库
    def setUp(self):
        print('setup..')
    
    def tearDown(self):
        print('tearDown..')
            
#运行单元测试加下面2行代码或者用指令-m unittest
if __name__=='__main__':
    unittest.main()


