'''
给你一字典a，如a={2:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'。
'''
from __future__ import print_function  #让python2使用python3的print
print(*a.keys(),sep=',')

