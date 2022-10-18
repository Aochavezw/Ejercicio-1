def Saludo():
    return print("Hola Mundo")

def get_resistor_code(cadena):
    resistor_map = {
    "Negro": 0,
    "Marrón": 1,
    "Rojo": 2,
    "Naranja": 3,
    "Amarillo": 4,
    "Verde": 5,
    "Azul": 6,
    "Púrpura": 7,
    "Gris": 8,
    "Blanco": 9
    }

    cadena='Rojo-Púrpura-Verde'
    resistors=cadena.split('-')
    if len(resistors)>=2:
      resistorcode=str(resistor_map[resistors[0]]) + str(resistor_map[resistors[1]])
    else:
        resistorcode=str(resistor_map[resistors[0]])

    return print("El código es: ", resistorcode)

def isleap(año):

    if año % 4 != 0:
        mensaje="No es bisiesto"
    elif año % 4 == 0 and año % 100 != 0:
        mensaje="Es bisiesto"
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
        mensaje="No es bisiesto"
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
        mensaje="Es bisiesto"
    return print(año,mensaje)

def get_planetary_age(Planeta,edad_segundos):
    age_planetary_map = {
    "Mercurio": 0.2408467,
    "Venus": 0.615197226,
    "Tierra": 1,
    "Marte": 1.8808158,
    "Júpiter": 11.862612,
    "Saturno": 29.447498,
    "Urano": 84.016846,
    "Neptuno": 164.79132
    }

    edad_años=edad_segundos/31557600
    edad_planetaria=edad_años*age_planetary_map[Planeta]

    return print(round(edad_planetaria,2))