# -*- coding: utf-8 -*-
# @Time    : 2022/1/15 13:58
# @Author  : Junzhou Liu
# @FileName: receipt.py
# @Software: PyCharm
import csv
import traceback
from datetime import datetime


def read_dict():
    product_info_dict = {}
    with open('products.csv') as product_info:
        reader = csv.reader(product_info)
        next(reader)
        for line in reader:
            product_info_dict[line[0]] = line
    return product_info_dict


def main():
    try:
        products_dict = read_dict()
        '''
        for (k, v) in products_dict.items():
            print(k, v)
        '''
        with open('request.csv') as request_info:
            reader = csv.reader(request_info)
            next(reader)
            total_count = 0
            due = 0
            for item in reader:
                # product = products_dict[0o03]
                product = products_dict[item[0]]
                print(f'{product[1]} \t *  {item[1]} :{product[2]}/unit')
                total_count = total_count + int(item[1])
                due = due + int(item[1]) * float(product[2])
            # exceeding requirement: bag purchase
            bag = int(input('How many bags do you want(0.05/each)?'))
            if bag > 0:
                due += bag * 0.05
            elif bag < 0:
                print('Value error! ')
            print('Inkom Emporium')
            # exceeding requirement : discount 10 percent over 10
            print('*** 10% off over $10 ***')
            print(f'Number of Items: {total_count}')
            print(f'Subtotal: {due:.2f}')
            if due >= 10:
                print(f'Discount: {due * 0.1:.2f}')
                due = due * 0.9
                print(f'Subtotal after discount: {due:.2f}')
            print(f'Sales Tax: : {due * 0.06 :.2f}')
            print(f'Total: {due * 1.06:.2f}')
            print('Thank you for shopping at the Inkom Emporium.')
            current_date_and_time = datetime.now()
            print(f"{current_date_and_time:%a %b %d %I:%M:%S %p %Y}")
    except FileNotFoundError:
        print('file not found error')
    except PermissionError:
        print('no permission')
    except KeyError:
        print('key error')
    # exceeding requirement: extra exception handling
    except ValueError as e:
        traceback.print_exc()
        print('value error')
    except BaseException as e:
        traceback.print_exc()


if __name__ == '__main__':
    main()
