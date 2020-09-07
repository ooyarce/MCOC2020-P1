**- (2pt) Grafíque, como arriba, la posición (x,y,z) en el tiempo del vector de estado de Sentinel 1A/B que le tocó. Para esto, descargue y utilice la función leer_eof.py (Enlaces a un sitio externo.) para poder trabajar con los archivos EOF.**

![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo1.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo2.png?raw=true)


**- (5pt) Usando la condición inicial (primer OSV) de su archivo, compare la solución entre odeint y eulerint. Use Nsubdiviciones=1. Grafíque la deriva en el tiempo como arriba ¿Cuánto deriva eulerint de odeint en este caso al final del tiempo? (Esta pregunta solo compara algoritmos, no se usa más que la condición inicial del archivo EOF). ¿Cuanto se demora odeint y eulerint respectivamente en producir los resultados?**

![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteobasediagonal.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/plote_optimizado2.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo3.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo4.png?raw=true)

El gráfico de la izquierda muestra la gráfica de la deriva del eulerint (azul) versus la gráfica del odeint (naranjo). El gráfico de la derecha muestra la deriva de la odeint. La deriva entre eulerint y odeint está dada por 17942.38 kilómetros. Es decir, Eulerint con 1 iteración de Nsubdivisiones es muchísimo menos eficiente que odeint. Respectivamente, odeint y eulerint demoran 0.18 segundos y 0.49 segundos, mostrando nuevamente que odeint es mejor.

**-(3pt) ¿Cuantas subdivisiones hay que usar para que la predicción con eulerint al final del tiempo esté en menos de un 1% de error? Grafique la deriva en el tiempo. Comente con respecto del tiempo de ejecución de eulerint ahora.**

Para encontrar eso, probé con diferentes valores, 10,100,150,200,250,270,300,500, y 1000. El más eficiente se encontraba en el N = 1000, con un pequeño margen de error al inicio pero con un margen del 2% de error al final. Por ende podemos decir con certeza de que el numero N de subdivisiones suficiente para encontrar un error menor al 1% fluctúa entre 1500 y 2000 Esto se traduce en que no hay forma de acomodar en una forma 100% la órbita satélital usando odeint natural, pero sí con el eulerint, con un grandísimo número de Nsubintervalos. El tiempo de ejecucción fue excesivamente grande y fue de: 1343.83 segundos (22 minutos aproximadamente).

![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/eulerint_1000_it.png?raw=true)
![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/eulerint_1000_it.png?raw=true)

**-(5pt) Implemente las correcciones J2 y J3. Repita los gráficos de arriba para su caso particular. ¿Cuánta deriva incurre al agregar las correcciones J2 y J3? ¿Cuanto se demora su código en correr?**
Respecto al primer gráfico, obtenemos un resultado muchisimo más preciso, tanto, que de hecho las lineas se ven superpuestas a simple vista mientras que en el primer gráfico se podía apreciar notablemente la linea azul (odeint sin J2 ni J3). Por otro lado, respecto a los tiempos de resolución, estos son idénticos y la carga de memoria no es tan grave por lo que se podría decir que es un método muy eficiente. Las derivas implementando el J2 y el J3 mejoran notablemente la precisión, no obstante, la diferencia entre J2 y J2+J3 no fue tan grande ni significativa por lo que el J2 basta para encontrar una aproximación con odeint que baje notablemente el margen de error.

![alt_text](https://github.com/ooyarce/MCOC2020-P1/blob/master/Entrega%205/ploteo2.png?raw=true)


