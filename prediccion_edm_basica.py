from scipy.integrate import odeint
from  matplotlib.pylab import *
import numpy as sp

#parametros
G = 6.67*10**-11 #Nm^2/kg^2
mt = 5.98*10**24 #kg 
r = (6371 + 700)*1000 #mts
omega = 2*sp.pi/86400 #teta de tiempo
earth_radius = (6371)*1000
atmosphere_radius = (6371+80)*1000

#matrices de rotacion
def zpunto(z,t):
    R = sp.array([[sp.cos(omega*t),-sp.sin(omega*t),0],
             [sp.sin(omega*t), sp.cos(omega*t),0],
             [0,                0,             1]])
    
    dR_dt = sp.array([[-sp.sin(omega*t)*omega,-sp.cos(omega*t)*omega,0],
                  [sp.cos(omega*t)*omega, -sp.sin(omega*t)*omega,0],
                  [0,                0,             0]])
    
    dR2_dt2 = sp.array([[-sp.cos(omega*t)*omega**2,sp.sin(omega*t)*omega**2,0],
                   [-sp.sin(omega*t)*omega**2,-sp.cos(omega*t)*omega**2,0],
                   [0,                0,             0]])
    z1 = z[0:3]

    zp = sp.zeros(6)
    zp[0:3] = z[3:6]
    z1 = (-G*mt/r**3)*z[0:3]  - R.T@(dR2_dt2@z[0:3] + 2*dR_dt@z[3:6])
    zp[3:6] = z1
    return zp

from datetime import datetime
ti = "2020-07-26T22:59:42.000000"
ti = ti.split("T")
ti = "{} {}".format(ti[0],ti[1])
ti = datetime.strptime(ti, '%Y-%m-%d %H:%M:%S.%f')

tf = "2020-07-28T00:59:42.000000"
tf = tf.split("T")
tf = "{} {}".format(tf[0],tf[1])
tf = datetime.strptime(tf, '%Y-%m-%d %H:%M:%S.%f')

deltaT = (tf-ti).total_seconds()

#<TAI>TAI=2020-07-26T23:00:19.000000</TAI>
#<UTC>UTC=2020-07-26T22:59:42.000000</UTC>
#<UT1>UT1=2020-07-26T22:59:41.787522</UT1>
#<Absolute_Orbit>+22648</Absolute_Orbit>
#<X unit="m">1371481.573761</X>
#<Y unit="m">-1304066.019697</Y>
#<Z unit="m">-6824657.090969</Z>
#<VX unit="m/s">1581.121107</VX>
#<VY unit="m/s">-7202.607570</VY>
#<VZ unit="m/s">1694.526810</VZ>
x_i = 1371481.573761
y_i = -1304066.019697
z_i = -6824657.090969
vx_i = 1581.121107
vy_i = -7202.607570 
vz_i = 1694.526810

#<TAI>TAI=2020-07-28T01:00:19.000000</TAI>
#<UTC>UTC=2020-07-28T00:59:42.000000</UTC>
#<UT1>UT1=2020-07-28T00:59:41.788197</UT1>
#<Absolute_Orbit>+22664</Absolute_Orbit>
#<X unit="m">2053456.226545</X>
#<Y unit="m">5744691.526128</Y>
#<Z unit="m">-3593901.482495</Z>
#<VX unit="m/s">322.597794</VX>
#<VY unit="m/s">-4098.186538</VY>
#<VZ unit="m/s">-6376.048388</VZ>
x_f = 2053456.226545
y_f = 5744691.526128
z_f = -3593901.482495
vx_f = 322.597794
vy_f = -4098.186538
vz_f = -6376.048388

t = sp.linspace(0,deltaT,9361)
z0 = sp.array([x_i,y_i,z_i,vx_i,vy_i,vz_i])
sol = odeint(zpunto,z0,t)
x = sol[:,0:3]
pos_final = sp.array([x_f,y_f,z_f,vx_f,vy_f,vz_f]) - sol[-1]

for el in pos_final:
    print (el)























