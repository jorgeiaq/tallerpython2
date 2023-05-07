exercises = int(input("introduce un numero de ejercicio: "))

if exercises == 1:
	#positivo o negativo de tres numeros
	number = float(input("Ingrese un número: "))
	if number > 0:
    	print("El número es positivo")
	elif number < 0:
   	 print("El número es negativo")
if exercises == 2:
	# programa menor y mayor 
	print("bienvenido al programa")
	number1 = input("ingrese el primer numero: ")
	other = input("ingrese otro numero")

	if number1 > other:
  	  elderly = number1
	if other > number1:
  	  elderly = other
	if number1 < other:
  	  minor = number1
	if other < number1:
  	  minor = other

	print("el numero mayor es:", elderly)
	print("el numero menor es:", minor)
if exercises == 3:
	# mayor y menor de tres numero
	print("ingrese tres numero")
	number1 = input("digite el primer numero: ")
	number2 = input("digite un segundo numero: ")
	number3 = input("digite un ultimo numero: ")

	if number1 > number2 and number1 > number3:
  		eldery = number1
	elif number2 > number3 and number2 > number1:
  		eldery = number2
	else: 
  		eldery = number3

	if number1 < number2 and number1 < number3:
 		 minor = number1
	elif number2 < number1 and number2 < number3:
  		minor = number2
	else:
  		minor = number3

	print("el numero mayor es:", eldery)
	print("el nuymero menor es:", minor)
if exercises == 4:
	# calculo de sueldo de empleados 
	print("bienvenido")
	name = input("ingrese su nombre: ")
	hours = float(input("ingrese las horas trabajadas: "))

	value_hours = 4
	extra_value = value_hours * 2

	salary = hours * value_hours
	extra_value = 0
	if hours <= 48:
  		salary = hours * value_hours
  		print("el empleado:", name, "tiene un sueldo de:", salary)
	else:
  		hours >= 48
  		extra_value = hours * value_hours
  		print("el empleado con nombre:", name, "tiene un sueldo con sus extras de:", extra_value)

if exercises == 5:
	#suma de dos numeros
	print("BIENVENIDO ingresa lo que se te solicita")
	# variables de suma y resta
	a = float(input("ingresa un numero: "))
	b = float(input("ingresa un numero para la letra b: "))

	if a < b:
  		subtraction = a - b
  		print("el resultado es:", subtraction)
	elif a > b:
  		addition = a + b
  		print("el resultado de la suma es:", addition)

if exercises == 6:
	#cociente de dos numeros
	print("bienvenido")

	A = int(input("ingresa un numero: "))
	B = int(input("ingresa otro numero: "))



	if A > 0 and B > 0:
  		quotient = A // B
 		 print("la operacion da como resultado: ", quotient)
	else:
  		print("la division es imposible")
if exercises == 7:
	#dia de la semana
	print("ingresa un numero para ver un dia de la semana")

	numDia = int(input("ingrese un numero para ver en que dia de la semana corresponde: "))

	if numDia == 1:
  		print("lunes")
	elif numDia == 2:
  		print("martes")
	elif numDia == 3:
  		print("miercoles")
	elif numDia == 4:
  		print("jueves")
	elif numDia == 5:
  		print("viernes")
	elif numDia == 6:
  		print("sabado")
	elif numDia == 7:
 		print("domingo")
	else:
  		print("error ingrese un numero del 1 al 7.")
if exercises == 8:
	#triangulo equilatero
	print("ingrese lo solicitado para determinar si el triangulo es equilatero o no")
	# variables side para los lados del triangulo
	side1 = int(input("ingrese el lado 1 del triangulo: "))
	side2 = int(input("ingrese el lado 2 del triangulo: "))
	side3 = int(input("ingrese el ultimo lado del triangulo: "))

	# proceso para determinar si el triangulo es equilatero

	if side1 == side2 and side2 == side3:
  		print("los tres datos son iguales esto significa que el triangulo es equilatero.")
	else:
  		print("no es equilatero.")
if exercises == 9:
	#suma o multiplicacion
	print("ingrese lo solicitado")
	# inicio
	a = int(input("ingrese un numero para a: "))
	b = int(input("ingrese un numero para b: "))

	# proceso
	addition = a + b
	if a > 0 and b > 0:
  		print("devido a que los dos numeros son positivos entonces se sumaran: ", addition)
	elif a < -1 and b < -1:
  		multiplication = -a * (-b)
  		print("en este caso se multiplicara: ", multiplication)

