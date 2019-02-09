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


def getPlayerInput() :#获取玩家键入
    
    print()
    answer = input()
    
    #y or n
    if answer.lower() in {'y', 'yes'} :
        return True
    elif answer.lower() in {'n', 'no'} :
        return False
        
    #get point
    else :
        aw_lt = list(answer)
        if (len(aw_lt) == 3) and (aw_lt[1] == ',') :
            return [int(aw_lt[0]), int(aw_lt[2])]
        

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
        
        if getPlayerInput():
            
            return True
        
        else :
            
            return False
        
        
def printInterface(interface) : #打印界面
    with open(cwd + sep + 'player_interface' + sep +'{}'.format(interface),'r') as current_interface :
        print(current_interface.read())
    return interface


def getIndexChoice() : #主页选项
        
    while True :
        
        time.sleep(1)
        print()
        print('Make a choice .')
        
        try :
            
            print()
            choice = int(input())
            
        except ValueError :
            
            time.sleep(1)
            print()
            print('You did not make a choose .')
            continue
        
        else :
        
            #choice
            if choice in {1, 2, 3} :
            
                #new 
                if choice == 1 :
                    game_new_world.newWorld()
                    break
                
                #choose file
                elif choice == 2 :
                    pass
                    break
                
                #exit
                elif choice == 3 :
                    sys.exit()
                    break
            
            #not choice
            else :
                time.sleep(1)
                print()
                print('You did not make a choose .')
                continue 
