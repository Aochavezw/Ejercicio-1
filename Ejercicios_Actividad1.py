from src import Funciones_Actividad1 as fa

"Ejercicio 1: Escribe una función que imprima la cadena 'Hola Mundo'"

fa.Saludo()


"""Ejercicio2: Si desea construir algo usando una Raspberry Pi, probablemente use resistencias. Para este ejercicio, necesitas saber dos cosas sobre ellos:
•Cada resistencia tiene un valor específico,  los resistores son pequeños, tan pequeños que si imprimieras el valor de resistencia en ellos, sería difícil de leer.
•Para solucionar este problema, los fabricantes imprimen bandas codificadas por colores en las resistencias para indicar sus valores. Cada banda tiene una posición y un valor numérico.
•Las primeras 2 bandas de una resistencia tienen un esquema de codificación simple: cada color se asigna a un solo número. Por ejemplo, si imprimieran una banda marrón (valor 1) seguida de una banda verde (valor 5), se traduciría en el número 15.
•En este ejercicio vas a crear un programa útil para que no tengas que recordar los valores de las bandas. El programa tomará los nombres de los colores como entrada y generará un número de dos dígitos, ¡incluso si la entrada es de más de dos colores!
•Los colores de la banda se codifican de la siguiente manera:
•Negro: 0, Marrón: 1, Rojo: 2, Naranja: 3, Amarillo: 4, Verde: 5, Azul: 6, Púrpura: 7, Gris: 8, Blanco: 9
•El argumento de la función debe aceptar una cadena de colores separados por un guión."""

fa.get_resistor_code('Rojo-Púrpura-Verde')

fa.isleap(2016)

fa.get_planetary_age('Tierra',1000000000)
fa.get_planetary_age('Mercurio',2134835688)
fa.get_planetary_age('Venus',189839836)
fa.get_planetary_age('Marte',2129871239)
fa.get_planetary_age('Júpiter',901876382)
fa.get_planetary_age('Saturno',2000000000)
fa.get_planetary_age('Urano',1210123456)
fa.get_planetary_age('Neptuno',1821023456)