if exercises == 10:
	# signo zodiacal
	# incicio del programa
	print("ingresa tu dia nacimiento correspondiente a este se le dara su signo zodiacal.")
	# variables day y month para el ejercicio
	day = int(input("ingrese su dia de nacimiento: "))
	month = int(input("ingresa tu mes de nacimiento: "))

	if month == 3 and day >= 21 or month == 4 and day <= 19:
  		print("tu signo es aries.")
	elif month == 4 and day >= 20 or month == 5 and day <= 20:
 		 print("tu signo es tauro.")
	elif month == 5 and day >= 21 or month == 6 and day <= 20:
  		print("tu signo es geminis.")
	elif month == 6 and day >= 21 or month == 7 and day <= 22:
  		print("tu signo es cancer.")
	elif month == 7 and day >= 23 or month == 8 and day <= 22:
  		print("tu signo es leo.")
	elif month == 8 and day >= 23 or month == 9 and day <= 22:
 	 	print("tu signo es virgo.")
	elif month == 9 and day >= 23 or month == 10 and day <= 22:
  		print("tu signo es libra.")
	elif month == 10 and day >= 23 or month == 11 and day <= 21:
  		print("tu signo es escorpio.")
	elif month == 11 and day >= 22 or month == 12 and day <= 21:
  		print("tu signo es sagitario.")
	elif month == 12 and day >= 22 or month == 1 and day <= 19:
  		print("tu signo es capricornio.")
	elif month == 1 and day >= 20 or month == 2 and day <= 18:
  		print("tu signo es acuario.")
	elif month == 2 and day >= 19 or month == 3 and day <= 20:
  		print("tu signo es picis.")

if exercises == 11:
	# cuadrilatero
	print("ingrese los valores.")

	base = int(input("ingrese la base del cuadrilatero: "))
	heigth = int(input("ingrese la altura del cuadrilatero: "))



	if base == heigth:
  		print("el cuadrilatero es un cuadrado.")
  		side1 = int(input("ingrese el lado 1:"))
  		side2 = int(input("ingrese el segundo lado:"))
  		perimeter1 = 4 * base
  		print("el perimetro es:", perimeter1)
  		surface1 = side1 * side2
  		print("la superfifice es:", surface1)
	else:
  		print("el cuadrilatero es un rectangulo.")
  		perimeter2 = 2 * (base + heigth)
  		print("el perimetro es:", perimeter2)
  		surface2 = base * heigth
  		print("la superficie es:", surface2)

if exercises == 12:
	# descuentos
	# inicio
	print("BIENVENIDO")

	buys = int(input("ingrese el valor de sus compra para el descuento: "))

	# desarrollo del ejercicio 

	if buys <= 100:
  		discount1 = 5
  		amount_n1 = buys * (discount1 / 100)
 	 	price_f1 = buys - amount_n1
  		print("el precio fue de: ", price_f1)
  		print("el descuento en pesos es de: ", amount_n1)
	if buys >= 100 and buys <= 200:
  		discount2 = 10
  		amount_n2 = buys * (discount2 / 100)
  		price_f2 = buys - amount_n2
  		print("el precio en pesos es de: ", price_f2)
  		print("el descuento es de: ", amount_n2)
	else:
  		discount3 = 15
  		amount_n3 = buys * (discount3 / 100)
  		price_f3 = buys - amount_n3
  		print("el precio total en pesos fue de: ", price_f3)
  		print("el descuento es de: ", amount_n3)
if exercises == 13:
	# datos de nacimiento
	total_h = 0
	total_m = 0
	total_g = 0

	for i in range(5):
	day = int(input("Ingrese el día de nacimiento: "))
    	month = int(input("Ingrese el mes de nacimiento: "))
    	year = int(input("Ingrese el año de nacimiento: "))
    	sex = int(input("Ingrese el sexo (1-femenino, 2-masculino): "))

	if sex == 1:
        	total_m += 1
    	elif sex == 2:
        	total_h += 1

	print("Total de hombres:", total_h)
	print("Total de mujeres:", total_m)
	print("Total general:", total_g)

