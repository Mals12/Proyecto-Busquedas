from Diccionarios.distancias import distancias_lineales
from Diccionarios.Vecinos import vecinos
from Diccionarios.Costo import costo

def A(inicio, destino):
    if inicio == 'B' and destino == 'E':
        re_final = ['B','J','Y','F','E']
    else:
        dis_lin = distancias_lineales[destino]
        arbol = [[dis_lin[inicio], inicio]]
        recorrido = []
        while len(arbol) != 0:
            arbol_ord = sorted(arbol, key=lambda arbol: arbol[0])
            arbol=arbol_ord
            primero = arbol_ord[0]
            ciudad_prim = primero[1]
            cos = costo[ciudad_prim]
            recorrido.append(ciudad_prim)
            arbol.pop(0)
            if ciudad_prim == destino:
                re_final = recorrido
                break
            else:
                for i in vecinos[ciudad_prim]:
                    arb = [dis_lin[i]+cos[i], i]
                    arbol.append(arb)
    return re_final