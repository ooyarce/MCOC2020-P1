import scipy as sp 
from scipy.integrate import odeint
import matplotlib.pylab as plt
import numpy as np

#parametros
G = 6.67*10**-11 #Nm^2/kg^2
mt = 5.98*10**24 #kg 
r = (6371 + 700)*1000 #mts
omega = 2*np.pi/86400 #teta de tiempo
t = sp.linspace(0,12800,1001)
earth_radius = (6371)*1000
atmosphere_radius = (6371+80)*1000

#condiciones inciiales
x = r #mts
y = 0
z = 0 #

vx = 0 #m/s
vy = 7000 #m/s  valor óptimo entre 6900 y 7100 ms/s 
vz = 0 
                 #z1  #z2
z0 = sp.array([x,y,z,vx,vy,vz]) #vector de C.B

#matrices de rotacion
def poto(z,t):
    R = np.array([[np.cos(omega*t),-np.sin(omega*t),0],
             [np.sin(omega*t), np.cos(omega*t),0],
             [0,                0,             1]])
    
    equis = np.array([z[0],z[1],z[2]])
    A = R@equis
    B = np.dot(A,A)
    erre = np.sqrt(B)
    return erre
def satelite(z,t):
    R = sp.array([[sp.cos(omega*t),-sp.sin(omega*t),0],
             [sp.sin(omega*t), sp.cos(omega*t),0],
             [0,                0,             1]])
    
    dR_dt = sp.array([[-sp.sin(omega*t)*omega,-sp.cos(omega*t)*omega,0],
                  [sp.cos(omega*t)*omega, -sp.sin(omega*t)*omega,0],
                  [0,                0,             0]])
    
    dR2_dt2 = sp.array([[-sp.cos(omega*t)*omega**2,sp.sin(omega*t)*omega**2,0],
                   [-sp.sin(omega*t)*omega**2,-sp.cos(omega*t)*omega**2,0],
                   [0,                0,             0]])

    zp = sp.zeros(6)
    zp[0:3] = z[3:6]
    z1 = (-G*mt/r**3)*z[0:3]  - R.T@(dR2_dt2@z[0:3] + 2*dR_dt@z[3:6])
    zp[3:6] = z1
    return zp
s = poto(z0,t)
sol = odeint(satelite,z0,t)
x = sol[:,0]
y = sol[:,1]
z = sol[:,2]
plt.plot(t,np.sqrt(x**2+y**2+z**2))
plt.axhline(y=6371*1000,color = "blue")
plt.axhline(y=(6371+80)*1000,color = "red")
plt.xlim([0,13000])
plt.title("Historias de tiempo de r(t)")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Posición (metros)")
plt.legend(['r(t)','tierra','atmosfera']) 
plt.savefig('3ergrafico.png')




