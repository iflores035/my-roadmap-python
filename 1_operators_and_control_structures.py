'''
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

# OPERADORES EN PYTHON

#Operadores aritméticos
# → suma
suma = 10 + 5
print(f'suma = {suma}')

# → resta
resta = 10-20
print(f'resta = {resta}')

# → multiplicación
multiplicacion = 4 * 4
print(f'multiplicacion = {multiplicacion}')

# / → división (devuelve float)
division = 10 / 7
print(f'division = {division}')

# // → división entera
division_entera = 10 // 7
print(f'division entera = {division_entera}')

# % → módulo (resto)
resto = 10 % 7
print(f'modulo = {resto}')

# ** → potencia
potencia = 2**2
print(f'potencia = {potencia}')

# @ → multiplicación matricial
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])

mult_matricial = a @ b
print(f'multiplicación matricial = \n{mult_matricial}\n')



# Operadores de asignación
# = → asignación simple
asign_simple = 'se asigna de forma simple este string a la varible'
print(f'Asignación simple a variable asing_simple = {asign_simple}')

# += → suma y asigna
numero = 1
numero += 1
print(f'numero con suma y asigna = {numero}')

# -= → resta y asigna
numero -= 2
print(f'numero resta y asigna = {numero}')

# *= → multiplica y asigna
numero += 10
numero *= 2
print(f'numero multiplica y asigna = {numero}')

# /= → divide y asigna
numero /= 4
print(f'numero divide y asigna = {numero}')

# //= → división entera y asigna
numero //= 4
print(f'numero divide y asigna = {numero}')

# %= → módulo y asigna
numero = 10
numero %= 4
print(f'numero modulo y asigna = {numero}')

# **= → potencia y asigna
numero **= 2
print(f'numero potencia y asigna = {numero}')

# @= → multiplicación matricial y asigna
m1 = np.array([
    [1, 2],
    [3, 4]
])
m2 = np.array([
    [5, 6],
    [7, 8]
])

m1 @= m2
print(f'multiplicación matricial y asigna = \n{m1}\n')


# &= → AND bit a bit y asigna
# |= → OR bit a bit y asigna
# ^= → XOR bit a bit y asigna

# = → desplazamiento derecha y asigna
# <<= → desplazamiento izquierda y asigna
# := → operador walrus (asigna dentro de una expresión)


# Operadores de comparación
# == → igual a
nombre1 = 'ivan'
nombre2 = 'juan'
print (f'operador igual a = {nombre1 == nombre2}')

# != → distinto de
print (f'operador distinto de = {nombre1 != nombre2}')

# > → mayor que
num1 = 10
num2 = 12
print(f'el numero {num1} > {num2} = {num1 > num2}')

# < → menor que
print(f'el numero {num1} < {num2} = {num1 < num2}')

# >= → mayor o igual
print(f'el numero {num1} >= {num2} = {num1 >= num2}')

# <= → menor o igual
print(f'el numero {num1} <= {num2} = {num1 <= num2}')

# Operadores lógicos
# and → AND lógico
a = 1
b = 1
c = 2
print(f'a=b y b=c / donde a=1, b=1 y c=2:  {(a == b) and (b == c)}')

# or → OR lógico
print(f'a=b o b=c / donde a=1, b=1 y c=2:  {(a == b) or (b == c)}')

# not → negación lógica
print(f'NOT (a=b o b=c) / donde a=1, b=1 y c=2:  {not((a == b) or (b == c))}')


# Operadores de identidad
# is → verifica si son el mismo objeto
lista1 = [10, 20, 30]
lista2 = lista1
print(f'lista1 es el mismo objeto que lista2 = {lista1 is lista2}')

# is not → verifica si no son el mismo objeto
print(f'lista1 NO es el mismo objeto que lista2 = {lista1 is not lista2}')

# Operadores de pertenencia
# in → verifica pertenencia
print(f'20 esta en lista1 = {20 in lista1}')

# not in → verifica no pertenencia
print(f'20 NO esta en lista1 = {20 not in lista1}')

# Operadores bit a bit
numbit1 = 0b0101
numbit2 = 0b1101
print(f'numbit1 = {bin(numbit1)}')
print(f'numbit2 = {bin(numbit2)}')

# & → AND bit a bit
print(f'numbit1 AND numbit2 = {bin(numbit1 & numbit2)}')

# | → OR bit a bit
print(f'numbit1 OR numbit2 = {bin(numbit1 | numbit2)}')

# ^ → XOR bit a bit
print(f'numbit1 XOR numbit2 = {bin(numbit1 ^ numbit2)}')

# ~ → NOT bit a bit (inversión)
print(f'NOT numbit1 = {bin(~numbit1)}')
print(f'NOT numbit1 con mascara = {bin(~numbit1 & 0b1111)}')

# << → desplazamiento izquierda
print(f'desplazamiento izquierda 1101 (numbit2) << 1 = {bin(numbit2 << 1)}')

# → desplazamiento derecha
print(f'desplazamiento derecha 1101 (numbit2) >> 2 = {bin(numbit2 >> 2)}')

# Operador condicional (ternario)
# x if condicion else y → devuelve un valor según una condición
# variable = valor_si_es_verdadero if condicion else valor_si_es_falso
vida = 100
dano = 90
vida = (vida-dano) if (vida-dano>0) else 0
print(f'vida = {vida}')

# Operadores estructurales / de acceso
# . → acceso a atributos
saludo = 'hola'
print(f'Caso de uso del punto en un objeto, cambia texto a mayuscula = {saludo.upper()}')

# [] → indexación o acceso por clave
nombres = ['ivan', 'karen', 'andrea', 'michelle']
print(f'Utilización de operador de acceso [1] = {nombres[1]}')
print(f'Utilización de operador de acceso [1:3] = {nombres[1:3]}')
nombres_dic = {'nombre': 'ivan', 'edad': 50}
print(f'Acceso diccionario dato edad = {nombres_dic['edad']}')

# () → llamada a función
print('ejemplo de llamada a función print()')

# : → definición de bloques
if num1 == 1:
    print('ejemplo de : como definición de bloque')
else:
    print('ejemplo de : como definición de bloque')

# , → separador / creación de tuplas
tupla = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')
print(f'Imprime tupla = {tupla}')

# * → desempaquetado
print('desempaquetado tupla * = ', *tupla)

# ** → desempaquetado de diccionarios
dic = {**nombres_dic}
print('ejemplo desempaquetado de dicicionario = ', dic)


# ** ESTRUCTURAS DE CONTROL **

# 1. ESTRUCTURAS CONDICIONALES
var1 = 30
var2 = 30

# if: Evalúa una condición inicial.
if var1 > var2:
    print(f'condición IF: {var1} es mayor que {var2}')

# elif: Evalúa condiciones adicionales si la anterior fue falsa.
if var1 > var2:
    print(f'condición IF: {var1} es mayor que {var2}')
elif (var1 < var2):
    print(f'condición IF: {var1} es menor que {var2}')

# else: Ejecuta un bloque si ninguna condición previa se cumplió.
if var1 > var2:
    print(f'condición IF: {var1} es mayor que {var2}')
elif (var1 < var2):
    print(f'condición IF: {var1} es menor que {var2}')
else:
    print(f'los números {var1} y {var2} son iguales')

# 2. ESTRUCTURAS DE BUCLE (ITERATIVAS)
# for: Itera sobre elementos de una secuencia o iterable.
for i in range(5):
    print(i)

# while: Ejecuta un bloque mientras una condición sea verdadera.
j=0
while j<=5:
    print(j)
    j+=1


# 3. CONTROL DE FLUJO DENTRO DE BUCLES
# break: Termina el bucle prematuramente.
for i in range(10):
    print(i)
    if i == 5:
        break
print('buble terminado con break')

# continue: Salta a la siguiente iteración del bucle.
for i in range(10):
    if i == 5:
        print(f'nos saltamos la iteración {i}')
        continue
        
    print(i)

# else (en bucles): Se ejecuta solo si el bucle terminó sin interrupción (sin break).

numeros = (10,11,3,5,6,)
for i in numeros:
    if i == 100:
        print('numero 100 encontrado')
else:
    print('numero 100 no encontrado')


# 4. GESTIÓN DE EXCEPCIONES
# try: Bloque donde se intenta ejecutar código que puede fallar.
# except: Captura y maneja errores específicos.
# else (en try): Se ejecuta si no hubo ninguna excepción.
# finally: Bloque que se ejecuta siempre, ideal para limpieza.
try:
    numerador = 10
    denominador = 10
    sum = numerador / denominador
except ZeroDivisionError:
    print ('no se puede dividir por 0')
else:
    print('no hay error continua el resto del programa')
finally:
    print('esta parte del codigo siempre se ejecutará')

# except*: Maneja grupos de excepciones (Python 3.11+).
# raise: Lanza una excepción de forma manual.
grupo = ExceptionGroup('fallos detectados',[
    ValueError("Formato malo"),
    TypeError("tipo no permitido"),
    ValueError('dato mal'),
    RuntimeError('el sistema fallo')
])
try:
    raise grupo
except* ValueError as eg:
    print(f'Captura de errores: {eg.exceptions}')
except* TypeError as eg:
    print(f'Captura de errores: {eg.exceptions}')
except* RuntimeError as eg:
    print(f'Captura de errores: {eg.exceptions}')


# assert: Verifica una condición y lanza AssertionError si es falsa.
prueba_assert = 100
print(f'prueba assert = {prueba_assert}')
assert prueba_assert == 100, 'error, prueba assert debe ser 1000'





# 5. EMPAREJAMIENTO DE PATRONES ESTRUCTURALES (Python 3.10+)
# match: Sujeto a comparar.
# case: Patrón específico a evaluar.




# 6. GESTIÓN DE CONTEXTO Y RECURSOS
# with: Administra recursos (abrir/cerrar) de forma segura.




# 7. CONTROL ASÍNCRONO (CONCURRENCIA)
# async for: Itera sobre iterables asíncronos.
# async with: Gestiona contextos asíncronos.
# await: Pausa la ejecución hasta que una tarea asíncrona finalice.




# 8. RETORNO Y GENERADORES
# return: Sale de una función devolviendo un valor.
# yield: Pausa una función devolviendo un valor (generador).
# yield from: Delega la generación a otro iterable o subgenerador.



# 9. OTROS
# pass: Sentencia nula que sirve como marcador de posición.