from Diccionarios.distancias import distancias_lineales
from Diccionarios.Vecinos import vecinos

def greedy(inicio, destino):
    dis_lin = distancias_lineales[destino]
    arbol = [[dis_lin[inicio], inicio]]
    recorrido = []
    while len(arbol) != 0:
        arbol_ord = sorted(arbol, key=lambda arbol: arbol[0])
        primero = arbol_ord[0]
        ciudad_prim = primero[1]
        recorrido.append(ciudad_prim)
        arbol.pop(0)
        if ciudad_prim == destino:
            re_final = recorrido
            break
        else:
            for i in vecinos[ciudad_prim]:
                arb = [dis_lin[i], i]
                arbol.append(arb)
    return re_final
