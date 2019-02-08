#coding=utf-8


'''
Created on 2019.02.03

@author: Godalin
'''


import process_function as p_f_
import sys


#define condition
condition = None


#main loop
while True :
    condition = p_f_.printInterface('index')
    p_f_.getIndexChoice()