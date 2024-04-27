import preguntas as p

def print_pregunta(enunciado, alternativas):
    print(enunciado)
    letras = ['A', 'B', 'C', 'D']
    for letra, (opcion, _) in zip(letras, alternativas):
        print(f"{letra}. {opcion}")

if __name__ == '__main__':
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    
    