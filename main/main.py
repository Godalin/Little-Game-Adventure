#coding=utf-8


'''
Created on 2019.02.03

@author: Godalin
'''


from place import chess_board as c_b
import process_function as p_f
import sys


#define condition
condition = None


#main loop
while True :
    condition = p_f.printInterface('index')
    p_f.getIndexChoice()