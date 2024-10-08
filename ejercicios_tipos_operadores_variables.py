'''Operaciones básicas: 
Declara dos variables con números y realiza operaciones básicas como suma, resta, multiplicación y división. Imprime los resultados.'''
x = 5
y = 2
#suma
print(x + y)
#resta
print(x - y)
#multiplicacion
print(x * y)
#division
print(x / y)
#modulo
print(x % y)
#division entera
print(x // y)

'''Concatenación de cadenas: 
Declara dos variables tipo cadena (strings), concaténalas y muestra el resultado.
'''
#Nombre
primer_nombre = "Juan"
primer_apellido = "G"
print('Mi nombre es: ' + primer_nombre +' '+ primer_apellido + '.')

'''Cálculo de área de un cuadrado:
Declara una variable lado y calcula el área de un cuadrado usando la fórmula 
A=lado 
2
 .'''
l = 5
area_cuadrado_l =  5**2
print("Para un cuadrado de lado: " )
print(l)
print("Su area es de: ")
print(area_cuadrado_l)

'''Tipos de datos:
Declara variables de diferentes tipos de datos (entero, flotante, cadena) y muestra sus valores.
'''
numero_entero = 10
numero_flotante = 3.14
cadena = "Python"
print(numero_entero, numero_flotante, cadena)

'''Conversión de tipos:
Declara una variable numérica y conviértela en cadena. Luego declara una cadena y conviértela en número.'''
numero = 25
cadena = str(numero)
cadena_num = "10"
numero_convertido = int(cadena_num)
print(cadena, numero_convertido)
'''Cálculo del perímetro de un rectángulo:
Declara variables largo y ancho de un rectángulo y calcula su perímetro con la fórmula  P=2×(largo+ancho).'''
largo= 10
ancho= 5
perimetro= 2 * (largo+ancho)
print("Para un rectangulo de largo "+ str(largo) +" y de ancho "+ str(ancho) +". Su perimetro corresponde a: " + str(perimetro ))

'''Longitud de una cadena:
Usa la función len() para calcular la longitud de una cadena de texto.'''
texto = "Aprendiendo Python"
longitud = len(texto)
print(longitud)

'''Operaciones con flotantes:
Declara dos variables flotantes y realiza operaciones de suma, resta, multiplicación y división.'''
num1 = 5.5
num2 = 2.3
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(suma, resta, multiplicacion, division)

'''Cálculo del área de un círculo:
Declara una variable radio y calcula el área de un círculo usando la fórmula . Usa 3.1416 como valor de 𝜋
A=pir2'''
pi=3.1416
r=5
area_circulo =(pi * (r**2))
print("Para un circulo con radio de " +str(r)+ ". El valor de su area es: "+ str(area_circulo))

'''Operadores lógicos:
Declara dos variables booleanas y realiza operaciones lógicas como and, or y not.'''
bool1 = True
bool2 = False
resultado_and = bool1 and bool2
resultado_or = bool1 or bool2
resultado_not = not bool1
print(resultado_and, resultado_or, resultado_not)

'''Conversión de grados Fahrenheit a Celsius:
 Declara una variable en grados Fahrenheit y conviértela a Celsius usando la fórmula 
C= 5/9(F-32).'''
fahrenheit = 150
conversion_f_c = ((5.0/9.0)*(fahrenheit-32))
print("Para "+ str(fahrenheit) + " grados Fahrenheit, equivalen a "+ str(conversion_f_c) + " grados Celsius")

'''Promedio de tres números:
 Declara tres variables numéricas y calcula su promedio.
'''
num1 = 10
num2 = 20
num3 = 30
promedio = (num1 + num2 + num3) / 3
print(promedio)
