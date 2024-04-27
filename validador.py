def validate(opciones, eleccion):
    while eleccion not in opciones:
        eleccion = input('Opción no válida. Por favor, ingrese una de las opciones válidas: ').lower()
    return eleccion

if __name__ == '__main__':
    eleccion = input('Ingresa una Opción: ').lower()
    numeros = ['0', '1']
    validate(numeros, eleccion)
