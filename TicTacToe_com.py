#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import copy
import itertools
import random
#import time
#import math


# In[7]:



def tttshow(ox=None):
    '''显示棋盘，参数是棋盘矩阵'''
    #'''打印列标号'''
    print("{0:^5}".format('x\y'), end='') # 5个字符
    for j in range(ox.shape[1]):
        print("{0:^5}".format(j+1), end='') # 5个字符          
    print('\n')  # 换行,打印空行        
      
    #'''打印棋盘'''            
    for i in range(ox.shape[0]):        #行数
        #'''打印行标号'''
        print("{0:^5}".format(i+1), end='') # 5个字符

        #'''打印该行棋盘'''    
        for j in range(ox.shape[1]):
            if ox[i][j] == 0:    #未落子  5个字符
                print("{0:^5}".format('~'), end='')
            elif ox[i][j] == 1:   # x 落子  5个字符
                print("{0:^5}".format('X'), end='')
            elif ox[i][j] == -1:  # o 落子
                print("{0:^5}".format('O'), end='') 
        print('\n')  
                

def ttt_simu(ttt, player=None, movesteps=None):
    '''根据给定棋盘现状和后续下法，返回棋盘最终状态，谁赢或者平局'''
    ox = copy.deepcopy(ttt)
    playturn = player
    if movesteps is not None:
        for ms in movesteps:
            ox[ms] = 1 if playturn=='x' else -1
            '''计算ttt方阵连线情况,1代表'x'连成一线，-1代表'o'，0代表没有'''
            '''把各行列的和组成列表'''
            ox_line = list(ox.sum(axis=1)) + list(ox.sum(axis=0))
            '''第一条对角线的和加入列表'''
            ox_line += [sum([ox[i, i] for i in range(ox.shape[0]) ])]
            '''第二条对角线的和加入列表'''
            ox_line += [sum([ox[ox.shape[0]-1-i,i] for i in range(ox.shape[0]) ])]
            if ox.shape[0] == max(abs(x) for x in ox_line):
                return -1 if -ox.shape[0] in ox_line else 1 if ox.shape[0] in ox_line else 0
            playturn = 'x' if playturn=='o' else 'o'
        return 0
    
    
def ai_move(ttt, player='o'):
    '''AI走一步，但每走一步都穷尽所有走法，找到最好的,'''
    ox = ttt
    playturn = player
    move_value = {x:0 for x in ttt_availables}
    print(move_value)
    #'''一个产生下法序列的生成器函数，穷举直到不再有新的下法序列'''
    #'''使用了排列生成，生成函数是个函数生成器； 返回剩余下法的所有排列'''
    mvs = itertools.permutations(ttt_availables)
    for m in mvs:
        move_value[m[0]] += ttt_simu(ox, playturn, m)

    mvlist = [k for k,v in move_value.items() if v==move_value[min(move_value, key=move_value.get)]]
    print(move_value)
    print(mvlist)
    return mvlist[random.randint(0,len(mvlist)-1)] #返回元组(x,y)

          
def update(player, location, ttt):
    '''# player在location(x,y)处落子，更新棋盘，,更新可用位置，计算此时棋局胜负'''
    ttt[location] = 1 if player=='x' else -1
    ttt_availables.remove( location )


# In[8]:


''' # 3 x 3 矩阵，值是棋子类型，0空，1代表'x'，-1代表'o'; ''' 
ttt = np.zeros((3, 3), dtype=int )
ttt_availables = set( [(i,j) for i in range(3) for j in range(3)] )  
while True:
    print('请选择先手，o电脑先，x选手先：')
    player = input()
    if player == 'x' or player == 'o':
        break


# In[9]:



#print(ttt_availables)

while True :
    
    tttshow(ttt)
    
    if player == 'x':
        print('请选手选择落子处的数字，如23代表在第2行第3列落子：', end='')
        xy = input()
        playlocation = (int(xy[0])-1, int(xy[1])-1 )
        update(player, playlocation, ttt)
        if ttt_simu(ttt) == 1:
            print('选手 赢')
            tttshow(ttt)
            break
        if ttt_availables == set():
            print('平局')
            tttshow(ttt)
            break
        player = 'o'
        
    if player == 'o':
        playlocation = ai_move(ttt)
        print(playlocation)
        update(player, playlocation, ttt)
        if ttt_simu(ttt) == -1:
            print('计算机 赢')
            tttshow(ttt)
            break 
        if ttt_availables == set():
            print('平局')
            tttshow(ttt)
            break
        player = 'x'
        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




