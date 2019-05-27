#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

class Board(object):
    '''棋盘，默认是“井字棋”Tie Tac Toe，也可以作为五子棋的棋盘'''
    def __init__(self, height=3, width=3, ninline=3):
        self.width = width     #列
        self.height = height   #行 
        self.ninline = ninline    # 表示几个相同的棋子连成一线算作胜利
        
        #''' # M x N 矩阵，值是棋子类型，0空，1代表'x'，-1代表'o'; ''' 
        self.ox = np.zeros((self.height, self.width), dtype=int )
        
        #'''现棋盘空余可下位置集合如{(0,0), (0,1), }'''
        self._ox_availables = set( [(i,j) for i in range(self.height) for j in range(self.width)] )
        #'''最后一步的位置和玩家'''
        self._ox_lastmove = None
        
        #'''棋盘棋局胜负标志，1代表'x'赢，-1代表'o'赢，0代表平局，None代表未结束'''
        self._ox_states = None
                    

    def _nmatrixwinner(self,nm):
        '''计算方阵连线情况,1代表'x'连成一线，-1代表'o'连成一线，0代表没有
           把各行列的和组成集合，查找集合中是否存在3或-3，代表连成一行'''
        n_line = set(nm.sum(axis=1)) | set(nm.sum(axis=0))
        '''第一条对角线的和加入列表；使用方阵的迹'''
        #n_line.add(sum([nm[i, i] for i in range(self.ninline) ]))
        n_line.add(nm.trace())
        '''第二条对角线的和加入列表；使用方阵反转后的迹'''
        #n_line.add(sum([nm[self.ninline-1-i,i] for i in range(self.ninline) ]))
        n_line.add(nm[::-1].trace())
        
        #-1代表o赢，1代表x，0平局，None还没有结果
        return -1 if -nm.shape[0] in n_line else 1 if nm.shape[0] in n_line else 0 if nm.all() else None
    
        
    def _checkwinner(self):
        '''检查棋盘棋局胜负，1代表'x'赢，-1代表'o'赢，0代表平局，None代表未结束'''
        #'''生成棋盘所有ninline维方阵，并判断方阵是否有连成一线的情况'''
        matrixlist = [self.ox[i:i+self.ninline, j:j+self.ninline] 
                      for i in range(self.height- self.ninline +1)
                        for j in range(self.width- self.ninline +1)
                     ]
    
        #'''如果出现ninline维方阵返回1或者-1，代表已经有了输赢，返回输赢结果'''
        for nm in matrixlist:
            if self._nmatrixwinner(nm) != 0:
                return self._nmatrixwinner(nm) 
        
        #'''所有ninline维方阵返回都是0，检查是否有可落子处，无则返回0代表平局，有则None代表未结束'''
        return 0 if not self._ox_availables else None
          
    
    def board_now(self):
        #返回一个元组，第一个元素是输赢状态，第二个元素是剩余可落子位置的集合,第三个元素是最后一步情况
        return (self._ox_states, self._ox_availables, self._ox_lastmove)    
    
    
    
    def board_update(self, player, location): 
        '''# player在location(x,y)处落子，更新棋盘，,更新可用位置，计算此时棋局胜负'''
        if location in self._ox_availables:
            self.ox[location] = 1 if player=='x' else -1
            self._ox_availables.remove( location )
            self._ox_lastmove = (player, (location))
            self._ox_states = self._checkwinner()
            return 1    
        else:
            return 0     
                  
            
    def board_show(self):
        '''显示棋盘，参数是棋盘矩阵'''
        #'''打印列标号'''
        print("{0:>15}".format('x\y'), end='') # 5个字符
        for j in range(self.width):
            print("{0:^5}".format(j), end='') # 5个字符          
        print('\n')  # 换行,打印空行        
      
        #'''打印棋盘'''            
        for i in range(self.height):        #行数
            #'''打印行标号'''
            print("{0:>15}".format(i), end='') # 5个字符
            #'''打印该行棋盘'''    
            for j in range(self.width):
                if self.ox[i][j] == 0:    #未落子  5个字符
                    print("{0:^5}".format('+'), end='')
                elif self.ox[i][j] == 1:   # x 落子  5个字符
                    print("{0:^5}".format('X'), end='')
                elif self.ox[i][j] == -1:  # o 落子
                    print("{0:^5}".format('Q'), end='') 
            print('\n')     
            
 
