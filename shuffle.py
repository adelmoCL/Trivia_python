import preguntas as p
import random

def shuffle_alt(pregunta):
    alternativas = pregunta['alternativas']
    
    random.shuffle(alternativas)
    
    return alternativas

if __name__ == '__main__':
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
