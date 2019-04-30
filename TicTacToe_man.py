# Author Yuan Honggang
# Copyright 1.0

from board import Board

xo = Board(3,3,3)
player = 'x'

while True :
    xo.oxshow()
        
    print('请选手(%s)选择落子处的数字：'%(player), end='')
    xy = input()
    playlocation = (int(xy[0])-1, int(xy[1])-1 )
    
    if xo.update(player, playlocation ):
        if xo.oxstates() == 1:
            print('    选手X 赢')
            xo.oxshow()
            break
        elif xo.oxstates() == -1:
            print('    选手O 赢')
            xo.oxshow()
            break
        elif xo.oxstates() == 0:
            print('    平局')
            xo.oxshow()
            break
        elif xo.oxstates() == 2:
            player = 'o' if player == 'x' else 'x'
            
    


    
