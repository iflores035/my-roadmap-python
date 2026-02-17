'''
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
'''

# Sito oficial Python https://www.python.org/

# En python solo existe como comentario los de línea anteponiendo el signo #
# Los comentarios multilínea no están soportados como otros lenguajes /*  */
'''
La triple comilla parece un comentario multilinea
técnicamente no es un comentario, si no un string multilinea
se usa principalmente para:
     - docstring (documentación de funciones, clases y módulos)
     - documentación formal del código
Si lo usuamos suelto, Python lo interpreta como un string que no se usa
'''

nombre = 'Ivan' # variable nombre
PI = 3.14 # Python no soporta constantes, pero de usarlas el nombre sería todo con mayusculas

# Variables representando tipos de datos primitivos

#Integer	Números enteros
numero = 10

#Float / Double	Decimales
numero2 = 10.75

#Boolean	Lógica
flag = True

#Char	Carácter individual
letra = 'a'

#String	Texto
cadena = 'esto es un string'

#Null	Ausencia de valor
variable = None

# Hola Python por terminal
print('¡Hola, Python!')