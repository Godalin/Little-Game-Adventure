#coding=utf-8


'''
Created on 2019.02.09

@author: Godalin
'''


import time, os, sys

sep = os.path.sep
cwd = os.path.split(os.path.realpath(__file__))[0]
save_path = os.path.abspath(os.path.dirname(cwd) + sep + '..') + sep +'save'


fileChoose_path = cwd + sep + 'player_interface' + sep + 'fileChoose' + sep
fileChooseT = fileChoose_path + 'fileChooseTop'
fileChooseB = fileChoose_path + 'fileChooseBottom'


def getFileList() :
    
    fileList = []
    
    for filename in os.listdir(save_path):
        if not (os.path.isdir(filename)):
            fileList.append(filename)
    return fileList


def printFileChoose() :

    #print T
    with open(fileChooseT, 'r') as fCT :
        print(fCT.read())
    
    #print Files
    fileList = getFileList()
    for num in range(len(fileList)) :
        fileName = fileList[num]
        fileNameLen = len(fileName)
        print('|' + ' ' * 8 + 
              '[' + ' ' * 3 + fileName + (' ' * (29 - fileNameLen)) + 
              '[' + ' ' * (3 - len(str(num))) + str(num) + 
              ']' + ' ' * 3 + 
              ']' + ' ' * 8 + 
              '|')
        
    #print B
    with open(fileChooseB, 'r') as fCB :
        print(fCB.read())
