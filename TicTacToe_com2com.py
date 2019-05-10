# coding: utf-8

import numpy as np
import copy
import itertools
import random


def tttshow(ox):
    '''显示棋盘，参数是棋盘矩阵'''
    #'''打印列标号'''
    print("{0:^25}".format('x\y'), end='') # 5个字符
    for j in range(ox.shape[1]):
        print("{0:^5}".format(j), end='') # 5个字符          
    print('\n')  # 换行,打印空行        
      
    #'''打印棋盘'''            
    for i in range(ox.shape[0]):        #行数
        #'''打印行标号'''
        print("{0:^25}".format(i), end='') # 5个字符
        #'''打印该行棋盘'''    
        for j in range(ox.shape[1]):
            if ox[i][j] == 0:    #未落子  5个字符
                print("{0:^5}".format('~'), end='')
            elif ox[i][j] == 1:   # x 落子  5个字符
                print("{0:^5}".format('X'), end='')
            elif ox[i][j] == -1:  # o 落子
                print("{0:^5}".format('Q'), end='') 
        print('\n')  
                

def ttt_winner(ox):
    '''计算方阵连线情况,1代表'x'连成一线，-1代表'o'连成一线，0代表没有'''
    '''把各行列的和组成集合，查找集合中是否存在3或-3，代表连成一行'''
    ox_line = set(ox.sum(axis=1)) | set(ox.sum(axis=0))
    '''第一条对角线的和加入列表'''
    ox_line.add(sum([ox[i, i] for i in range(ox.shape[0]) ]))
    '''第二条对角线的和加入列表'''
    ox_line.add(sum([ox[ox.shape[0]-1-i,i] for i in range(ox.shape[0]) ]))
    
    return -1 if -ox.shape[0] in ox_line else 1 if ox.shape[0] in ox_line else 0
    
    
def ttt_simu(ttt, playturn='o', ms=[]):
    '''根据给定棋盘现状和后续下法，返回棋盘最终状态，谁赢或者平局'''
    ox = copy.deepcopy(ttt)
    for i in range(len(ms)):
        ox[ms[i]] = 1 if playturn=='x' else -1     # 更新棋盘   
        if ttt_winner(ox) == 1:
            return ttt_winner(ox) + (len(ms)-i-1)
        elif ttt_winner(ox) == -1:
            return ttt_winner(ox) - (len(ms)-i-1)       
        elif ttt_winner(ox) == 0 :
            playturn = 'o' if playturn=='x' else 'x'
    return 0
    
    
def ai_getmove(ox, playturn='o', ox_availables=set()):
    '''AI走一步，但每走一步都穷尽所有走法，找到最好的,'''
    '''生成剩余下法的胜利初始化表'''
    move_value = {x:0 for x in ox_availables}
    #'''一个产生下法序列的生成器函数，穷举直到不再有新的下法序列'''
    #'''使用了排列生成，生成函数是个函数生成器； 返回剩余下法的所有排列'''
    mvs = itertools.permutations(ox_availables) 
    for m in mvs:
        move_value[m[0]] += ttt_simu(ox, playturn, m)
        
    if playturn == 'o':
        minvalue = move_value[min(move_value, key=move_value.get)]
        mvlist = [k for k,v in move_value.items() if v==minvalue ]
    if playturn == 'x':
        maxvalue = move_value[max(move_value, key=move_value.get)]
        mvlist = [k for k,v in move_value.items() if v==maxvalue ]

    return mvlist[random.randint(0,len(mvlist)-1)] #返回元组(x,y)

          
def update(ox, player, location):
    '''# player在location(x,y)处落子，更新棋盘，,更新可用位置，计算此时棋局胜负'''
    ox[location] = 1 if player=='x' else -1
    global ttt_availables 
    ttt_availables.remove( location )


''' # 3 x 3 矩阵，值是棋子类型，0空，1代表'x'，-1代表'o'; ''' 
ttt = np.zeros((3, 3), dtype=int )
ttt_availables = set( [(i,j) for i in range(3) for j in range(3)] )  

player = 'x'

while True :

    tttshow(ttt)

    if player == 'x':
        playlocation = ai_getmove(ttt, player, ttt_availables)
        update(ttt, player, playlocation)
        if ttt_winner(ttt) == 1:
            print('选手 赢')
            tttshow(ttt)
            break
        if ttt_availables == set():
            print('平局')
            tttshow(ttt)
            break
        player = 'o'

    if player == 'o':
        playlocation = ai_getmove(ttt, player, ttt_availables)
        update(ttt, player, playlocation)
        if ttt_winner(ttt) == -1:
            print('计算机 赢')
            tttshow(ttt)
            break 
        if ttt_availables == set():
            print('平局')
            tttshow(ttt)
            break
        player = 'x'



