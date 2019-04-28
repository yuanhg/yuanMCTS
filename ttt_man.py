# Author Yuan Honggang
# Copyright 1.0

from mtcsboard import Board

xo = Board()
player = 'x'

while True :
    xo.oxshow()
    if xo.oxavailable() == {}:
        print('平局')
        break
        
    print('请选手(%s)选择落子处的数字：'%(player), end='')
    xy = input()
    playlocation = (int(xy[0]), int(xy[1]) )
    if xo.update(player, playlocation ) == 0:
        continue
    if xo.oxstates() == 1:
        print('选手X 赢')
        break
    elif xo.oxstates() == -1:
        print('选手Q 赢')
        break
    player = 'o' if player == 'x' else 'x'


    
