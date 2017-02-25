# -*- coding: UTF-8 -*-

'''
Created on 2017年2月8日

@author: Administrator
广告展示模块测试用例
'''

from appiumTest.PublicClass import clickText,swipeLeft, getScreenShot
import time
'''-----------------------------------定位弹窗框-----------------------------
1、定位弹窗：允许、不允许
2、升级提醒弹窗：取消、升级

 '''
class TanChuangChuLi():
    def tanChuang(self):
        myBoolean=True
        while myBoolean:   
            try:
                if clickText("允许"):                        
                    continue                                      
                elif clickText("不允许"):                        
                    continue
                elif clickText("取消"):                        
                    continue
                elif clickText("升级"):                        
                    continue
                else:
                    print("未弹出权限处理")   
                    myBoolean=False     
            except:
                print("捕获到异常")
                continue
        else:
            print("退出弹框处理")
'''----------------------------------广告展示--------------------------------
多页面滑动切换广告展示：向左滑动，向右滑动，向左向右滑动、向右向左滑动
getScreenShot()为截屏方法
        '''
class HuaDongChuli():
    def HuaDong(self):
        time.sleep(1)
        getScreenShot("进入时默认展示的广告页面")
        swipeLeft(1000)
        time.sleep(1)
        getScreenShot("第一次滑动后的广告页面")
        swipeLeft(1000)
        time.sleep(1)
        getScreenShot("第二次滑动后的广告页面")
        swipeLeft(1000)
        time.sleep(1)
        getScreenShot("第三次滑动后的广告页面")
        
        clickText("登 录")
        