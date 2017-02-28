# -*- coding: UTF-8 -*-
'''
Created on 2017年2月8日

@author: Administrator
执行测试用例
'''
import unittest,HTMLTestRunner,time
from appiumTest.DisplayAdvertisingTestcases import TanChuangChuLi,HuaDongChuli
from appiumTest.PublicClass import creatdir,getMyTime
'''
unittest.suite单元测试容器
'''
class Execute(unittest.suite):
    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass
        '''
    将系统进入时的弹窗进行封装
    '''
    @classmethod
    def tanChuangchuli(self):
        TanChuangChuLi.tanChuang(self)
        time.sleep(3)
    '''
    将广告展示的滑动方法进行封装
    '''
    @classmethod
    def HuaDongchuli(self):
        HuaDongChuli.HuaDong(self)
        time.sleep(3)

if __name__ == "__main__":      #程序运行入口
    myunit=unittest.suite.TestSuite()  #定义一个单元测试容器
    # myunit.addTest(Execute("tanChuangchuli"))
    myunit.addTest(Execute("HuaDongchuli")) #添加测试用例到测试容器内（将Execute类中的HuaDongchuli方法测试用例添加到测试容器中
    # 获取当前系统时间
    wenjianjia=creatdir()
    mytime=getMyTime()
    myfile="C:/Users/Administrator/Documents/"+wenjianjia+"/result_"+mytime+".html"#定义测试报告存放路径
    fo = open(myfile,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream= fo,
        title='测试报告',
        description='用例执行详情'                           
    ) #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(myunit)  #自动进行测试
    fo.close()
        
        