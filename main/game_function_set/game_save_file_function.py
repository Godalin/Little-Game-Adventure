#coding=utf-8


'''
Created on 2019.02.09

@author: Godalin
'''


import os


#定义常量
sep = os.path.sep
cwd = os.path.split(os.path.realpath(__file__))[0]
ffwd = os.path.abspath(os.path.dirname(cwd) + sep +'..')


#定义save路径
save_path = ffwd + sep + 'save'
print(save_path)


def setSave() :
    
    
    #判断是否存在
    def isSaveExist() :
        #是（不存在，N）
        if not os.path.exists(save_path) :
            return True
        #否（存在，E）
        else :
            return False
    
    if isSaveExist() :
        #是，创建
        os.makedirs(save_path)
    else :
        #否，不创建
        pass
    
    #返回save路径
    return save_path
    
