# 实测可用ssd1306驱动型号为SSD1315的液晶屏
# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import subprocess
import time

import adafruit_ssd1306
import busio
from PIL import Image, ImageDraw, ImageFont
from board import SCL, SDA


class SSD1306:

    def __init__(self, pixel_width, pixel_height):
        # 创建I2C接口。
        self.draw = None
        i2c = busio.I2C(SCL, SDA)

        # 创建SSD1306 OLED类。
        # 前两个参数是像素宽度和像素高度。
        # ssd1315的像素为128*64
        self.disp = adafruit_ssd1306.SSD1306_I2C(pixel_width, pixel_height, i2c)

        # 清空屏幕.
        self.disp.fill(0)
        self.disp.show()

        # 为绘图创建空白图像
        # 确保为1位颜色创建模式为“1”的图像。
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("1", (self.width, self.height))

        # 获取要在图像上绘制的绘图对象。
        self.draw = ImageDraw.Draw(self.image)

        # 绘制一个黑色填充框以清除图像。
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        # 画一些形状。
        # 首先定义一些常量，以便轻松调整形状大小。
        padding = -2
        self.top = padding
        bottom = self.height - padding
        # 从左向右移动，跟踪绘制形状的当前x位置。
        self.x = 0

        # 加载默认字体。
        self.font = ImageFont.load_default()
        # 使用汉仪颜楷字体
        # self.font = ImageFont.truetype('/home/pi/Code/ssd1306/HanYiYanKaiW.ttf', 9)
        # 使用华康简仿宋字体
        # self.font = ImageFont.truetype('/home/pi/Code/ssd1306/HuaKangJianFangSong.ttf', 14)
        # 或者加载TTF字体。确保.ttf字体文件位于
        # font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

    # 从pixel像素宽处，写普通字符串
    # string：字符串 str
    # pixel：像素 int
    def print_line_normal_string(self, string, pixel):
        self.draw.text((self.x, self.top + pixel), string, font=self.font, fill=255)

    # 从pixel像素宽处，写捕获响应执行cmd命令的与string拼接后的字符串
    # string：参与拼接的字符串 str
    # cmd：cmd命令 str
    # pixel：像素 int
    def print_line_cmd(self, string, cmd, pixel):
        try:
            cmd = cmd
            result = subprocess.check_output(cmd, shell=True).decode("utf-8")
            self.draw.text((self.x, self.top + pixel), string + result, font=self.font, fill=255)
        except Exception as e:
            print("用户自定义Exception：cmd命令错误")

    # 绘制一个黑色填充框以清除图像
    def clear_image(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

    # 显示图像
    # time：系统sleep() int float
    def show(self, _time):
        self.disp.image(self.image)
        self.disp.show()
        time.sleep(_time)

    # while True:
    #     # 绘制一个黑色填充框以清除图像。
    #     draw.rectangle((0, 0, width, height), outline=0, fill=0)
    #
    #     # 用于系统监控的Shell脚本：
    #     cmd = "hostname -I | cut -d' ' -f1"
    #     IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
    #     cmd = 'cut -f 1 -d " " /proc/loadavg'
    #     CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    #     cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    #     MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    #     cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    #     Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    #
    #     # 书写四行文字。
    #     # 将ssd1315的像素为宽64分为4份
    #     draw.text((x, top + 0), "IP: " + IP, font=font, fill=255)
    #     draw.text((x, top + 16), "CPU load: " + CPU, font=font, fill=255)
    #     draw.text((x, top + 32), MemUsage, font=font, fill=255)
    #     draw.text((x, top + 50), Disk, font=font, fill=255)
    #
    #     # 显示图像。
    #     disp.image(image)
    #     disp.show()
    #     time.sleep(0.1)
