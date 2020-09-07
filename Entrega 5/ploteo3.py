from scipy.integrate import odeint
import  matplotlib.pylab as plt
import numpy as sp
from eof import leer_eof
from time import perf_counter
#parametros
G = 6.67*10**-11 #Nm^2/kg^2
mt = 5.98*10**24 #kg 
omega = 2.*sp.pi/86400 #teta de tiempo
#funcion zpunto
def zpunto(z,t):
    #parámetros
    zp = sp.zeros(6)
    sin = sp.sin(omega*t)
    cos = sp.cos(omega*t)
    z1 = z[0:3]
    r2 = sp.dot(z1,z1)
    r = sp.sqrt(r2)
    #defino mis matrices de rotación
    R = sp.array([
        [cos,-sin,0],
        [sin,cos,0],
        [0,0,1]])
    
    dR_dt = sp.array([
        [-sin*omega,-cos*omega,0],
        [cos*omega, -sin*omega,0],
        [0,0,0]])   
    dR2_dt2 = sp.array([
        [-cos*omega**2,sin*omega**2,0],
        [-sin*omega**2,-cos*omega**2,0],
        [0,0,0]]) 
    
    #defino mi vector zp 
    zp[0:3] = z[3:6] 
    zp[3:6]= (-G*mt/r**3)*z[0:3]  - R.T@(dR2_dt2@z[0:3] + 2*dR_dt@z[3:6])
    return zp

#solución euler
def eulerint(zp,z0,t,Nsubdivisiones = 1):
    Nt = len(t)
    Ndim = len(sp.array(z0))
    z = sp.zeros((Nt,Ndim))
    z[0,:] = z0[:]
    for i in range(1,Nt):
        t_anterior = t[i-1]
        dt = (t[i] - t[i-1])/Nsubdivisiones
        z_temp = z[i-1,:].copy()
        for k in range(Nsubdivisiones):
            z_temp += dt * zpunto(z_temp,t_anterior + k*dt)
        z[i,:] = z_temp
    return z

#puntos reales
t, x, y, z, vx, vy, vz = leer_eof('S1B_OPER_AUX_POEORB_OPOD_20200816T110726_V20200726T225942_20200728T005942.EOF') 
z0 = sp.array([x[0],y[0],z[0],vx[0],vy[0],vz[0]]) #condicion de borde inicial

#puntos de predicción
t1 = perf_counter()
sol = odeint(zpunto,z0,t)
t2 = perf_counter()
print(t2-t1)
x_sol = sol[:,0]
y_sol = sol[:,1]
z_sol = sol[:,2]

zp = sol[:,:] 
t1 = perf_counter()
sol2 = eulerint(zp,z0,t,Nsubdivisiones = 1)
t2 = perf_counter()
print(t2-t1)
x_euler = sol2[:,0]
y_euler = sol2[:,1]
z_euler = sol2[:,2]
#formato gráfico
delta = sp.sqrt((x-x_sol)**2+(y-y_sol)**2+(z-z_sol)**2)
delta2 = sp.sqrt((x-x_euler)**2+(y-y_euler)**2+(z-z_euler)**2)
max1 = delta2.max()/1000
print(max1)
plt.plot(t/3600,delta2/1000)
plt.plot(t/3600,delta/1000)
plt.ylabel('Deriva, δ (KM)')
plt.xlabel('Tiempo, t (horas)')
plt.title('Distancia entre posición real y predicha, $δ_{max}$ = 20882.82 (km)')
plt.savefig('ploteo3.png')
plt.show()