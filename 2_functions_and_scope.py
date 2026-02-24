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
# - Encapsulamiento y visibilidad
# - Uso de nonlocal para variables internas

# 4️⃣ Variables en funciones
# - Variables locales: existen solo dentro de la función
# - Variables globales: definidas fuera de la función
# - Uso de global para modificar variables globales
# - Diferencia entre local, global y nonlocal

# 5️⃣ Funciones lambda (anónimas)
# - Funciones de una sola línea
# - Uso con map, filter, sorted, reduce
# - Diferencias con funciones normales

# 6️⃣ Funciones incorporadas de Python (built-in)
# - Funciones de tipo y estructura: len(), type(), range(), sorted()
# - Funciones matemáticas: sum(), max(), min(), abs()
# - Funciones de comprobación: isinstance(), all(), any()
# - Otras útiles: enumerate(), zip(), reversed()

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