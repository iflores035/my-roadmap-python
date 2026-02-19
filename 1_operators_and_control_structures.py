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

# << → desplazamiento izquierda
# → desplazamiento derecha

# Operador condicional (ternario)
# x if condicion else y → devuelve un valor según una condición

# Operadores estructurales / de acceso
# . → acceso a atributos
# [] → indexación o acceso por clave
# () → llamada a función
# : → definición de bloques
# , → separador / creación de tuplas

# → desempaquetado
# ** → desempaquetado de diccionarios

