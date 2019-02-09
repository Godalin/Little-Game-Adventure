#coding=utf-8


'''
Created on 2019.02.02

@author: Godalin
'''


import time, os, sys


#定义常量
int_Ten = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
sep = os.path.sep
cwd = os.getcwd()


sys.path.append(cwd + sep + 'game_function_set' + sep)


import game_new_world


def getPlayerInputYoN() :#获取玩家键入
    
    while True :
        
        print()
        answer = input()
    
        #y or n
        if answer.lower() in {'y', 'yes'} :
            return True
        elif answer.lower() in {'n', 'no'} :
            return False
        else :
            print()
            print('Not an answer .')
            time.sleep(1)
            print()
            print('Please answer once more .')
            continue
        

def expressPity() : #表达遗憾
    time.sleep(2)
    print('Pity to hear that .')
    print()
    time.sleep(2)
    print('See you next time .')
    print()
    time.sleep(2)
    return False


def askYesOrNo(question) : #询问是否
    
    if question == 'isReadyaToPlay' : #是否开始
        
        print()
        time.sleep(1)
        print('Are you ready ?')
        
        if getPlayerInput() :
            
            print()
            time.sleep(1)
            print('Let\'s do it !')
            print()
            return True
        
        else :
            
            return expressPity()
            
        
    else : #统一回答
        
        print()
        time.sleep(1)
        print('Are you willing to '+question+' ?')
        
        if getPlayerInputYoN():
            
            return True
        
        else :
            
            return False
        
        




