#程序版本：v1.0
#2025/3/18
#实现在屏幕上显示动态的丽萨如图，在程序中修改相关参数可以修改显示效果
#作者：棉桂星秋

from math import sin
from machine import SoftI2C,Pin,I2C
from ssd1306 import SSD1306_I2C
from time import sleep
#############初始化屏幕并设置参数##################
i2c = I2C(sda=Pin(26), scl=Pin(25))
dp = SSD1306_I2C(128, 64, i2c)

xA=30
yA=30
xw=2
yw=3
v=2
###################测试屏幕#######################
dp.fill(1)
dp.show()
sleep(0.1)
dp.fill(0)
dp.show()
#################开始显示#########################
while 1:
    dp.text('xA=%s'%xA,69,0,1)
    dp.text('yA=%s'%yA,69,8,1)
    dp.text('xw=%s'%xw,69,20,1)
    dp.text('yw=%s'%yw,69,28,1)
    dp.text('v=%s'%v,69,40,1)
    for j in range(1570):
        dp.fill_rect(0,0,60,64,0)
        for i in range(628):
            dp.pixel(int(xA*sin(xw*(i/100+j/100))+30),int(yA*sin(yw*(i/100+j*v/100))+30),1)
        dp.show()
