from random import choice
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(16,16))
def tran_1(p):
    x=p[0]
    y=p[1]
    x1=0.5*x
    y1=0.5*y
    return x1,y1
def tran_2(p):
    x=p[0]
    y=p[1]
    x1=0.5*x+0.5
    y1=0.5*y+0.5
    return x1,y1
def tran_3(p):
    x=p[0]
    y=p[1]
    x1=0.5*x+1
    y1=0.5*y
    return x1,y1
transformations=[tran_1,tran_2,tran_3]
a1=[0]
b1=[0]
a,b=0,0
num_of_trans=10000000
for i in range(num_of_trans):
    transformations_choice = choice(transformations)
    a,b=transformations_choice(list((a,b)))
    a1.append(a)
    b1.append(b)
plt.plot(a1,b1,'o')
plt.show()