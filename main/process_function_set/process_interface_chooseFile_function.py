#coding=utf-8


'''
Created on 2019.02.09

@author: Godalin
'''


import time, os, sys

sep = os.path.sep
cwd = os.path.split(os.path.realpath(__file__))[0]
fwd = os.path.abspath(os.path.dirname(cwd) + sep + '.')

fileChoose_path = cwd + sep + 'player_interface' + sep + 'fileChoose' + sep
fileChooseT = fileChoose_path + 'fileChooseTop'
fileChooseB = fileChoose_path + 'fileChooseBottom'

def printFileChoose() :
    
    
    #print T
    with open(fileChooseT, 'r') as fCT :
        print(fCT.read())
        
    #print B
    with open(fileChooseB, 'r') as fCB :
        print(fCB.read())
