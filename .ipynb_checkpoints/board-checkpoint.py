{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "class Board(object):\n",
    "    '''棋盘，默认是“井字棋”Tie Tac Toe，也可以作为五子棋的棋盘'''\n",
    "    def __init__(self, height=3, width=3, ninline=3):\n",
    "        self.width = width     #列\n",
    "        self.height = height   #行 \n",
    "        self.ninline = ninline    # 表示几个相同的棋子连成一线算作胜利\n",
    "        \n",
    "        #''' # M x N 矩阵，值是棋子类型，0空，1代表'x'，-1代表'o'; ''' \n",
    "        self.ox = np.zeros((self.height, self.width), dtype=int )\n",
    "        \n",
    "        #'''现棋盘空余可下位置集合如{(0,0), (0,1), }'''\n",
    "        self._ox_availables = set( [(i,j) for i in range(self.height) for j in range(self.width)] )\n",
    "        \n",
    "        #'''棋盘棋局胜负标志，1代表'x'赢，-1代表'o'赢，0代表平局，2代表未结束'''\n",
    "        self._ox_states = 2\n",
    "                    \n",
    "\n",
    "    def _nmatrixwinner(self,nm):\n",
    "        '''计算方阵连线情况,1代表'x'连成一线，-1代表'o'连成一线，0代表没有\n",
    "           把各行列的和组成集合，查找集合中是否存在3或-3，代表连成一行'''\n",
    "        n_line = set(nm.sum(axis=1)) | set(nm.sum(axis=0))\n",
    "        '''第一条对角线的和加入列表；使用方阵的迹'''\n",
    "        #n_line.add(sum([nm[i, i] for i in range(self.ninline) ]))\n",
    "        n_line.add(nm.trace())\n",
    "        '''第二条对角线的和加入列表；使用方阵反转后的迹'''\n",
    "        #n_line.add(sum([nm[self.ninline-1-i,i] for i in range(self.ninline) ]))\n",
    "        n_line.add(nm[::-1].trace())\n",
    "        \n",
    "        #-1代表o赢，1代表x，0平局，None还没有结果\n",
    "        return -1 if -nm.shape[0] in n_line else 1 if nm.shape[0] in n_line else 0 if nm.all() else None\n",
    "    \n",
    "        \n",
    "    def _checkwinner(self):\n",
    "        '''检查棋盘棋局胜负，1代表'x'赢，-1代表'o'赢，0代表平局，None代表未结束'''\n",
    "        #'''生成棋盘所有ninline维方阵，并判断方阵是否有连成一线的情况'''\n",
    "        matrixlist = [self.ox[i:i+self.ninline, j:j+self.ninline] \n",
    "                      for i in range(self.height- self.ninline +1)\n",
    "                        for j in range(self.width- self.ninline +1)\n",
    "                     ]\n",
    "    \n",
    "        #'''如果出现ninline维方阵返回1或者-1，代表已经有了输赢，返回输赢结果'''\n",
    "        for nm in matrixlist:\n",
    "            if self._nmatrixwinner(nm) != 0:\n",
    "                return self._nmatrixwinner(nm) \n",
    "        \n",
    "        #'''所有ninline维方阵返回都是0，检查是否有可落子处，无则返回0代表平局，有则None代表未结束'''\n",
    "        return 0 if not self._ox_availables else None\n",
    "          \n",
    "    \n",
    "    def board_now(self):\n",
    "        return (self._ox_states, self._ox_availables)    #返回一个元组，第一个元素是输赢状态，第二个元素是剩余可落子位置的集合\n",
    "    \n",
    "    \n",
    "    def board_update(self, player, location): \n",
    "        '''# player在location(x,y)处落子，更新棋盘，,更新可用位置，计算此时棋局胜负'''\n",
    "        if location in self._ox_availables:\n",
    "            self.ox[location] = 1 if player=='x' else -1\n",
    "            self._ox_availables.remove( location )    \n",
    "            self._ox_states = self._checkwinner()\n",
    "            return 1    \n",
    "        else:\n",
    "            return 0     \n",
    "                  \n",
    "            \n",
    "    def board_show(self):\n",
    "        '''显示棋盘，参数是棋盘矩阵'''\n",
    "        #'''打印列标号'''\n",
    "        print(\"{0:>15}\".format('x\\y'), end='') # 5个字符\n",
    "        for j in range(self.width):\n",
    "            print(\"{0:^5}\".format(j), end='') # 5个字符          \n",
    "        print('\\n')  # 换行,打印空行        \n",
    "      \n",
    "        #'''打印棋盘'''            \n",
    "        for i in range(self.height):        #行数\n",
    "            #'''打印行标号'''\n",
    "            print(\"{0:>15}\".format(i), end='') # 5个字符\n",
    "            #'''打印该行棋盘'''    \n",
    "            for j in range(self.width):\n",
    "                if self.ox[i][j] == 0:    #未落子  5个字符\n",
    "                    print(\"{0:^5}\".format('+'), end='')\n",
    "                elif self.ox[i][j] == 1:   # x 落子  5个字符\n",
    "                    print(\"{0:^5}\".format('X'), end='')\n",
    "                elif self.ox[i][j] == -1:  # o 落子\n",
    "                    print(\"{0:^5}\".format('Q'), end='') \n",
    "            print('\\n')     \n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                      x\\y  0    1    2  \n",
      "\n",
      "                        0  +    +    +  \n",
      "\n",
      "                        1  +    +    +  \n",
      "\n",
      "                        2  +    +    +  \n",
      "\n",
      "2\n",
      "{(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=Board(3,3,3)\n",
    "a.board_show()\n",
    "s, (v) = a.board_now()\n",
    "print(s)\n",
    "print(v)\n",
    "type(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "{(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (2, 2), (1, 0), (0, 2)}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.board_update('x',(1,1))\n",
    "print(s)\n",
    "print(v)\n",
    "type(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                      x\\y  0    1    2  \n",
      "\n",
      "                        0  +    +    +  \n",
      "\n",
      "                        1  +    X    +  \n",
      "\n",
      "                        2  +    Q    +  \n",
      "\n",
      "2\n",
      "{(0, 1), (1, 2), (0, 0), (2, 0), (2, 2), (1, 0), (0, 2)}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.board_update('o',(2,1))\n",
    "a.board_show()\n",
    "s, (v) = a.board_now()\n",
    "print(s)\n",
    "print(v)\n",
    "type(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}