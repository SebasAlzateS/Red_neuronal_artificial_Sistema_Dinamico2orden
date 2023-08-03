import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.close()
u=0
k=1.6222
Wn=1.5
E=0.5
delta=0.7
t=0
z=[]
y=0
x=0
tt=[]
uu=[]

while t<=210:
      
      if t>=30:
         u=40
      if t>=60:
         u=80   
      if t>=90:
         u=100
      if t>=120:
         u=100
      if t>=150:
         u=75 
      if t>=180:
         u=25
      if t>=210:
         u=0
         

      #print(y)
      uu.append(u)
      z.append(y)
      tt.append(t)
      t=t+1
      A=(1/(1/delta**2)+((E*Wn)/delta))
      B=(Wn**2)*k
      C=(Wn**2)-(2/delta**2)
      D=(1/delta**2)-((E*Wn)/(delta))
      y=(1/A)*(B*uu[t-1]-C*z[t-1]-D*z[t-2])
      
      print(y)

           
zmax=max(z)
zmin=min(z)
umax=max(uu)
umin=min(uu)

normu=[]
normz=[]
for i in range(len(z)):
    nz=(z[i]-zmin)/(zmax-zmin)
    normz.append(nz)
    nu=(uu[i]-umin)/(umax-umin)
    normu.append(nu)
    
plt.plot(tt,normz, color="red")
plt.show()
planta=[uu,z]
planta=np.transpose(planta)

uk_1=normu[1:len(normu)-1]
uk_2=normu[0:len(normu)-2]
yk_1=normz[1:len(normz)-1]
yk_2=normz[0:len(normz)-2]
yk=normz[2:]

matriz=np.zeros((len(z)-2,5))
matriz[:, 0]=uk_1
matriz[:, 1]=uk_2
matriz[:, 2]=yk_1
matriz[:, 3]=yk_2
matriz[:, 4]=yk

np.savez("matriz", matriz=matriz,tt=tt)
UY_min_max = list(np.array([umin, umax, zmin, zmax]))
np.savetxt('UY_min_max.txt', UY_min_max)

