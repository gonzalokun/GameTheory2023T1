import csv

# CARGA MATRIZ COSTOS

jugadores = 3

matriz_costos = [[[0 for _ in range(jugadores)] for _ in range(jugadores)] for _ in range(jugadores)]
nombres_estrategias = ["Vuelo de 1 escala", "Vuelo de 2 escalas", "Vuelo directo"]

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
            print("La estrategia {} es dominante para el jugador A".format(nombres_estrategias[estrategia]))
        
        if debilmente_dominante:
            print("La estrategia {} es debilmente dominante para el jugador A".format(nombres_estrategias[estrategia]))
        
        if dominada:
            print("La estrategia {} es dominada por las demás para el jugador A".format(nombres_estrategias[estrategia]))
        
        if debilmente_dominada:
            print("La estrategia {} es debilmente dominada por las demás para el jugador A".format(nombres_estrategias[estrategia]))
        
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
            print("La estrategia {} es dominante para el jugador B".format(nombres_estrategias[estrategia]))
        
        if debilmente_dominante:
            print("La estrategia {} es debilmente dominante para el jugador B".format(nombres_estrategias[estrategia]))

        if dominada:
            print("La estrategia {} es dominada por las demás para el jugador B".format(nombres_estrategias[estrategia]))
        
        if debilmente_dominada:
            print("La estrategia {} es debilmente dominada por las demás para el jugador B".format(nombres_estrategias[estrategia]))

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
            print("La estrategia {} es dominante para el jugador C".format(nombres_estrategias[estrategia]))
        
        if debilmente_dominante:
            print("La estrategia {} es debilmente dominante para el jugador C".format(nombres_estrategias[estrategia]))
        
        if dominada:
            print("La estrategia {} es dominada por las demás para el jugador C".format(nombres_estrategias[estrategia]))
        
        if debilmente_dominada:
            print("La estrategia {} es debilmente dominada por las demás para el jugador C".format(nombres_estrategias[estrategia]))
        
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

print("----- Calculando estrategias dominantes: -----")

print("----- JUGADOR A (ARGENTINO) -----")
calc_est_dominante_A()

print("----- JUGADOR B (MEXICANO) -----")
calc_est_dominante_B()

print("----- JUGADOR C (ESPAÑOL) -----")
calc_est_dominante_C()

def encontrar_equilibrio_nash():
    equilibrios_nash = []
    
    # Verificar posibles equilibrios de Nash
    for estrategia_A in range(3):
        for estrategia_B in range(3):
            for estrategia_C in range(3):
                es_equilibrio = True
                
                for alt_A in range(3):
                    if matriz_costos[alt_A][estrategia_B][estrategia_C][0] >= matriz_costos[estrategia_A][estrategia_B][estrategia_C][0]:
                        es_equilibrio = False
                        break
                
                for alt_B in range(3):
                    if matriz_costos[estrategia_A][alt_B][estrategia_C][1] >= matriz_costos[estrategia_A][estrategia_B][estrategia_C][1]:
                        es_equilibrio = False
                        break
                
                for alt_C in range(3):
                    if matriz_costos[estrategia_A][estrategia_B][alt_C][2] >= matriz_costos[estrategia_A][estrategia_B][estrategia_C][2]:
                        es_equilibrio = False
                        break
                
                if es_equilibrio:
                    equilibrios_nash.append((estrategia_A, estrategia_B, estrategia_C))
                    
    if equilibrios_nash:
        nombre_equilibrio = tuple(map(lambda x: nombres_estrategias[x], list(equilibrios_nash[0])))
        print(f"Se han encontrado los siguientes equilibrios de Nash: {nombre_equilibrio}")
    else:
        print("No se han encontrado equilibrios de Nash.")

