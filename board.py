import numpy as np

class Board(object):
    '''棋盘，默认是“井字棋”TieTacToe，也可以作为五子棋'''
    def __init__(self, height=3, width=3, ninline=3):
        self.width = width     #列
        self.height = height   #行 
        ''' # 表示几个相同的棋子连成一线算作胜利'''
        self.ninline = ninline
        
        ''' # M x N 矩阵，值是棋子类型，0空，1代表'x'，-1代表'o'; ''' 
        self.ox = np.zeros((self.height, self.width), dtype=int )
        '''棋盘棋局胜负标志，1代表'x'赢，-1代表'o'赢，0代表平局'''
        self.ox_states = 0
        '''可下位置列表元素如[1:(0,0), 2:(0,1), ]'''
        self.ox_available = dict(zip( [(k+1) for k in range(self.width*self.height)], 
                                  [(i+1,j+1) for i in range(self.height) for j in range(self.width)] ))
        
    '''显示棋盘，参数是棋盘矩阵'''        
    def oxshow(self):
        '''打印列标号'''
        print('    ', end='') # 5个空格
        for j in range(self.width):
            if j <10:
                print('  %d '%(j+1), end='')
            elif j <100:
                print('  %d'%(j+1), end='')
        print('')  # 换行
        '''打印分割线'''
        print('    ', end='')# 5个空格
        for j in range(self.width):
            print('    ', end='')
        print('')
        
        '''打印棋盘'''            
        for i in range(self.height):        #行数
            '''打印行标号'''
            if i <10:
                print('  %d  '%(i+1), end='' )
            elif i*self.width+j <100:
                print('  %d '%(i+1), end='' )
            '''打印该行棋盘'''    
            for j in range(self.width):
                if self.ox[i][j] == 0:    #未落子
                    print(' ~  ', end='')
                elif self.ox[i][j] == 1:   # x 落子
                    print(' X  ', end='')
                elif self.ox[i][j] == -1:  # o 落子
                    print(' Q  ', end='') 
            print('')
            '''打印分割线'''
            print('    ', end='')# 5个空格
            for j in range(self.width):
                print('    ', end='')
            print('')                    
                
 
    '''计算一个ninlin方阵连线情况,1代表'x'连成一线，-1代表'o'，0代表没有'''
    def nmatrixwinner(self,nm):
        '''把各行列的和组成列表'''
        ox_line = list(nm.sum(axis=1)) + list(nm.sum(axis=0))
        '''第一条对角线的和加入列表'''
        ox_line += [sum([nm[i, i] for i in range(nm.shape[0]) ])]
        '''第二条对角线的和加入列表'''
        ox_line += [sum([nm[nm.shape[0]-1-i,i] for i in range(nm.shape[0]) ])]            
        
        return -1 if -nm.shape[0] in ox_line else 1 if nm.shape[0] in ox_line else 0
    
    
    '''检查棋盘棋局胜负，1代表'x'赢，-1代表'o'赢，0代表平局'''
    def oxwinner(self):
        '''生成棋盘所有ninline维方阵，并判断方阵是否有连成一线的情况'''
        matrixlist = [self.ox[i:i+self.ninline, j:j+self.ninline] 
                      for i in range(self.ox.shape[0]- self.ninline +1)
                     for j in range(self.ox.shape[1]- self.ninline +1)
                     ]
    
        '''如果出现ninline维方阵返回1或者-1，代表已经有了输赢，返回输赢结果'''
        for nm in matrixlist:
            if self.nmatrixwinner(nm) != 0:
                return self.nmatrixwinner(nm) 
        
        '''若所有ninline维方阵返回都是0，则返回0平局'''
        return 0       
      
    
    '''# player在location(x,y)处落子，更新棋盘，,更新可用位置，计算此时棋局胜负'''
    def update(self, player, location): 
        if location in self.ox_available.values():
            self.ox[location[0]-1, location[1]-1] = 1 if player=='x' else -1
            self.ox_available.pop( (location[0]-1)*self.width + location[1] )    
            self.ox_states = self.oxwinner()
            return 1
        else:
            return 0
        
            
    '''返回棋盘输赢状态'''
    def oxstates(self):        
        return self.ox_states
    
    
    '''为AI返回一个可以选择落子的字典集合'''
    def oxavailable(self):
        return self.ox_available
    

