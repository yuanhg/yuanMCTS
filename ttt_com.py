# coding: utf-8

# Author Yuan Honggang
# Copyright 1.0

from mtcsboard import Board

def lockrevalue(player='x', location=(1,1) ):
    if xo.update(player, location) == 0:
        return 0
    xo_lock[(location[0]-1)*3 + location[1]] = 1 if player == 'x' else -1
        
    #分别评估剩余空格对x、o两方的价值，计入x_value，o_value
    #行列如果有两子情况出现，则另一个空位是对双方来说价值最高的
    #行列如果有一子情况出现，则另两个个空位是对双方来说价值次高的
    
    #落子处价值归零
    for i in range(1,10):
        if xo_lock[i] != 0:
            xo_value[i] = 0
            
    #判断3行中空位价值
    for i in range(1,8,3):
        if xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == 2 or xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == -2:
            for j in range(3):
                if xo_lock[i+j] == 0:
                    xo_value[i+j] = 99

        if xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == 1 or xo_lock[i] + xo_lock[i+1] + xo_lock[i+2] == -1:
            #如果存在两个空位，价值次高，否则价值不变
            if [xo_lock[i] , xo_lock[i+1] , xo_lock[i+2]].count(0) == 2:
                for j in range(3):
                    if xo_lock[i+j] == 0:
                        xo_value[i+j] = 33
                    
    #判断3列中空位价值，落子处价值归0
    for i in range(1,4):
        if xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == 2 or xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == -2:
            for j in range(0,7,3):
                if xo_lock[i+j] == 0:
                    xo_value[i+j] += 99

        if xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == 1 or xo_lock[i] + xo_lock[i+3] + xo_lock[i+6] == -1:
            #如果存在两个空位，价值次高，否则价值不变
            if [xo_lock[i] , xo_lock[i+3] , xo_lock[i+6]].count(0) == 2:
                for j in range(0,7,3):
                    if xo_lock[i+j] == 0:
                        xo_value[i+j] += 33
       
    #检查两条斜线
    if xo_lock[3] + xo_lock[5] + xo_lock[7] == 2 or xo_lock[3] + xo_lock[5] + xo_lock[7] == -2:
        for j in range(3,8,2):
            if xo_lock[j] == 0:
                xo_value[j] += 99

    if xo_lock[1] + xo_lock[5] + xo_lock[9] == 2 or xo_lock[1] + xo_lock[5] + xo_lock[9] == -2:
        for j in range(1,10,4):
            if xo_lock[j] == 0:
                xo_value[j] += 99
                    
    if xo_lock[3] + xo_lock[5] + xo_lock[7] == 1 or xo_lock[3] + xo_lock[5] + xo_lock[7] == -1:
        #如果存在两个空位，价值次高，否则价值不变
        if [xo_lock[3] , xo_lock[5] , xo_lock[7]].count(0) == 2:
            for j in range(3,8,2):
                if xo_lock[j] == 0:
                    xo_value[j] += 33

    if xo_lock[1] + xo_lock[5] + xo_lock[9] == 1 or xo_lock[1] + xo_lock[5] + xo_lock[9] == -1:
        #如果存在两个空位，价值次高，否则价值不变
        if [ xo_lock[1] , xo_lock[5] , xo_lock[9] ].count(0) == 2:
            for j in range(1,10,4):
                if xo_lock[j] == 0:
                    xo_value[j] += 33

    return 1


# return point(i) available [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
def availablepoint():
    ap = 0
    max = 0
    for i in range(1,10):
        if xo_value[i] > max:
            max = xo_value[i]
            ap = i
    return ap


xo = Board()
xo.oxshow()
#lock xo, and revalue x_value and o_value
# 0表示未落子，1表示x落子，-1表示o落子，初始没有落子
xo_lock  = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
xo_value = {1:3,2:2,3:3,4:2,5:4,6:2,7:3,8:2,9:3}

while True:
    print('请选择先手，o电脑先，x选手先：')
    player = input()
    if player == 'x' or player == 'o':
        break
    
while True :
    
    if xo.oxavailable() == {}:
        print('平局')
        break
    
    if player == 'x':
        print('请选手选择落子处的数字，如23代表在第2行第3列落子：', end='')
        xy = input()
        playlocation = (int(xy[0]), int(xy[1]) )
        if lockrevalue(player, playlocation) == 0:
            continue  #没有选择正确的落子位置，重新选        
        
        if xo.oxstates() == 1:
            print('选手 赢')
            break  
        player = 'o'
        
    if player == 'o':
        playnum = availablepoint()
        if playnum == 0:
            print('平局')
            break
                   
        print('计算机选择（%s, %s)落子' %((playnum-1)//3+1, (playnum-1)%3+1))
        lockrevalue(player, ((playnum-1)//3+1, (playnum-1)%3+1) )
        if xo.oxstates == -1:
            print('计算机 赢')
            break        
        player = 'x'

        xo.oxshow()

        
