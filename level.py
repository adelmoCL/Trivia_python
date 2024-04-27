def choose_level(n_pregunta, p_level):
    # Convertir el nivel a entero
    p_level = int(p_level)
    
    # 
    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        elif n_pregunta == 3:
            level = 'avanzadas'
        else:
            raise ValueError("Número de pregunta inválido para la cantidad de preguntas.")
    elif p_level == 2:
        if n_pregunta <= 2:
            level = 'basicas'
        elif n_pregunta <= 4:
            level = 'intermedias'
        elif n_pregunta <= 6:
            level = 'avanzadas'
        else:
            raise ValueError("Número de pregunta inválido para la cantidad de preguntas.")
    elif p_level == 3:
        if 0 < n_pregunta <= 3:
            level = 'basicas'
        elif 3 < n_pregunta <= 6:
            level = 'intermedias'
        elif 6 < n_pregunta <= 9:
            level = 'avanzadas'
        else:
            raise ValueError("Número de pregunta inválido para la cantidad de preguntas.")
    else:
        raise ValueError("Opción de nivel inválida.")
    
    return level




if __name__ == '__main__':
    # Verificar resultados
    print(choose_level(2, 2))  # Básicas
    print(choose_level(3, 2))  # Intermedias
    print(choose_level(7, 2))  # Avanzadas
    print(choose_level(4, 3))  # Intermedias
