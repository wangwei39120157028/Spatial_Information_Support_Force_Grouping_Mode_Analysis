#coding:utf-8
import matplotlib.pyplot as plt
import math
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np

N = 23               #总节点数

c=[0 ,math.pi/2 ,math.pi ,3*math.pi/2,  math.pi/4, 3*math.pi/4, 5*math.pi/4 , 7*math.pi/4  , math.pi/2 , math.pi, 3*math.pi/2 ,0  , 3*math.pi/4 ,5*math.pi/4 ,7*math.pi/4,  math.pi/4 , math.pi, 3*math.pi/2, 0 , math.pi/2 ,7*math.pi/4 ,math.pi/4, 3*math.pi/4 ]
w = [2 , 2.8  , 3,3.2 ,  2 ,  2.8 , 3 ,  3.2 ,2 , 2.8  , 3, 3.2 ,   2 , 2.8 ,3,  3.2 ,  2  ,2.8 , 3 , 3.2 , 2, 2  ,1.5 ]

'''
w = [0,2,3,3,4,4,2,3,3,4,4,2,3,3,4,4,2,3,3,4,4,2,2,3,4,1]                #自然频率向量,w[0] = 0占位
c = [0,0,math.pi / 2,math.pi,3 * math.pi / 2,0,
0,math.pi / 2,math.pi,3 * math.pi / 2,0,0,
math.pi / 2,math.pi,3 * math.pi / 2,0,0,math.pi / 2,
math.pi,3 * math.pi / 2,0,0,math.pi / 2,math.pi,3 * math.pi / 2,
0,0,math.pi / 2,math.pi,3 * math.pi / 2,0,0]                #初始相位,c[0] = 0占位
'''
k0 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0  ,0.5,  0.5 , 0.5 , 0  ,0 , 0 , 0 , 0 , 0,  0 , 0 , 0 , 0 , 0 , 0,  0,  0 , 0 , 0  ,0.2, 0 ,0,],
[0.5 , 0 , 0 , 0  ,0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 , 0 , 0  ,0 , 0  ,0 , 0 , 0 , 0 , 0  ,0  ,0,]  ,
[0.5 ,0 , 0 , 0, 0 , 0 , 0 , 0,  0 , 0 , 0 , 0 ,0 , 0,  0, 0 , 0 , 0 , 0  ,0 , 0 , 0 , 0 ]  ,
[0.5 ,0 , 0 , 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0,  0, 0 , 0 , 0 , 0 , 0  ,0 , 0 , 0 ]  ,
[  0 ,0 , 0 , 0, 0 , 0.5 , 0.5 , 0.5 , 0 , 0 ,0 , 0,  0, 0 , 0 , 0 , 0 , 0  ,0  ,0 , 0.2 ,0 ,0 ],
[  0 ,0 , 0 , 0, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0, 0, 0 , 0 , 0 , 0  ,0 , 0 , 0 , 0 ] ,
[  0 ,0 , 0 , 0, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0, 0, 0 , 0 , 0 , 0  ,0 , 0 , 0 , 0 ] ,
[  0 ,0 , 0 , 0, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0, 0, 0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0 , 0 , 0.5 , 0.5 , 0.5,  0,  0 , 0,  0 , 0 , 0 , 0,  0 , 0 ,0.2 ,0] ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0,  0 , 0 , 0 , 0 ] ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0  ,0 , 0 , 0 , 0 , 0 , 0 ],
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0  ,0  ,0 , 0 , 0 , 0 , 0 , 0 ],
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0 , 0.5 , 0.5 , 0.5 , 0 , 0,  0 , 0 , 0, 0.2, 0] ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0.5  ,0 , 0 , 0 , 0 ,0 ,0 ,0 ,0  ,0 , 0 ] ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0.5  ,0  ,0 , 0 , 0 ,0 ,0 ,0 ,0  ,0 , 0 ],
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0.5  ,0  ,0  ,0 , 0 ,0 ,0 ,0 ,0  ,0 , 0 ],
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0 , 0 ,0 , 0 , 0 , 1, 1, 1, 0, 0 , 0.5 ] ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0 , 0 ,0 , 0 , 1 , 0, 0, 0, 0, 0 , 0 ]  ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0 , 0 ,0 , 0 , 1 , 0, 0, 0, 0, 0 , 0 ]  ,
[  0 ,0 , 0 , 0, 0 , 0 , 0, 0, 0, 0, 0, 0,0 , 0 ,0 , 0 , 1 , 0, 0, 0, 0, 0 , 0 ] ,
[  0.2, 0 ,0,  0 , 0.2 ,0 ,0 , 0, 0, 0, 0,0 , 0 ,0 , 0 , 0,  0 , 0,  0 , 0,  0 , 0  ,0.5 ] ,
[  0 , 0 , 0,  0 , 0 , 0 , 0 , 0, 0.2 ,0, 0,0 , 0.2, 0,0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0.5 ] ,
[  0  ,0 , 0,  0,  0,  0,  0 , 0, 0, 0 ,0,0 , 0 , 0 , 0  ,0 , 0.5 , 0 , 0 , 0,  0.5, 0.5 , 0 ]
]

