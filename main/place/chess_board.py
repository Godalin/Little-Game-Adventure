#coding=utf-8


'''
Created on 2019.02.02

@author: Godalin
'''


import random


#常量
r_char_dir = {0:'p', 1:'$', 2:'F', 3:'%'}
int_Ten = {0,1,2,3,4,5,6,7,8,9}

         
class ChessBoard :
    
    
    #add the LGA place for players to start
    
    
    #类常量
    size = 10
    
    
    #类方法
    
    
    def __init__(self) : #自建
        
        #定义表里
        self.__icb = []
        self.__ocb = []
        
        #初始化表里
        
        #表
        for line in range(10) :
            self.__ocb.append([])
            for row in range(10) :
                self.__ocb[line].append(' ')
        #里
        for line in range(10) :
            self.__icb.append([])
            for row in range(10) :
                self.__icb[line].append(' ')
        
        
    def getNewBoard(self) : #随机新建
        
        #插入相异里元素
        for line in range(10) :
            for row in range(10) :
                r_sp = random.randint(0, 3)
                r_char = r_char_dir[r_sp]
                self.__icb[line][row] = r_char
            
            
    def printBoard(self, io) : #打印版面
        
        #选择表里
        if io == 'o' :
            cb = self.__ocb
        elif io == 'i' :
            cb = self.__icb
        
        #通用打印    
        print()
        print('+-----------------------+')
        print('| |0|1|2|3|4|5|6|7|8|9| |')
        print('|-+-+-+-+-+-+-+-+-+-+-+-|')
        for row in range(10) :
            print('|'+str(row)+'|',end = '')
            for line in range(10) :
                print(cb[line][row]+'|',end = '')
            print(str(row)+'|')
            print('|-+-+-+-+-+-+-+-+-+-+-+-|')
        print('| |0|1|2|3|4|5|6|7|8|9| |')
        print('+-----------------------+')
        print()

        
    def getChessBoardData(self) : #获取版面数据
        
        #表
        ocb = ''
        for row in range(10) :
            for line in range(10) :
                ocb += self.__ocb[line][row]
            ocb += '\n'
                
        #里
        icb = ''
        for row in range(10) :
            for line in range(10) :
                icb += self.__icb[line][row]
            icb += '\n'
            
        return {
            'i':icb[:], 
            'o':ocb[:]
            }
            