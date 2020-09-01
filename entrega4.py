from scipy.integrate import odeint
import matplotlib.pylab as plt
import numpy as np

#parametros
m = 1.0 #kg
f= 1.0 #Hz
chi = 0.2
w = 2*np.pi*f
k = m*w**2
c = 2*chi*w*m
t = np.linspace(0, 4., 100)

#condición inicial
x0 = 1
v0 = 1
z0 = [x0,v0]

#solución analítica
function = np.exp(-c*t/2)*np.cos(w*t)
plt.plot(t,function,color = 'black',linewidth=2,label = 'analytical solution')

#solución 
def zpunto(z,t):
    zp = np.zeros(2)
    zp[0] = z[1]
    z1 = z[0]
    z2 = z[1]
    zp[1] = -(c*z2+k*z1)/m
    return zp
sol = odeint(zpunto,z0,t)
xpp = sol[:,0]
plt.plot(t,xpp,color = 'blue',label = 'odeint function')

#solución euler
def eulerint(zp,z0,t,Nsubdivisiones = 1):
    Nt = len(t)
    Ndim = len(np.array(z0))
    z = np.zeros((Nt,Ndim))
    z[0,:] = z0[0]
    for i in range(1,Nt):
        t_anterior = t[i-1]
        dt = (t[i] - t[i-1])/Nsubdivisiones
        z_temp = z[i-1,:].copy()
        for k in range(Nsubdivisiones):
            z_temp += dt * zpunto(z_temp,t_anterior + k*dt)
        z[i,:] = z_temp
    return z

#Nsub = 1
zp = sol[:,:]
sol = eulerint(zp,z0,t,Nsubdivisiones = 1)
euler = sol[:,0]
plt.plot(t,euler,':',color = 'green',label = "Ndiv = 1")

#Nsub = 10
sol = eulerint(zp,z0,t,Nsubdivisiones = 10)
euler = sol[:,0]
plt.plot(t,euler,':',color = 'red',label = "Ndiv = 10")

#Nsub = 100
sol = eulerint(zp,z0,t,Nsubdivisiones = 100)
euler = sol[:,0]
plt.plot(t,euler,':',color = 'orange',label = "Ndiv = 100")

#formato de ploteo
plt.legend()
plt.title(" Aproximaciones oscilador armónico")
plt.xlabel('Tiempo (t) ')
plt.ylabel('X(t)')
plt.show()