'''
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
'''

# =====================================================
# 📌 TEMARIO UNIFICADO Y COMPLETO DE FUNCIONES EN PYTHON
# =====================================================

# 1️⃣ Conceptos Básicos de Funciones
# - Definición con def
# - Llamada / invocación de la función
# - Bloque de código reutilizable
# - Diferencia entre función y procedimiento (retorna valor o no)
# - Documentación con docstrings ("""comentario""")

def saludo():
    '''Saluda al usuario al ingresar al sistema.'''
    print(f'Hola... ¿como estas?')

saludo()


# 2️⃣ Tipos de Funciones según parámetros y retorno
# 1. Sin parámetros ni retorno
saludo()

# 2. Con uno o varios parámetros, sin retorno
def saludo_personalizado(nombre):
    '''Saluda al usuario al ingresar al sistema

       Parámetros:
       nombre (string) = nombre del usuario
       '''
    
    print(f'Hola {nombre}... ¿como estas?')

saludo_personalizado('Karen')


# 3. Con parámetros y retorno
def saludo_especial(name):
    '''Crea mensaje de saludo al usuario
    
    Parámetros:
    nombre (str) = nombre del usuario

    Retorna:
    str: mensaje de saludo al usuario
    '''
    return f'hola {name}... ¿estas bien?'

print(saludo_especial('Iván'))


# 4. Con parámetros por defecto
def saludo_porDefecto(nombre = 'Visita'):
    '''Saluda al usuario con ingresa al sistema

    Parameters:
    nombre (str) = nombre del usuario, por defecto 'Visita'
    '''
    print (f'Hola {nombre}, bienvenido')

saludo_porDefecto()
saludo_porDefecto('Erwin')


# 5. Con número variable de argumentos (*args)
def saludo_personas(*personas):
    '''Saluda a varias personas que ingresan al sistema
    
    Parameters:
    *personas (str) = nombre de las personas, recibido como tupla
    '''
    for persona in personas:
        print(f'Hola {persona}... saludos.')

saludo_personas('ivan', 'andrea', 'michelle')

# 6. Con argumentos nombrados variables (**kwargs)
def informacion_persona(**kwargs):
    '''
    Imprime información de una persona dada

    Parameters:
    **kwargs = nombre y edad, recibido como diccionario 
    '''
    print(f"nombre: {kwargs['nombre']}, edad: {kwargs['edad']}")

datos = {'nombre': 'ivan',
         'edad': 50}
informacion_persona(**datos)

# 7. Combinación de obligatorios, por defecto, *args y **kwargs
def material(tipo, *args, **kwargs):
    '''Imprime tipo de material, los repuestos y el nombre del cliente y dirección
    
    parameters:
    tipo (str) = tipo de material (ej: repuesto)
    *args (str) = repuestos que cliente comprará
    **kwargs (str) = cliente y dirección del cliente
    '''
    print(f'tipo: {tipo}')

    print('repuestos: ')
    for rep in args:
        print(f'--> {rep}')

    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


material('repuesto', 'aaa', 'bbb', 'ccc', cliente='BHP', direccion='sta mercedes')


# 3️⃣ Funciones anidadas
# - Funciones dentro de funciones
# - Uso de nonlocal para variables internas
# - Encapsulamiento y visibilidad

def externa():
    '''llama función interna para imprimir
    '''
    def interna():
        '''Imprime que tipo de función es
        '''
        print('soy una función interna anidada')

    interna() 

externa()


def crea_sumador(*args):

    suma = 0

    def sumador(*valores):
        for valor in valores:
            nonlocal suma
            suma += valor       
        
        return suma

    sumador(*args)
    return sumador

#sumador(10,11,3,5,20) // esto genera error por que la función esta encapsulada

s = crea_sumador()

print(f'resultado = {s(10,11,3,5,20)}')
print(f'resultado = {s(10)}')


# 4️⃣ Variables en funciones
# - Variables locales: existen solo dentro de la función
def ejvlocal():
    a = 1
    return a

# a += 1   --- esto genera error por que es una variable local
print(f'prueba de variable local: {ejvlocal()}')


# - Variables globales: definidas fuera de la función
vg = 1 #global

def ejvglobal():
    vg = 2
    return vg

print(f'variables global: {vg}')
print(f'retorno de la función: {ejvglobal()}')
print(f'nuevo valor de variable: {vg}')

# - Uso de global para modificar variables globales
vg2 = 1 #global

def ejvglobal2():
    global vg2
    vg2 = 2
    return vg2

print(f'variables global: {vg2}')
print(f'retorno de la función: {ejvglobal2()}')
print(f'nuevo valor de variable: {vg2}')

# - Diferencia entre local, global y nonlocal
varglob = 'global' # global

def diflgn():
    varloc = 'local'
    varnoloc = 'aaa'

    def interior():
        nonlocal varnoloc
        varnoloc = 'no local'
        return varnoloc
    
    interior()
    return varloc, varnoloc

print (f'variable global = {varglob}')
print (f'variables local = {diflgn()}')


# 5️⃣ Funciones lambda (anónimas)
# - Funciones de una sola línea
# - Diferencias con funciones normales
suma = lambda numero: numero + 1
print (f'suma = {suma(5)}')

persona = lambda nombre, edad : print(f'Nombre: {nombre} edad: {edad}')
persona('ivan', 50)

