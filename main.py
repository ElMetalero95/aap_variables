#saludo = "Hola "
#nombre = input ("Ingrese su Nombre")

#print(saludo + nombre)


 #num1 = int(input("Ingrese un numero "))
 #num2 = int(input("Ingrese otro numero "))

"""print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
"""

"""
if y Operadores de comparacion
"""

#print(5 < 10) #True
#print(2 > 20) #False
#print(6 <= 6) #True
#print(0 == 0) #True
"""
prom = input("pedir promedio")
si prom > 6 entonces
  aprueba
sino
  rerprueba
"""

#prom = int (input("pedir promedio "))

#if (prom > 6):
	#print("aprobado")
#else:
	#print("desaprobado")


"""nota1 = int (input("ingrese primera nota ")) 
nota2 = int (input("ingrese segunda nota ")) 
nota3 = int (input("ingrese tercera nota "))
prom = (nota1 + nota2 + nota3)/3

print ("El promedio es: %.2f" % prom)

if (prom > 6):
	 print("aprobado")
else:
	 print("desaprobado")
"""

num = int(input("ingrese nota "))

prom = 0
cant = 0

while (num !=0):
	if(num >=0 and num <=10):
	    prom = num + prom
	    cant = cant + 1
	    num = int(input("ingrese nota "))
	else:
		num = int(input("Valor fuera del rango por favor ingresa una nota entre 1 y 10. 0 para salir "))

print("prom %.2f y cant %i "% (prom,cant))

prom_final = prom/cant

print("promedio final %.2f "% prom_final)