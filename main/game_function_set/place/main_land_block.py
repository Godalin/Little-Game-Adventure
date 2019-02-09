#coding=utf-8


'''
Created on 2019.02.02

@author: Godalin
'''


import random


#常量
r_char_dir = {0:'p', 1:'$', 2:'F', 3:'%'}
int_Ten = {0,1,2,3,4,5,6,7,8,9}

         
class MainLandBlock :
    
    
    #add the LGA place for players to start
    
    
    #类常量
    size = 10
    
    
    #类方法
    
    
    def __init__(self) : #构造
        
        #定义表里
        self.__imlb = []
        self.__omlb = []
        
        #初始化表里
        
        #表
        for line in range(10) :
            self.__omlb.append([])
            for row in range(10) :
                self.__omlb[line].append(' ')
        #里
        for line in range(10) :
            self.__imlb.append([])
            for row in range(10) :
                self.__imlb[line].append(' ')
        
        
    def getNewBlock(self) : #随机新建
        
        #插入相异里元素
        for line in range(10) :
            for row in range(10) :
                r_sp = random.randint(0, 3)
                r_char = r_char_dir[r_sp]
                self.__imlb[line][row] = r_char
            
            
    def printBlock(self, io) : #打印版面
        
        #选择表里
        if io == 'o' :
            mlb = self.__omlb
        elif io == 'i' :
            mlb = self.__imlb
        
        #通用打印    
        print()
        print('+-----------------------+')
        print('| |0|1|2|3|4|5|6|7|8|9| |')
        print('|-+-+-+-+-+-+-+-+-+-+-+-|')
        for row in range(10) :
            print('|'+str(row)+'|',end = '')
            for line in range(10) :
                print(mlb[line][row]+'|',end = '')
            print(str(row)+'|')
            print('|-+-+-+-+-+-+-+-+-+-+-+-|')
        print('| |0|1|2|3|4|5|6|7|8|9| |')
        print('+-----------------------+')
        print()

        
    def getBlockData(self) : #获取版面数据
        
        #表数据
        omlbd = ''
        for row in range(10) :
            for line in range(10) :
                omlbd += self.__omlb[line][row]
            omlbd += '\n'
                
        #里数据
        imlbd = ''
        for row in range(10) :
            for line in range(10) :
                imlbd += self.__imlb[line][row]
            imlbd += '\n'
            
        return {'i':imlbd[:], 'o':omlbd[:]}
    
    