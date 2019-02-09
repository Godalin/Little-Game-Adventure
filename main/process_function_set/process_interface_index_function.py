#coding=utf-8


'''
Created on 2019.02.09

@author: Godalin
'''


import time, os, sys

cwd = os.getcwd()
sep = os.path.sep

interface_path = cwd + sep + 'process_function_set' + sep + 'player_interface' + sep
index = interface_path + 'index'

sys.path.append(cwd)

from game_function_set import game_new_world


def printIndex() : #打印主界面
    with open(index, 'r') as Index :
        print(Index.read())


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