k1 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.5],      
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.5],      
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0.5],      
[1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0.5],      
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],        
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2],        
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0],          
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0],          
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0],
[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,2,0,0,0,1]]                #i和j的耦合矩阵，独立分组,1-25,0占位


k2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0.5],      
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0.5],      
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,2,0,0,0.5],      
[1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,2,0,0.5],     
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],       
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],        
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],         
[0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],         
[0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,0,0],          
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2],
[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,2,0,0,0,1]]                #i和j的耦合矩阵，完全分散分组                    


k3 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0.5],      
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0.5],      
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,2,0,0,0.5],      
[1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],        
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,2,0,0.5],      
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],        
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],        
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0],        
[0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0],          
[0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1,1,1,0],          
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1,0,1,1,2],
[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,2,0,0,0,1]]                 #i和j的耦合矩阵，不完全分散分组


#r = (float(1) / N )* x                #目标函数
n = [i + 1 for i in range(22)]                #目标划分,24个值,1-24
t = [j  for j in range(1000)]
ci = 0


C = []
C.append(c)

for d in range(1100):
    for i in n :
        for j in range(22):
            cj = c[j + 1] - c[i]
            ci += k3[i][j + 1] * math.sin(cj) 
    
        cii = ci + w[i]
        h = [0.01 * cii + z for z in c]
        C.append(h)
        c = h

def r_function(u):
    y1 = 0
    y2 = 0
    y12 = 0
    y22 = 0
    r = []
    for x in range(1000):
        for ul in u:
            y1 += math.cos(C[x][ul])
            y2 += math.sin(C[x][ul])
        y12 = y1 ** 2
        y22 = y2 ** 2
        r.append((float(1) / N ) * ((y12 + y22) ** 0.5))
    return r
    
    
'''
r1 = r_function([1,2,3,4,5])
r2 = r_function([6,7,8,9,10])
r3 = r_function([11,12,13,14,15,])
r4 = r_function([16,17,18,19,20])
r5 = r_function([21,22,23,24,25])
'''


r1 = r_function([1,2,3,4,5])
r2 = r_function([6,7,8,9])
r3 = r_function([10,11,12,13])
r4 = r_function([14,15,16,17])
r5 = r_function([18,19,20])


ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置 
ymajorLocator  = MultipleLocator(0.1) #将y轴主刻度标签设置为0.5的倍数 
ax.yaxis.set_major_locator(ymajorLocator) 
plt.plot(t, r1, marker='o', color='green', label='1')
plt.plot(t, r2, marker='D',color='red', label='2')
plt.plot(t, r3, marker='+',color='skyblue', label='3')
plt.plot(t, r4, marker='h', color='blue', label='4')
plt.plot(t, r5, marker='_',color='yellow', label='5')

#plt.plot(t, r6, color='red', label='6')


plt.legend() # 显示图例
plt.xlabel('iteration times')
plt.ylabel('rate')
plt.show()





