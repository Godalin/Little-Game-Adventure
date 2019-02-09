#coding=utf-8


'''
Created on 2019.02.08

@author: Godalin

'''


import os, sys, time
import game_main_land_function as gml_f
import game_save_file_function as gsf_f

sep = os.path.sep
cwd = os.getcwd()
fwd = os.path.abspath(os.path.dirname(cwd) + sep + ".")


sys.path.append(fwd + sep)

import process_function as pcs_f


def isIncludeSep(word) : #判断/\
    if not (('/' in word) or ('\\' in word)) :
        return True
    else :
        return False
    

def newWorld() : #创建新世界
    
    #save文件夹有关
    gsf_f.setSave()
    
    #寒暄
    print()
    print("Name can not include '\\'s or '/'s .")
    time.sleep(1)
    print()
    print('Choose a world name .')
    
    
    #去除/\
    while True :
        print()
        name = input()
        if isIncludeSep(name) :
            break
        else :
            print()
            print('Name is not available .')
            time.sleep(1)
            print()
            print('Choose another name .')
            continue
            
        
    #重名处理
    while True :
        
        #设置（重置）世界路径
        world_path = (fwd + sep + 'save' + sep + '{}'.format(name))
        
        
        #不存在
        if not os.path.exists(world_path) :
            
            os.makedirs(world_path)
            
            #生成主世界
            
            #新建一个区块及其文件夹
            main_land = gml_f.setMainLand()
            main_land_path = (world_path + sep + 'main_land') 
            os.makedirs(main_land_path)
            #设置i，o路径
            opath = main_land_path + sep + 'o'
            ipath = main_land_path + sep + 'i'

            #将主世界存入存档
            
            #o
            with open(opath, 'w') as mlo :
                mlo.write(main_land['o'])
            #i
            with open(ipath, 'w') as mli :
                mli.write(main_land['i'])
            #完成
            break
        
        
        #已存在
        else :
            
            #寒暄
            print()
            print('World exists .')

            
            #覆盖
            
            #询问是否
            if pcs_f.askYesOrNo('cover it') :
                
                #寒暄
                print()
                print('World name will be {} .'.format(name))
                
                #生成主世界
                main_land = gml_f.setMainLand()
                main_land_path = (world_path + sep + 'main_land')
                
                #判断main_world文件夹
                if not os.path.exists(main_land_path) :
                    os.makedirs(main_land_path)
                else :
                    pass
                
                #设置i，o路径
                opath = main_land_path + sep + 'o'
                ipath = main_land_path + sep + 'i' 
            
                #将主世界先删除再存入存档
                
                #删除
                try :
                    os.remove(opath)
                    os.remove(ipath)
                    
                except FileNotFoundError :
                    pass
                
                #o
                with open(main_land_path + sep + 'o', 'w') as mlo :
                    mlo.write(main_land['o'])
                #i
                with open(main_land_path + sep + 'i', 'w') as mli :
                    mli.write(main_land['i'])
                
                break
            
            elif pcs_f.askYesOrNo("add a '_' after it") : #加_
                name += '_'
                continue
            
            else :
                break
            