#coding:utf-8
import matplotlib.pyplot as plt
import math
import numpy as np

N = 23                #总节点数

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
t = [j / 10 for j in range(300)]
a = [0 for j in range(300)]
b = [0 for j in range(300)]
ci = 0
r = [0 for j in range(300)]

for i in n :
    for j in range(22):
        cj = c[j + 1] - c[i]
        ci += k0[i][j + 1] * math.sin(cj) 
    
    cii = ci + w[i]
    #h = [z * cii for z in t]
    #cii = (float(1) / N ) * ci + w[i]
    h = [0.01 * cii + z for z in c]
    
    a1 = [math.cos(hi) for hi in h]
    b1 = [math.sin(hi) for hi in h]
    a = [a[f]+a1[f] for f in range(0,len(a1))] 
    b = [b[f]+b1[f] for f in range(0,len(b1))] 
    
    #c = [0 for j in range(300)]
    c = h
    aj = [ai ** 2  for ai in a]
    bj = [bi ** 2  for bi in b]
    #print aj
    #print bj
    r = [r[f] + (float(1) / N ) * (aj[f]+bj[f]) ** 0.5 for f in range(0,len(aj))] 
    #r = [(float(1) / N ) * (abi ** (1/2)) for abi in ab]
    #print r
    #t = t[1:300]
    #r = r[1:300]
    ci = 0
    plt.title('Result Analysis')
    if i == 4:
        r1 = r
        print r1[40]
        a = [0 for j in range(300)]
        b = [0 for j in range(300)]
        a1 = 0
        b1 = 0
        ci = 0
        h = []
        r = [0 for j in range(300)]
    if i == 10:
        r2 = r
        a = [0 for j in range(300)]
        b = [0 for j in range(300)]
        a1 = 0
        b1 = 0
        ci = 0
        h = []
        r = [0 for j in range(300)]
    if i == 15:
        r3 = r
        a = [0 for j in range(300)]
        b = [0 for j in range(300)]
        a1 = 0
        b1 = 0
        ci = 0
        h = []
        r = [0 for j in range(300)]
    if i == 20:
        r4 = r
        a = [0 for j in range(300)]
        b = [0 for j in range(300)]
        a1 = 0
        b1 = 0
        ci = 0
        h = []
        r = [0 for j in range(300)]
    if i == 24:
        r5 = r
        a = [0 for j in range(300)]
        b = [0 for j in range(300)]
        a1 = 0
        b1 = 0
        ci = 0
        h = []
        r = [0 for j in range(300)]
    if i == 25:
        r6 = r
        a = [0 for j in range(300)]
        b = [0 for j in range(300)]
        a1 = 0
        b1 = 0
        ci = 0
        h = []
        r = [0 for j in range(300)]
        
        
plt.plot(t, r1, color='green', label='1')
'''
plt.plot(t, r2, color='red', label='2')
plt.plot(t, r3, color='skyblue', label='3')
plt.plot(t, r4, color='blue', label='4')
#plt.plot(t, r5, color='yellow', label='5')
#plt.plot(t, r6, color='red', label='6')
'''
plt.legend() # 显示图例
plt.xlabel('iteration times')
plt.ylabel('rate')
plt.show()


####r1 = 0.0486,tm = 2 ,b = 0.9
####r2 = 0.028, tm = 4 ,b = 0.9
####r3 = 0.036, tm = 3 ,b = 0.9



