import matplotlib.pyplot as plt
import random as rd
import numpy as np
#plt.style.use('seaborn')
plt.style.use('dark_background')
f= lambda x:np.exp(x)
def algo_monte_carlo(a,b,precision_n,f):
    pas = (abs(a) + abs(b)) / precision_n
    Y = [f(a+i*pas) for i in range(precision_n + 1)]
    return min(Y),max(Y)
def show_monte_carlo(a,b,precision_n,n_point,f):
    pas=(abs(a)+abs(b))/precision_n
    X=np.array([a+i*pas for i in range(precision_n+1)])
    L_pont=algo_monte_carlo(a,b,precision_n,f)
    X_point_inside=[]
    Y_point_inside=[]
    X_point_outside=[]
    Y_point_outside=[]
    res=0
    for i in range(n_point):
        xp=rd.uniform(a, b)
        yp=rd.uniform(L_pont[0], L_pont[1])

        if(yp<=f(xp)):
            X_point_inside.append(xp)
            Y_point_inside.append(yp)
            res += 1
        else:
            X_point_outside.append(xp)
            Y_point_outside.append(yp)
    res=(res/n_point)*(b-a)*L_pont[1]
    plt.plot(X_point_inside,Y_point_inside,'ko',markersize=2,color='blue',label='point_interieure')
    plt.plot(X_point_outside,Y_point_outside,'ko',markersize=2,color='red',label='point_exterieure')
    plt.title("l'integrele de f dans ["+str(a)+","+str(b)+"] "+str(res))
    plt.plot(X, f(X), color='white',label="fonction")
    plt.legend()
    plt.show()
#print(algo_monte_carlo(-np.pi,np.pi,1000,f))
show_monte_carlo(-8,1,1000,10000,f)