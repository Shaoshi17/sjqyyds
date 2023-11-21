#作者少世
#此脚本只能刷文章所以需要先打开文章栏目然后点击为文本课程，然后开启全屏运行脚本就可以自动刷分
import time
import random
from pymouse import *
from pykeyboard import *
import pyperclip
from pykeyboard import PyKeyboard
#————————————————————————图像识别技术——————————————————————————————
import pyautogui
import time


def zan():
    time.sleep(0.5)    # 等待 0.5 秒
    #left, top, width, height = pyautogui.locateOnScreen('read1.png')   # 寻找 点击播放的按钮图片；
    left, top, width, height = pyautogui.locateOnScreen('read2.png')   # 寻找 点击选课并播放的按钮图片；
    center = pyautogui.center((left, top, width, height))    # 寻找 图片的中心
    pyautogui.click(center)    # 点击
    print('进入成功')


def Image_recognition():
    ci=0
    while ci<4:
        if pyautogui.locateOnScreen('read2.png') or pyautogui.locateOnScreen('read1.png'):
            zan()   # 调用函数
            break  #只执行一次
        else:
            pyautogui.scroll(-500)    # 本页没有图片后，滚动鼠标；
            print('没有找到目标，屏幕下滚~')
            ci=ci+1



m = PyMouse()
keyboard = PyKeyboard()
#-------------------打开网页调试文本课类型---------------------
# m.click(152, 879)                            #打开收藏在任务栏里面的网页
# time.sleep(random.uniform(1,3))
# keyboard.press_key(keyboard.function_keys[11])   #全屏方 便操作
# time.sleep(random.uniform(1,3))
# m.click(1027, 502)                          #点击课程类型
# time.sleep(random.uniform(1,3))
# m.click(1016, 590)                          #点击文本课
# time.sleep(random.uniform(1,3))
# m.click(1213, 500)                          #搜索
time.sleep(random.uniform(1,5))
def Column_broadcast(): #专栏课程播放
    m.click(697,683)  # 点击第一个文章

def Column_slide():   #划到下一个播放点
    keyboard.press_key(keyboard.down_key)  #下滑
    time.sleep(0.1)
    keyboard.press_key(keyboard.down_key)  # 下滑
    time.sleep(0.1)
    keyboard.press_key(keyboard.down_key)  # 下滑
    time.sleep(0.1)
    keyboard.press_key(keyboard.down_key)  # 下滑
    time.sleep(0.1)

def Read_article():  #阅读文章然后全部关闭后重新进入文章选择
    keyboard.press_key(keyboard.end_key)   #划到最下面
    time.sleep(random.uniform(2, 3))
    keyboard.press_key(keyboard.function_keys[11])  #推出全屏
    time.sleep(random.uniform(2, 3))
    m.click(733,19)  # 叉掉页面
    time.sleep(random.uniform(2, 3))
    m.click(512, 19)  # 叉掉页面
    keyboard.press_key(keyboard.function_keys[11])  # 推出全屏
    time.sleep(random.uniform(2, 3))
def Turn_page():
    keyboard.press_key(keyboard.end_key)
    time.sleep(random.uniform(2, 3))
    m.click(1135,524)  # 点击下一页
    time.sleep(random.uniform(2, 3))
    keyboard.press_key(keyboard.home_key) #回到最顶上
    time.sleep(random.uniform(2, 3))

def all(): #一页
    Column_broadcast()
    time.sleep(random.uniform(2, 3))
    Image_recognition()
    time.sleep(random.uniform(2, 3))
    Read_article()
    time.sleep(random.uniform(2, 3))
    Column_slide()
def alls():  #全部
    all()
    time.sleep(random.uniform(2, 3))
    all()
    time.sleep(random.uniform(2, 3))
    all()
    time.sleep(random.uniform(2, 3))
    all()
    time.sleep(random.uniform(2, 3))
    all()
    time.sleep(random.uniform(2, 3))
    all()
    time.sleep(random.uniform(2, 3))
    all()
    time.sleep(random.uniform(2, 3))
    Turn_page()
alls()
alls()
alls()
alls()
alls()
alls()
alls()
alls()
alls()
alls()
alls()
alls()
alls()