#802-3av-cluster.py
#simulation of IEEE 802.3av network in Python

from mpl_toolkits import mplot3d
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

def graphic(Y,X,U):
        # Drawing 3D graphic
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot_wireframe(Y,X,U, color='black')
        ax.set_xlabel('N')
        ax.set_ylabel('$\omega _{max}[\mu s]$')
        ax.set_zlabel('U')
        plt.xticks(np.arange(0, 63, step=20))
        plt.yticks(np.arange(0, 0.00051, step=0.0001),
                   ('0','100','200','300','400','500'))
        plt.show()

def run_802_3av(N,Tw_max,T,k):
        P=[]    
        for ii in range(len(N)):
                P.append([])
                print(ii)
                tmax=10e-6
                t = uniform(0, tmax, [int(N[ii]), k])
                for jj in range(len(Tw_max)):
                        Tw = uniform(0, Tw_max[jj], [int(N[ii]), k])
                        Q = zeros([int(N[ii]), k])
                        for i in range(int(N[ii])):
                                D = zeros([int(N[ii]), k])
                                for j in range(int(N[ii])):
                                        D[j, :] = (abs((t[j, :]+Tw[j, :]) -
                                                       (Tw[i, :]+t[i, :])) > T)
                                Q[i, :] = (sum(D, axis=0) == (int(N[ii])-1))
                        Pi = sum(Q, axis=0)/N[ii]
                        P[ii].append(sum(Pi)/k)
        return P,tmax

Nmin = 2 # minimalni broj ONU
Nmax = 64 # maksimalni broj ONU
nN = int(Nmax/2-1) # broj odbiraka opsega [Nmin, Nmax]

Tw_max1 = 1e-6 # minimalna vrednost maksimalnog slučajnog kašnjenja
Tw_max2 = 500e-6 # maksimalna vrednost maksimalnog slučajnog kašnjenja
nTw_max = 50 # broj odbiraka opsega [Tw_max1, Tw_max2]

N= np.linspace(Nmin,Nmax,nN)
Tw_max = np.linspace(Tw_max1,Tw_max2, nTw_max)
        
T = 2.2912e-6 # trajanje prozora pronalaženja
k = 100 # broj replikacija

X,Y=np.meshgrid(Tw_max,N) # potrebno za crtanje 3D wireframe

# probability of success for cluster ONU
P,tmax = run_802_3av(N,Tw_max,T,k)
U = np.array(Y,dtype=float)*np.array(P,dtype=float)*T/(tmax+T+np.array(X,dtype=float))

graphic(Y,X,U)
