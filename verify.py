import preguntas as p

def verificar(alternativas, eleccion):
    eleccion_index = ['a', 'b', 'c', 'd'].index(eleccion)
    
    opcion_seleccionada = alternativas[eleccion_index]
    
    if opcion_seleccionada[1] == 1:
        correcto = True
        print('Respuesta Correcta')
    else:
        correcto = False
        print('Respuesta Incorrecta')
    
    return correcto

if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
