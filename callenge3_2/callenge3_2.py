# -*- coding: utf-8 -*-

from openpyxl import load_workbook # 可以用来载入已有数据表格
from openpyxl import Workbook # 可以用来处理新的数据表格
import datetime # 可以用来处理时间相关的数据

def combine():
    '''
    该函数可以用来处理原数据文件：
    1. 合并表格并写入的 combine 表中
    2. 保存原数据文件
    '''
    wb = load_workbook('courses.xlsx')
    






def split():
    '''
    该函数可以用来分割文件：
    1. 读取 combine 表中的数据
    2. 将数据按时间分割
    3. 写入不同的数据表中
    '''
    TODO

# 执行
if __name__ == '__main__':
    combine()
    split()

来源: 实验楼
链接: https://www.shiyanlou.com/courses/1140
本课程内容，由作者授权实验楼发布，未经允许，禁止转载、下载及非法传播