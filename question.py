import preguntas as p
import random
from shuffle import shuffle_alt

opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}

def choose_q(dificultad):
    preguntas_disponibles = opciones[dificultad]
    
    n_elegido = random.choice(preguntas_disponibles)
    
    preguntas_disponibles.remove(n_elegido)
    
    pregunta = p.pool_preguntas[dificultad][f'pregunta_{n_elegido}']
    
    alternativas = shuffle_alt(pregunta)
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    for _ in range(3):
        pregunta, alternativas = choose_q('basicas')
        print(f'El enunciado es: {pregunta}')
        print(f'Las alternativas son: {alternativas}')
