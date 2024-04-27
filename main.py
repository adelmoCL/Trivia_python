import random
from validador import validate
from level import choose_level
from shuffle import shuffle_alt
from question import choose_q
from print_preguntas import print_pregunta
from verify import verificar
from preguntas import pool_preguntas
import time
import os
import sys
import random
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate

n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'



os.system(op_sys) 

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')

opcion = validate(['0', '1'], opcion)

if opcion == '0':
    print()
    time.sleep(2)
    os.system(op_sys)
    print("¡Hasta luego!")
    sys.exit()




while correcto and n_pregunta < 3 * p_level:
    
    if n_pregunta == 0:
        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        p_level = validate(['1', '2', '3'], p_level)
        p_level = int(p_level)

    if continuar == 'y':
        n_pregunta += 1
        nivel = choose_level(n_pregunta, str(p_level))
        print(f'Pregunta {n_pregunta}: Nivel {nivel.capitalize()}')
        enunciado, alternativas = choose_q(nivel)
        print_pregunta(enunciado, alternativas)

        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
        respuesta = validate(['a', 'b', 'c', 'd'], respuesta)
        correcto = verificar(alternativas, respuesta)

        if correcto and n_pregunta < 3 * p_level:
            print('Muy bien, sigue así!')
            continuar = input('¿Desea continuar? [y/n]: ').lower()
            continuar = validate(['y', 'n'], continuar)
            os.system(op_sys)
        elif correcto and n_pregunta == 3 * p_level:
            print(f'Felicitaciones, has respondido {3 * p_level} preguntas correctas.\nHas ganado la Trivia. ¡Gracias por Jugar, hasta luego!')
            time.sleep(3)
            os.system(op_sys)
            sys.exit()
        else: 
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.\n¡Sigue participando!')
            time.sleep(3)
            sys.exit()
    else: 
        print('Nos vemos la próxima vez, sigue practicando')
        time.sleep(3)
        sys.exit()
