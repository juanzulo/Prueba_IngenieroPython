# Prueba_IngenieroPython
 Prueba ingeniero python Ultracom

Para los retos se debe realizar lo siguiente:
1. Ejecutar el script Ajedrez.py el cual imprime los movimientos permitidos de las fichas de ajedrez en una posicion aleatoria,
	para el caso del peon se tiene que avanza de abajo hacia arriba.
	
2. Importar el archivo Algebra.py para usar las clases expresion_algebraica y operacion_algebraica.
	*Expresion_algebraica: esta clase debe resibir una cadena que represente la ecuacion algebraica en sumas y restas, los exponentes de la variable con ^
							por ejemplo "3x^2+2x+4", por defecto la varibale es x si se desea otra se debe colocar "la variable:", ej. "y:3y^2+2y+4".
							Tiene el metodo evaluar_expresion que reemplaza la variable por el parametro entero recibido y retorna un entero con el resultado.
							
	*operacion_algebraica: crearda para realizar opeaciones entre expresiones aljeraicas, posee los siguientes metodos:
		*suma = metodo que recibe 2 parametros que deben ser tipo Expresion_algebraica con el fin de retornar el reultado en texto con la suma 
				de las 2 expresiones algebraicas
		*simplificar = version reducida de la funcion suma que recibe solo una expresion aljebraica, simplifica la expresion, se usa en el metodo de multiplicacion.
		*resta = metodo que recibe 2 parametros que deben ser tipo Expresion_algebraica con el fin de retornar el reultado en texto con la resta 
				de las 2 expresiones algebraicas
		*multiplicacion = metodo que recibe 2 parametros que deben ser tipo Expresion_algebraica con el fin de retornar el reultado en texto con la multiplicacion 
				de las 2 expresiones algebraicas
		*multiplicacion_escalar = metodo que recibe 2 parametros, 1 tipo Expresion_algebraica  otro tipo entero, con el fin de retornar el reultado en texto con 
				la multiplicacion del entero a toda la expresion algebraica.