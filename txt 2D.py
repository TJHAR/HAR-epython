import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

x=np.arange(300,552,2)
y=np.arange(240,456,4)#建立Ex,Em数组 
Z=np.array([])
fp=open("./data.txt","r")
data=fp.readlines()
for i in data:
    xyz=i.split("\t")
    z=float(xyz[2].replace(",",""))
    Z=np.append(Z,z)#建立intensive数组
zmax=np.max(Z)
zmin=np.min(Z)

X,Y=np.meshgrid(x, y)#建立网格
Z=np.array(Z).reshape((54, 126))#一维升二维

zmid=zmin+330000
ex=np.arange(zmid,zmax,1000)
lim=np.arange(zmin,zmid,1000)#排除散射峰***
plt.contourf(X, Y, Z,lim,cmap="jet")#绘图
plt.colorbar()
#plt.contourf(X,Y,Z,ex,colors='r')

ax.set_xlabel('Em Wavelength (nm)')
ax.set_ylabel('Ex Wavelength (nm)')

plt.show()