resta = lambda a,b:a-b
print(f'resta = {resta(10,5)}')


# - Uso con map, filter, sorted, reduce
lista = [1,2,3,4,5]
print(f'Imprime lista = {lista}')

lista2 = list(map(lambda x:x+1, lista))
print(f'Imprime lista sumando 1 = {lista2}')

lista3 = sorted(lista2,reverse=True)
print(f'Imprime lista = {lista3}')




# 6️⃣ Funciones incorporadas de Python (built-in)
# - Funciones de tipo y estructura: len(), type(), range(), sorted()

# len()  --> devuelve el largo de un objeto
texto = 'hola'
print(f'El largo del texto "{texto}" es: {len(texto)}')

# type() --> devuelve el tipo de objeto
print(f'El tipo de la variable "{texto}" es: {type(texto)}')

# range() --> Genera una secuencia de números. Devuelve un objeto especial tipo range.
# 1 parametro
print(f'range de 1 parametro valor 5: {list(range(5))}')
# 2 parametros
print(f'range de 2 parametro valor 1,5: {list(range(1,5))}')
# 3 parametros
print(f'range de 3 parametro valor 0,10,2: {list(range(0,10,2))}')


#sorted() --> Devuelve una nueva lista ordenada a partir de un iterable (no modifica el original).
palabra = 'hola mundo'
numeros = [3,2,1,6,5,4,8,9,0]
print (f'orden de letras de fase "hola mundo": {sorted(palabra)}')
print (f'orden de numeros {numeros} --> {sorted(numeros)}')


# - Funciones matemáticas: sum(), max(), min(), abs()
print(f'suma de numeros {numeros} = {sum(numeros)}')
print(f'máximo de la lista {numeros} = {max(numeros)}')
print(f'minimo de la lista {numeros} = {min(numeros)}')
print(f'valor absoluto del número -124 = {abs(-124)}')

# - Funciones de comprobación: isinstance(), all(), any()
# isinstance() --> Verifica si un objeto es instancia de un tipo específico.
num = 10,5
print(f'variable num es int = {isinstance(num, int)}')

# all() --> Devuelve True si todos los elementos del iterable son verdaderos.
a = True
b = False
print(f' las variables a y b son todas verdaderas?: {all([a,b])}')

#any()
print(f' las variables a y b hay alguna verdadera?: {any([a,b])}')


# - Otras útiles: enumerate(), zip(), reversed()
# enumerate() --> para cuando quiero saber el índice y el valor al mismo tiempo
print('Ejemplo de enumerate():')
for clave, valor in enumerate(numeros):
    print (f'clave: {clave} / valor: {valor}')

# zip() --> Une varios iterables elemento por elemento.
nombres = ['ivan', 'karen', 'juan']
edades = [50, 47, 83]
personas = zip(nombres, edades)
print (list(personas))

# reversed() --> Solo invierte el orden actual
print(f'revierte orden de la lista {nombres}, quedando asi {list(reversed(nombres))}')



# 7️⃣ Funciones recursivas
# - Función que se llama a sí misma
# - Caso base obligatorio
# - Ejemplo clásico: factorial o Fibonacci

# 8️⃣ Funciones como objetos
# - Asignación de funciones a variables
# - Paso de funciones como argumentos a otras funciones
# - Retorno de funciones desde otras funciones

# 9️⃣ Decoradores
# - Concepto y sintaxis (@decorador)
# - Decoradores con o sin parámetros
# - Uso práctico para logging, validación o cronometraje

# 10️⃣ Anotaciones y tipado
# - Tipado de parámetros y retorno (->)
# - Uso de typing para hints avanzados (List, Dict, Callable)

# 11️⃣ Generadores y yield
# - Funciones generadoras (yield)
# - Iteración perezosa
# - Delegación con yield from

# 12️⃣ Funciones asíncronas
# - async def y await
# - async for, async with
# - Integración con asyncio

# 13️⃣ Ejercicio obligatorio (alineado al tuyo)
# 1. Funciones básicas:
#    - Sin parámetros ni retorno
#    - Con parámetros, con y sin retorno
#    - Con parámetros por defecto
#    - Con *args y **kwargs
# 2. Funciones dentro de funciones
# 3. Uso de funciones built-in dentro de tus funciones
# 4. Prueba de variables locales y globales
# 5. Cada ejemplo debe imprimir resultados

# 14️⃣ Ejercicio opcional / dificultad extra
# - Función que recibe dos cadenas de texto y retorna un número
# - Recorre números del 1 al 100:
#   - Múltiplo de 3 → imprimir primer parámetro
#   - Múltiplo de 5 → imprimir segundo parámetro
#   - Múltiplo de 3 y 5 → imprimir concatenación
#   - Si no es múltiplo → imprimir el número y contar cuántas veces ocurre
# - Retorna el total de números impresos

# 15️⃣ Extras recomendables para reforzar
# - Decoradores simples
# - Funciones lambda y map/filter
# - Generadores para iteraciones grandes
# - Funciones asíncronas para tareas concurrentes

# 💡 Consejo de estudio:
# 1. Repasa la teoría de cada sección.
# 2. Escribe al menos un ejemplo práctico por cada punto.
# 3. Usa print() para mostrar resultados y verificar comprensión.
# 4. Avanza hacia los ejercicios obligatorios y luego al opcional.