def encontrar_equilibrio_nash_debil():
    equilibrios_nash = []
    
    for estrategia_A in range(3):
        for estrategia_B in range(3):
            for estrategia_C in range(3):
                es_equilibrio = True
                
                for alt_A in range(3):
                    if matriz_costos[alt_A][estrategia_B][estrategia_C][0] > matriz_costos[estrategia_A][estrategia_B][estrategia_C][0]:
                        es_equilibrio = False
                        break
                
                for alt_B in range(3):
                    if matriz_costos[estrategia_A][alt_B][estrategia_C][1] > matriz_costos[estrategia_A][estrategia_B][estrategia_C][1]:
                        es_equilibrio = False
                        break
                
                for alt_C in range(3):
                    if matriz_costos[estrategia_A][estrategia_B][alt_C][2] > matriz_costos[estrategia_A][estrategia_B][estrategia_C][2]:
                        es_equilibrio = False
                        break
                
                if es_equilibrio:
                    equilibrios_nash.append((estrategia_A, estrategia_B, estrategia_C))
                    
    if equilibrios_nash:
        nombre_equilibrio = tuple(map(lambda x: nombres_estrategias[x], list(equilibrios_nash[0])))
        print(f"Se han encontrado los siguientes equilibrios de Nash: {nombre_equilibrio}")
    else:
        print("No se han encontrado equilibrios de Nash débiles.")

encontrar_equilibrio_nash()
encontrar_equilibrio_nash_debil()

print("----- MEJORES ESTRATEGIAS -----")

mejores_estrategias_A = [[0 for _ in range(3)] for _ in range(3)]
mejores_estrategias_B = [[0 for _ in range(3)] for _ in range(3)]
mejores_estrategias_C = [[0 for _ in range(3)] for _ in range(3)]

def mejor_respuesta_A(estrategia_B, estrategia_C):
    mejor_pago = matriz_costos[0][estrategia_B][estrategia_C][0]
    mejor_estrategia_A = 0
   
    for estrategia_A in range(3):
        pago_actual = matriz_costos[estrategia_A][estrategia_B][estrategia_C][0]
       
        if pago_actual > mejor_pago:
            mejor_pago = pago_actual
            mejor_estrategia_A = estrategia_A

    mejores_estrategias_A[estrategia_B][estrategia_C] = mejor_estrategia_A
     
    return mejor_estrategia_A

def mejor_respuesta_B(estrategia_A, estrategia_C):
    mejor_pago = matriz_costos[estrategia_A][0][estrategia_C][1]
    mejor_estrategia_B = 0
   
    for estrategia_B in range(3):
        pago_actual = matriz_costos[estrategia_A][estrategia_B][estrategia_C][1]
       
        if pago_actual > mejor_pago:
            mejor_pago = pago_actual
            mejor_estrategia_B = estrategia_B

    mejores_estrategias_B[estrategia_A][estrategia_C] = mejor_estrategia_B

    return mejor_estrategia_B

def mejor_respuesta_C(estrategia_A, estrategia_B):
    mejor_pago = matriz_costos[estrategia_A][estrategia_B][0][2]
    mejor_estrategia_C = 0
   
    for estrategia_C in range(3):
        pago_actual = matriz_costos[estrategia_A][estrategia_B][estrategia_C][2]
       
        if pago_actual > mejor_pago:
            mejor_pago = pago_actual
            mejor_estrategia_C = estrategia_C
           
    mejores_estrategias_C[estrategia_A][estrategia_B] = mejor_estrategia_C
     
    return mejor_estrategia_C

def cargar_mejores_respuestas():
    for estrategia_A in range(3):
        for estrategia_B in range(3):
            for estrategia_C in range(3):
                mejor_respuesta_A(estrategia_B, estrategia_C)
                mejor_respuesta_B(estrategia_A, estrategia_C) 
                mejor_respuesta_C(estrategia_A, estrategia_B)  

def print_mejores_estrategias_con_nombre(mej_est):
    print(list(map(lambda x: list(map(lambda y: nombres_estrategias[y], x)), list(mej_est))))

cargar_mejores_respuestas()

print("Mejores estrategias de A")
print_mejores_estrategias_con_nombre(mejores_estrategias_A)

print("Mejores estrategias de B")
print_mejores_estrategias_con_nombre(mejores_estrategias_B)

print("Mejores estrategias de C")
print_mejores_estrategias_con_nombre(mejores_estrategias_C)
