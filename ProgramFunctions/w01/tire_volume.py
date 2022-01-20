# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 10:49
# @Author  : Junzhou Liu
# @FileName: tire_volume.py
# @Software: PyCharm
import math
from datetime import datetime


class Tire:
    def __init__(self, width, aspect, diameter, price):
        self.width = width
        self.aspect = aspect
        self.diameter = diameter
        self.price = price


def load_price_data():
    price_data = []
    try:
        with open('price.txt', 'rt') as price_data_file:
            lines = price_data_file.readlines()
            for line in lines:
                cur_tire_data = line.split(',')
                # 185,50,14,40 (width aspect diameter price)
                # cur_tire = Tire(cur_tire_data[-4], cur_tire_data[-3], cur_tire_data[-2], cur_tire_data[-1])
                # price_data.append(cur_tire)
                price_data.append(cur_tire_data)
    except BaseException as e:
        print("error! information", e)      # 1打印错误信息
        # if there is no price data.txt in hard drive
        price_data.append(['185', '50', '14', '40'])
        price_data.append(['205', '60', '15', '50'])
        price_data.append(['200', '45', '12', '60'])
        price_data.append(['195', '55', '13', '80'])
    return price_data


def calculate_volume(w, a, d):
    return math.pi * w * w * a * (w * a + 2540 * d) / 10000000000


# week 2
price_info = load_price_data()
# assign 1 Gets the current date from the computer's operating system.
cur_date_time = datetime.now()
width = int(input('Enter the width of the tire in mm (ex 205):').strip())
aspect = int(input('Enter the aspect ratio of the tire (ex 60):').strip())
diameter = int(input('Enter the diameter of the wheel in inches (ex 15):').strip())
volume = calculate_volume(width, aspect, diameter)
buy = False
# exceed requirement if elif else statement
for i in range(4):
    if width == int(price_info[i][0]) and aspect == int(price_info[i][1]) and diameter == int(price_info[i][2]):
        print(f"The tire of the size you want is $"+price_info[i][3])
        buy = (input('Do you want to buy it(yes/no)?') == 'yes')
    elif i == 3 and buy == 0:
        print('Sorry, we don\'t have the tire you want.')
    else:
        continue
# assign 2 Opens a text file named price.txt for appending.
# t->text b->bytes
with open("volumes.txt", "at") as txt_files:
    '''
    assign 3 Appends to the end of the price.txt file one line of text that contains the following five values:
    current date
    width of the tire
    aspect ratio of the tire
    diameter of the wheel
    volume of the tire
    '''
    # file format : 2020-03-18, 185, 50, 14, 24.09
    if buy:
        # exceed requirement : ask phone number
        phone = input("What is your phone number?")
        print(f"{cur_date_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume :.2f}, {phone}", file=txt_files)
    else:
        print(f"{cur_date_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume :.2f}", file=txt_files)


