#coding=utf-8


'''
Created on 2019.02.03

@author: Godalin
'''


import time, os
from place import chess_board as c_b
import process_function as p_f


def setMainLand() : #生成主世界
    
    main_land = c_b.ChessBoard()
    main_land.getNewBoard()
    return main_land.getChessBoardData()


def newWorld() : #创建新世界
    
    print()
    print('Choose a world name .')
    print()
    name = input()
    
    while True :
        
        #设置路径
        target_path = (os.getcwd()
                       +os.path.sep
                       +'saves'
                       +os.path.sep
                       +'{}'.format(name))
        
        #不存在
        if not os.path.exists(target_path) :
            
            os.makedirs(target_path)
            
            #生成主世界
            main_land = setMainLand()
            main_land_path = (target_path
                         +os.path.sep
                         +'main_land') 
            os.makedirs(main_land_path)
            
            #将主世界存入存档
            #o
            with open(main_land_path
                      +os.path.sep
                      +'o','w') as mlo :
                mlo.write(main_land['o'])
            #i
            with open(main_land_path
                      +os.path.sep
                      +'i','w') as mli :
                mli.write(main_land['i'])
                
            break
        
        #已存在
        else :
            
            time.sleep(1)
            print()
            print('World exists .')
            
            if p_f.askYesOrNo('cover it') : #覆盖
                
                time.sleep(1)
                print()
                print('World name will be {} .'.format(name))
                
                #生成主世界
                main_land = setMainLand()
                main_land_path = (target_path
                                  +os.path.sep
                                  +'main_land') 
            
                #将主世界先删除再存入存档
                #删除
                try :
                    os.remove(main_land_path
                              +os.path.sep
                              +'o')
                    os.remove(main_land_path
                              +os.path.sep
                              +'i')
                except FileNotFoundError :
                    pass
                
                #o
                with open(main_land_path
                          +os.path.sep
                          +'o','w') as mlo :
                    mlo.write(main_land['o'])
                #i
                with open(main_land_path
                          +os.path.sep
                          +'i','w') as mli :
                    mli.write(main_land['i'])
                
                break
            
            elif p_f.askYesOrNo("add a '_'") : #加_
                name += '_'
                continue
            
            