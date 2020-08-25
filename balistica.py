import scipy as sp 
from scipy.integrate import odeint
import matplotlib.pylab as plt
#Unidades base
cm = 0.01
rho = 1.225 #kg /m3
inch = 2.54*cm
g=9.81
m= 15.
#vientos
vientos = [0.,10.,20.] #magnitudes en m/s
#coeficiente de arrastre
cd = 0.47
D = 8.5*inch
r = D/2
A = sp.pi*r**2
CD = 0.5*rho*cd*A
#funcion a integrar
# z es vector estado
# z  = [x,,y,vx,vy]
#dz/dt = bala (z,t)

def bala(z,t):
    zp = sp.zeros(4)
    zp[0] = z[2]
    zp[1] = z[3]
    v = z[2:4]
    v[0]= v[0] - V
    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)
    FD = -CD*v2*(v/vnorm)
    zp[2] = FD[0]/m
    zp[3] = FD[1]/m - g
    return zp
#vector tiempo

t = sp.linspace(0,30,1001)
#parte en x,y, teniendo una velocidad vx, vy 
vi= 100*1000/3600
z0 = sp.array([0,0,vi,vi])
plt.figure(1)
for i in vientos:
    V = i
    sol = odeint(bala,z0,t)
    x = sol[:,0]
    y = sol[:,1]
    plt.plot(x,y)
plt.grid()
plt.ylim(0,50)
plt.xlim(0,150)
plt.title("Trayectoria para distintos vientos")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.legend(["V = 0 m/s", "V = 10 m/s", "V = 20 m/s"]) 
plt.savefig('foo.png')
plt.show()