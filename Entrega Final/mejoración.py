from sympy import *
from legendre import legendre
from coeficiente import coeficientes
x = S('x')
y = S('y')
z = S('z')
μ = S('μ')
J2 = S('J2') 
J3 = S('J3')
J4 = S('J4') 
J5 = S('J5')
J6 = S('J6') 
J7 = S('J7')
J8 = S('J8') 
R = S('R')

r = sqrt(x**2 + y**2+ z**2)
sinθ = z/r
Φ = atan2(y,x)
u = -μ/r *(1 + 
            (J2*legendre(0,2,sinθ)/(r/R)**2 +
            J3*legendre(0,3,sinθ)/(r/R)**3  +
            J4*legendre(0,4,sinθ)/(r/R)**4  +
            J5*legendre(0,5,sinθ)/(r/R)**5)  +
                     #m,n               m,n         m                 m,n          m            n
            (legendre(1,2,sinθ)*(coeficientes(1,2)[0]*cos(1*Φ)+coeficientes(1,2)[1]*sin(1*Φ)) /(r/R)**2 + # n = 2, m = 1
            legendre(2,2,sinθ)*(coeficientes(2,2)[0]*cos(2*Φ)+coeficientes(2,2)[1]*sin(2*Φ)) /(r/R)**2 + # n = 2, m = 2 
          
            legendre(1,3,sinθ)*(coeficientes(1,3)[0]*cos(1*Φ)+coeficientes(1,3)[1]*sin(1*Φ)) /(r/R)**3 +# n = 3, m = 1
            legendre(2,3,sinθ)*(coeficientes(2,3)[0]*cos(2*Φ)+coeficientes(2,3)[1]*sin(2*Φ)) /(r/R)**3 +# n = 3, m = 2  
            legendre(3,3,sinθ)*(coeficientes(3,3)[0]*cos(3*Φ)+coeficientes(3,3)[1]*sin(3*Φ)) /(r/R)**3 +# n = 3, m = 3 

            legendre(1,4,sinθ)*(coeficientes(1,4)[0]*cos(1*Φ)+coeficientes(1,4)[1]*sin(1*Φ)) /(r/R)**4 +# n = 4, m = 1
            legendre(2,4,sinθ)*(coeficientes(2,4)[0]*cos(2*Φ)+coeficientes(2,4)[1]*sin(2*Φ)) /(r/R)**4 +# n = 4, m = 2  
            legendre(3,4,sinθ)*(coeficientes(3,4)[0]*cos(3*Φ)+coeficientes(3,4)[1]*sin(3*Φ)) /(r/R)**4 +# n = 4, m = 3
            legendre(4,4,sinθ)*(coeficientes(4,4)[0]*cos(4*Φ)+coeficientes(4,4)[1]*sin(4*Φ)) /(r/R)**4 +# n = 4, m = 4

            legendre(1,5,sinθ)*(coeficientes(1,5)[0]*cos(1*Φ)+coeficientes(1,5)[1]*sin(1*Φ)) /(r/R)**5 +# n = 5, m = 1
            legendre(2,5,sinθ)*(coeficientes(2,5)[0]*cos(2*Φ)+coeficientes(2,5)[1]*sin(2*Φ)) /(r/R)**5 +# n = 5, m = 2  
            legendre(3,5,sinθ)*(coeficientes(3,5)[0]*cos(3*Φ)+coeficientes(3,5)[1]*sin(3*Φ)) /(r/R)**5 +# n = 5, m = 3
            legendre(4,5,sinθ)*(coeficientes(4,5)[0]*cos(4*Φ)+coeficientes(4,5)[1]*sin(4*Φ)) /(r/R)**5 +# n = 5, m = 4
            legendre(5,5,sinθ)*(coeficientes(5,5)[0]*cos(5*Φ)+coeficientes(5,5)[1]*sin(5*Φ)) /(r/R)**5 # n = 5, m = 5 
            ))

Fx = u.diff(x)
Fy = u.diff(y)
Fz = u.diff(z)

print (Fx)
print (Fy)
print (Fz)
