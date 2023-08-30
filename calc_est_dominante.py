import csv

# CARGA MATRIZ COSTOS

jugadores = 3

matriz_costos = [[[0 for _ in range(jugadores)] for _ in range(jugadores)] for _ in range(jugadores)]

# print(matriz_costos)

for matriz in range(3):
    nombre_archivo = "tabla" + str(matriz)

    with open(nombre_archivo + ".txt") as tablaf:
        reader = csv.reader(tablaf, delimiter=";")

        row_number = 0

        for row in reader:

            col_number = 0
            
            for item in row:

                tupla = tuple(map(lambda x: int(x), item.replace("(", "").replace(")", "").split(",")))

                matriz_costos[row_number][col_number][matriz] = tupla

                col_number += 1
            
            row_number += 1


# print(matriz_costos[0][0][0])

# CALCULO DE ESTRATEGIA DOMINANTE

# Jugador A

def calc_est_dominante_A():

    hubo_alguna = False

    for estrategia in range(3):
        dominante = es_dominante_en_A(estrategia)
        debilmente_dominante = es_debilmente_dominante_en_A(estrategia)
        dominada = es_dominada_en_A(estrategia)
        debilmente_dominada = es_debilmente_dominada_en_A(estrategia)

        if dominante:
            print("La estrategia {} es dominante para el jugador A".format(estrategia))
        
        if debilmente_dominante:
            print("La estrategia {} es debilmente dominante para el jugador A".format(estrategia))
        
        if dominada:
            print("La estrategia {} es dominada por las demás para el jugador A".format(estrategia))
        
        if debilmente_dominada:
            print("La estrategia {} es debilmente dominada por las demás para el jugador A".format(estrategia))
        
        hubo_alguna = hubo_alguna or dominante or debilmente_dominante
    
    if not hubo_alguna:
        print("El jugador A no tiene estrategias dominantes ni debilmente dominantes")


def es_dominante_en_A(estrategia):

    dominante = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominante = dominante and matriz_costos[estrategia][i][j][0] > matriz_costos[otra_estrategia][i][j][0]

                        if not dominante:
                            return False
    
    return dominante

def es_debilmente_dominante_en_A(estrategia):

    dominante = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominante = dominante and matriz_costos[estrategia][i][j][0] >= matriz_costos[otra_estrategia][i][j][0]

                        if not dominante:
                            return False
    
    return dominante

def es_dominada_en_A(estrategia):
    dominada = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominada = dominada and matriz_costos[estrategia][i][j][0] < matriz_costos[otra_estrategia][i][j][0]

                        if not dominada:
                            return False
    
    return dominada

def es_debilmente_dominada_en_A(estrategia):
    dominada = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominada = dominada and matriz_costos[estrategia][i][j][0] <= matriz_costos[otra_estrategia][i][j][0]

                        if not dominada:
                            return False
    
    return dominada

# Jugador B

def calc_est_dominante_B():

    hubo_alguna = False

    for estrategia in range(3):
        dominante = es_dominante_en_B(estrategia)
        debilmente_dominante = es_debilmente_dominante_en_B(estrategia)
        dominada = es_dominada_en_B(estrategia)
        debilmente_dominada = es_debilmente_dominada_en_B(estrategia)

        if dominante:
            print("La estrategia {} es dominante para el jugador B".format(estrategia))
        
        if debilmente_dominante:
            print("La estrategia {} es debilmente dominante para el jugador B".format(estrategia))

        if dominada:
            print("La estrategia {} es dominada por las demás para el jugador B".format(estrategia))
        
        if debilmente_dominada:
            print("La estrategia {} es debilmente dominada por las demás para el jugador B".format(estrategia))

        hubo_alguna = hubo_alguna or dominante or debilmente_dominante
    
    if not hubo_alguna:
        print("El jugador B no tiene estrategias dominantes ni debilmente dominantes")


def es_dominante_en_B(estrategia):

    dominante = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominante = dominante and matriz_costos[i][estrategia][j][1] > matriz_costos[i][otra_estrategia][j][1]

                        if not dominante:
                            return False
    
    return dominante

def es_debilmente_dominante_en_B(estrategia):

    dominante = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominante = dominante and matriz_costos[i][estrategia][j][1] >= matriz_costos[i][otra_estrategia][j][1]

                        if not dominante:
                            return False
    
    return dominante

def es_dominada_en_B(estrategia):
    dominada = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominada = dominada and matriz_costos[i][estrategia][j][1] < matriz_costos[i][otra_estrategia][j][1]

                        if not dominada:
                            return False
    
    return dominada

def es_debilmente_dominada_en_B(estrategia):
    dominada = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominada = dominada and matriz_costos[i][estrategia][j][1] <= matriz_costos[i][otra_estrategia][j][1]

                        if not dominada:
                            return False
    
    return dominada

# Jugador C

def calc_est_dominante_C():

    hubo_alguna = False

    for estrategia in range(3):
        dominante = es_dominante_en_C(estrategia)
        debilmente_dominante = es_debilmente_dominante_en_C(estrategia)
        dominada = es_dominada_en_C(estrategia)
        debilmente_dominada = es_debilmente_dominada_en_C(estrategia)

        if dominante:
            print("La estrategia {} es dominante para el jugador C".format(estrategia))
        
        if debilmente_dominante:
            print("La estrategia {} es debilmente dominante para el jugador C".format(estrategia))
        
        if dominada:
            print("La estrategia {} es dominada por las demás para el jugador C".format(estrategia))
        
        if debilmente_dominada:
            print("La estrategia {} es debilmente dominada por las demás para el jugador C".format(estrategia))
        
        hubo_alguna = hubo_alguna or dominante or debilmente_dominante
    
    if not hubo_alguna:
        print("El jugador C no tiene estrategias dominantes ni debilmente dominantes")


def es_dominante_en_C(estrategia):

    dominante = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominante = dominante and (matriz_costos[i][j][estrategia][2] > matriz_costos[i][j][otra_estrategia][2])

                        if not dominante:
                            return False
    
    return dominante

def es_debilmente_dominante_en_C(estrategia):

    dominante = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominante = dominante and (matriz_costos[i][j][estrategia][2] >= matriz_costos[i][j][otra_estrategia][2])

                        if not dominante:
                            return False
    
    return dominante

def es_dominada_en_C(estrategia):
    dominada = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominada = dominada and matriz_costos[i][j][estrategia][2] < matriz_costos[i][j][otra_estrategia][2]

                        if not dominada:
                            return False
    
    return dominada

def es_debilmente_dominada_en_C(estrategia):
    dominada = True

    for otra_estrategia in range(3):
            if estrategia != otra_estrategia:
                for i in range(3):
                    for j in range(3):
                        dominada = dominada and matriz_costos[i][j][estrategia][2] <= matriz_costos[i][j][otra_estrategia][2]

                        if not dominada:
                            return False
    
    return dominada

# Programa principal

print("Calculando estrategias dominantes: ")

print("JUGADOR A (ARGENTINO)")
calc_est_dominante_A()

print("JUGADOR B (MEXICANO)")
calc_est_dominante_B()

print("JUGADOR C (ESPAÑOL)")
calc_est_dominante_C()