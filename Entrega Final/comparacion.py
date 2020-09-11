from leerof import leer_eof
from sys import argv
from numpy import sqrt

#eof_1 = argv[1]
#eof_2 = argv[2]
eof_1 = 'S1B_OPER_AUX_POEORB_OPOD_20200816T110726_V20200726T225942_20200728T005942.EOF'
eof_2 = 'S1B_OPER_AUX_POEORB_OPOD_20200816T110726_V20200726T225942_20200728T005942.PRED'

t1, x1, y1, z1, vx1, vy1, vz1 = leer_eof(eof_1)
t2, x2, y2, z2, vx2, vy2, vz2 = leer_eof(eof_2)

delta = (sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2))/7000

print(delta[-1]/1000, "kilometros")