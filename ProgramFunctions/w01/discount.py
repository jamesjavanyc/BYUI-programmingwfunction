# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 22:04
# @Author  : Junzhou Liu
# @FileName: discount.py
# @Software: PyCharm
import datetime
while True:
    price = float(input('Input price:'))
    if price == 0:
        break
    amount = float(input('Input amount:'))
    subtotal = subtotal + price * amount
weekday = datetime.weekday()
discount = 1
tax_rate = 0.06
if (weekday == 1 or weekday == 2) and subtotal >= 50:
    discount = 0.9
after_discount = subtotal * discount
after_tax = after_discount * (1 + tax_rate)
print(f'Subtotal is {subtotal}')
print(f'Discount amount is {subtotal - after_discount}')
print(f'Tax is {after_discount * tax_rate}')
print(f'Total is {after_tax}')
