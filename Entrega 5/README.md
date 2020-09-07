**- (2pt) Grafíque, como arriba, la posición (x,y,z) en el tiempo del vector de estado de Sentinel 1A/B que le tocó. Para esto, descargue y utilice la función leer_eof.py (Enlaces a un sitio externo.) para poder trabajar con los archivos EOF.**

![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo1.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo2.png?raw=true)


**- (5pt) Usando la condición inicial (primer OSV) de su archivo, compare la solución entre odeint y eulerint. Use Nsubdiviciones=1. Grafíque la deriva en el tiempo como arriba ¿Cuánto deriva eulerint de odeint en este caso al final del tiempo? (Esta pregunta solo compara algoritmos, no se usa más que la condición inicial del archivo EOF). ¿Cuanto se demora odeint y eulerint respectivamente en producir los resultados?**

![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo3.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteobasediagonal.png?raw=true)

La deriva entre eulerint y odeint está dada por 17942.38 kilómetros. Es decir, Eulerint con 1 iteración de Nsubdivisiones es muchísimo menos eficiente que odeint. Respectivamente, odeint y eulerint demoran 0.18 segundos y 0.49 segundos, mostrando nuevamente que odeint es mejor.

**-(3pt) ¿Cuantas subdivisiones hay que usar para que la predicción con eulerint al final del tiempo esté en menos de un 1% de error? Grafique la deriva en el tiempo. Comente con respecto del tiempo de ejecución de eulerint ahora. 
