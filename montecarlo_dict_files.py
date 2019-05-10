import json
import numpy as np
import itertools


board = 6   #默认围棋19大小的棋盘

a_point = set( [(i,j) for i in range(board) for j in range(board)] )

mv_dict = {}
for i in range(6, len(a_point)+1):
    mvs = itertools.combinations(a_point, i)
    #mv_dict = {}
    for mv in mvs:
        m_dict = {}
        for m in mv:
            m_dict[m] = (0.0 , 0)
        mv_dict[mv] = m_dict

print(mv_dict)
#mv_dict_file = json.dumps(mv_dict)

#with open('montecarlo_dic_files.json', 'w') as f:
#    f.write(mv_dict_file)

