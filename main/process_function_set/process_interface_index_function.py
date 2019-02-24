#coding=utf-8


'''
Created on 2019.02.09

@author: Godalin
'''


import time, os, sys

sep = os.path.sep
cwd = os.path.split(os.path.realpath(__file__))[0]
fwd = os.path.abspath(os.path.dirname(cwd) + sep + '.')
interface_path = cwd + sep + 'player_interface' + sep
index = interface_path + 'index'


sys.path.append(fwd + sep + 'game_function_set' + sep)

import game_new_world


sys.path.append(cwd + sep)

import process_interface_chooseFile_function as pic_f


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
                    pic_f.printFileChoose()
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