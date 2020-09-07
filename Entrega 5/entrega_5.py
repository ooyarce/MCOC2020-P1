from scipy.integrate import odeint
import  matplotlib.pylab as plt
import numpy as sp
from eof import leer_eof

#parametros
G = 6.67*10**-11 #Nm^2/kg^2
mt = 5.98*10**24 #kg 
omega = 2*sp.pi/86400 #teta de tiempo
earth_radius = (6371)*1000
atmosphere_radius = (6371+80)*1000

#matrices de rotacion
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

#puntos reales
t, x, y, z, vx, vy, vz = leer_eof('S1B_OPER_AUX_POEORB_OPOD_20200816T110726_V20200726T225942_20200728T005942.EOF') 
z0 = sp.array([x[0],y[0],z[0],vx[0],vy[0],vz[0]]) #condicion de borde inicial

#puntos de predicción
sol = odeint(zpunto,z0,t)
x_sol = sol[:,0]
y_sol = sol[:,1]
z_sol = sol[:,2]

#formato gráfico
y1=[-5e6,0,5e6]
ejey=["-5000","0","5000"]
x1=[0,18000,36000,54000,72000,90000]
ejex=["0","5","10","15","20","25"]

#ploteamiento1
plt.figure()
plt.subplot(3,1,1)
plt.plot(t,x)
plt.plot(t,x_sol)
plt.title("Posición")
plt.ylabel("X (Km)")
plt.yticks(y1,ejey)
plt.xticks(x1,ejex)

#ploteamiento2
plt.subplot(3,1,2)
plt.plot(t,y)
plt.plot(t,y_sol)
plt.ylabel("Y (Km)")
plt.yticks(y1,ejey)
plt.xticks(x1,ejex)

#ploteamiento3
plt.subplot(3,1,3)
plt.plot(t,z)
plt.plot(t,z_sol)
plt.ylabel("Z (Km)")
plt.yticks(y1,ejey)
plt.xticks(x1,ejex)
plt.xlabel('Tiempo, t (horas)')

#ajuste de gráfico
plt.tight_layout()

#guardo el gráfico en formato png
plt.savefig('ploteo1.png')