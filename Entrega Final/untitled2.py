μ = 1.
J2 = 1.
R = 1.

def Fg(x,y,z):
    Fx = x*μ*(J2*R**2*(3*z**2/(2*(r)) - 0.5)/(r) + 1)/(r)**(3/2) - μ*(-3*J2*R**2*x*z**2/(r)**3 - 2*J2*R**2*x*(3*z**2/(2*(r)) - 0.5)/(r)**2)/sqrt(r)
    Fy = y*μ*(J2*R**2*(3*z**2/(2*(r)) - 0.5)/(r) + 1)/(r)**(3/2) - μ*(-3*J2*R**2*y*z**2/(r)**3 - 2*J2*R**2*y*(3*z**2/(2*(r)) - 0.5)/(r)**2)/sqrt(r)
    Fz = z*μ*(J2*R**2*(3*z**2/(2*(r)) - 0.5)/(r) + 1)/(r)**(3/2) - μ*(-2*J2*R**2*z*(3*z**2/(2*(r)) - 0.5)/(r)**2 + J2*R**2*(-3*z**3/(r)**2 + 3*z/(r))/(r))/sqrt(r)
    return Fx,Fy,Fz
