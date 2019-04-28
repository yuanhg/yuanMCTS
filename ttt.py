# -*- coding: utf-8 -*-


#生成一个列表，用列表值画Tic Tac Toe图案
#行列用‘*’，用"X”和"O"表示下棋的两方

ttt = {}
for i in range(91):
    if i in [14,15,16,18,19,20,22,23,24,
             40,41,42,44,45,46,48,49,50,
             66,67,68,70,71,72,74,75,76]:
        ttt[i] = ' '
    else:
        ttt[i] = '*'

#一个字典，表示1-9个下棋空位在列表ttt中的序号
dt = {1:15, 2:19, 3:23, 4:41, 5:45, 6: 49, 7:67, 8:71, 9:75}
for i in range(1, 10):
    ttt[dt[i]] = i

    
def showttt():
    for i in range(len(ttt)):
        if (i+1)%13 != 0:
            print(ttt[i],  end='')
        else:
            print(ttt[i])

#显示初始井字图案，并用1-9表示可以落子的选择
showttt()

#检查是否有选手获胜，即连成3连线
def win():
    if str(ttt[dt[1]]) + str(ttt[dt[2]]) + str(ttt[dt[3]]) == 'XXX' or str(ttt[dt[1]]) + str(ttt[dt[2]]) + str(ttt[dt[3]]) == 'OOO':
        return 1
    if str(ttt[dt[4]]) + str(ttt[dt[5]]) + str(ttt[dt[6]]) == 'XXX' or str(ttt[dt[4]]) + str(ttt[dt[5]]) + str(ttt[dt[6]]) == 'OOO':
        return 1
    if str(ttt[dt[7]]) + str(ttt[dt[8]]) + str(ttt[dt[9]]) == 'XXX' or str(ttt[dt[7]]) + str(ttt[dt[8]]) + str(ttt[dt[9]]) == 'OOO':
        return 1
    if str(ttt[dt[1]]) + str(ttt[dt[4]]) + str(ttt[dt[7]]) == 'XXX' or str(ttt[dt[1]]) + str(ttt[dt[4]]) + str(ttt[dt[7]]) == 'OOO':
        return 1
    if str(ttt[dt[2]]) + str(ttt[dt[5]]) + str(ttt[dt[8]]) == 'XXX' or str(ttt[dt[2]]) + str(ttt[dt[5]]) + str(ttt[dt[8]]) == 'OOO':
        return 1
    if str(ttt[dt[3]]) + str(ttt[dt[6]]) + str(ttt[dt[9]]) == 'XXX' or str(ttt[dt[3]]) + str(ttt[dt[6]]) + str(ttt[dt[9]]) == 'OOO':
        return 1
    if str(ttt[dt[1]]) + str(ttt[dt[5]]) + str(ttt[dt[9]]) == 'XXX' or str(ttt[dt[1]]) + str(ttt[dt[5]]) + str(ttt[dt[9]]) == 'OOO':
        return 1
    if str(ttt[dt[3]]) + str(ttt[dt[5]]) + str(ttt[dt[7]]) == 'XXX' or str(ttt[dt[3]]) + str(ttt[dt[5]]) + str(ttt[dt[7]]) == 'OOO':
        return 1
    return 0

#下面轮流选择1-9，每选择一次，检查是否可选，若可以，则更改井字图案，更改棋手
play = 0
xo = ['X', 'O']
while True:
    #检查可选剩余可选数字
    nums = []
    for i in range(1,10):
        if ttt[dt[i]] == i :
           nums.append(i)
    if nums == []:
        print("Nobody Win")
        break

    print('请(%s)选择落子处的数字：' %(xo[play]), end='')
    playnum = int(input())
    if playnum not in nums:
          continue
    
    if play == 0 :
        ttt[dt[playnum]] = 'X'
        showttt()
        if win():
            print(xo[play], 'Player Win')
            break
        play = 1
    else:
        ttt[dt[playnum]] = 'O'
        showttt()
        if win():
            print(xo[play], 'Player Win')
            break
        play = 0

   


    

   

    
