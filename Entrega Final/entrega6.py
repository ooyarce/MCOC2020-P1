from numpy import zeros,array,dot,sqrt,pi
from scipy.integrate import odeint
from leerof import leer_eof
from numpy import sin as seno
from numpy import cos as cose

# Leer de línea de comando
from sys import argv
eofname=argv[1]

#eofname='S1B_OPER_AUX_POEORB_OPOD_20200816T110726_V20200726T225942_20200728T005942.EOF'
sat_t,sat_x,sat_y,sat_z,sat_vx,sat_vy,sat_vz=leer_eof(eofname)

eof_out=eofname.replace('.EOF','.PRED')
print(f'Archivo de entrada: {eofname}')
print(f'Archivo de salida: {eof_out}')

#Condición Inicial
z0=array([sat_x[0],sat_y[0],sat_z[0],sat_vx[0],sat_vy[0],sat_vz[0]])

#Condición Final
zf=array([sat_x[-1],sat_y[-1],sat_z[-1],sat_vx[-1],sat_vy[-1],sat_vz[-1]])

#parametros
G = 6.67*10**-11 #Nm^2/kg^2
mt = 5.98*10**24 #kg 
omega = 2*pi/86400 #teta de tiempo


def zpunto(z,t):
    #parámetros
    zp = zeros(6)
    sin = seno(omega*t)
    cos = cose(omega*t)
    z1 = z[0:3]
    r2 = dot(z1,z1)
    r = sqrt(r2)
    J2 = 1.75553*(10**10)*1000**5
    J3 = -2.61913*(10**11)*1000**6
    u = z[0]#x
    v = z[1]#y
    w = z[2]#z
    
    #defino mis valores de F
    Fx_J2 = J2*(u/r**7)*(6*w**2-3/2*(u**2+v**2))
    Fy_J2 = J2*(v/r**7)*(6*w**2-3/2*(u**2+v**2))
    Fz_J2 = J2*(w/r**7)*(3*w**2-9/2*(u**2+v**2))
    FJ2 = array([Fx_J2,Fy_J2,Fz_J2])
    
    Fx_J3 = J3*u*w/r**9*(10*w**2-15/2*(u**2+v**2))
    Fy_J3 = J3*v*w/r**9*(10*w**2-15/2*(u**2+v**2))
    Fz_J3 = J3/r**9*(4*w**2*(w**2-3*(u**2+v**2))+3/2*(u**2+v**2)**2)
    FJ3 = array([Fx_J3,Fy_J3,Fz_J3])
    
    #defino mis matrices de rotación
    R = array([
        [cos,-sin,0],
        [sin,cos,0],
        [0,0,1]])
    
    dR_dt = array([
        [-sin*omega,-cos*omega,0],
        [cos*omega, -sin*omega,0],
        [0,0,0]])   
    dR2_dt2 = array([
        [-cos*omega**2,sin*omega**2,0],
        [-sin*omega**2,-cos*omega**2,0],
        [0,0,0]]) 
    
    #defino mi vector zp 
    zp[0:3] = z[3:6] 
    zp[3:6]= (-G*mt/r**3)*z[0:3]  - R.T@(dR2_dt2@z[0:3] + 2*dR_dt@z[3:6]) + FJ2[0:3] + FJ3[0:3]
    return zp
sol=odeint(zpunto,z0,sat_t) 
sol_ode=sol[:,:]
t=sat_t
x=sol_ode[:,0]
y=sol_ode[:,1]
z=sol_ode[:,2]
vx=sol_ode[:,3]
vy=sol_ode[:,4]
vz=sol_ode[:,5]


with open(eof_out,'w') as fout:
    fout.write('<?xml version="1.0" ?>\n'
'<Earth_Explorer_File>\n'
'  <Earth_Explorer_Header>\n'
'    <Fixed_Header>\n'
'      <File_Name>S1B_OPER_AUX_POEORB_OPOD_20200817T110752_V20200727T225942_20200729T005942</File_Name>\n'
'      <File_Description>Precise Orbit Ephemerides (POE) Orbit File</File_Description>\n'
'      <Notes></Notes>\n'
'      <Mission>Sentinel-1B</Mission>\n'
'      <File_Class>OPER</File_Class>\n'
'      <File_Type>AUX_POEORB</File_Type>\n'
'      <Validity_Period>\n'
'        <Validity_Start>UTC=2020-07-27T22:59:42</Validity_Start>\n'
'        <Validity_Stop>UTC=2020-07-29T00:59:42</Validity_Stop>\n'
'      </Validity_Period>\n'
'      <File_Version>0001</File_Version>\n'
'      <Source>\n'
'        <System>OPOD</System>\n'
'        <Creator>OPOD</Creator>\n'
'        <Creator_Version>0.0</Creator_Version>\n'
'        <Creation_Date>UTC=2020-08-17T11:07:52</Creation_Date>\n'
'      </Source>\n'
'    </Fixed_Header>\n'
'    <Variable_Header>\n'
'      <Ref_Frame>EARTH_FIXED</Ref_Frame>\n'
'      <Time_Reference>UTC</Time_Reference>\n'
'    </Variable_Header>\n'
'  </Earth_Explorer_Header>\n'
'<Data_Block type="xml">\n'
'  <List_of_OSVs count="9361">\n')
    Nt=len(t) 
    for i in range(Nt):
        fout.write('    <OSV>\n'
f'      <TAI>TAI=2020-07-27T23:00:19.000000</TAI>\n'
f'      <UTC>UTC=2020-07-27T22:59:42.000000</UTC>\n'
f'      <UT1>UT1=2020-07-27T22:59:41.788119</UT1>\n'
f'      <Absolute_Orbit>+22663</Absolute_Orbit>\n'
f'      <X unit="m">{x[i]}</X>\n'
f'      <Y unit="m">{y[i]}</Y>\n'
f'      <Z unit="m">{z[i]}</Z>\n'
f'      <VX unit="m/s">{vx[i]}</VX>\n'
f'      <VY unit="m/s">{vy[i]}</VY>\n'
f'      <VZ unit="m/s">{vz[i]}</VZ>\n'
'      <Quality>NOMINAL</Quality>\n'
'    </OSV>\n')
    fout.write('  </List_of_OSVs>\n'
'</Data_Block>\n'
'</Earth_Explorer_File>\n')
