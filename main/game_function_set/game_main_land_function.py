#coding=utf-8


'''
Created on 2019.02.08

@author: Godalin
'''

import os, sys

cwd = os.getcwd()
sep = os.path.sep

sys.path.append(cwd)

from place import main_land_block as MLB

def setMainLand() : #生成主世界
    mlb_ori = MLB.MainLandBlock()
    mlb_ori.getNewBlock()
    return mlb_ori.getBlockData()
