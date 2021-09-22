import libreria as lc

def suvectores(v,w) :
    n = len(v)
    print(n)
    r = [(0,0)] *n
    for k in range(n):
        r[k]=lc.cplxsum(v[k],w[k])
    return r

def invector(a):
    n = len(v)
    print(n)
    r = [(0,0)] * n
    for k in range(n):
        r[k] = lc.cplxmult((-1,0),v[k])
    return r
def multesc(c,v):
    n = len(v)
    print(n)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = lc.cplxmult(c, v[k])
    return r

def summa(a,b):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxsum(a[j][k],b[j][k])
    return r
def mulma(c,a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxmult(c,a[j][k])
    return r
def invma(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):

        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxmult((-1,0),a[j][k])
    return r

def trama(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = a[k][j]
    return r

def conma(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] =  lc.cplxcon(a[j][k])
    return r
def addaga(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] =  lc.cplxcon(a[k][j])

    return r

def multmat(a,b):
    if (len(a[0]) != len(b)):
        return "Imposible"
    else:
        r = [[(0, 0) for x in b[0]] for x in a]
        for j in range(len(a)):
            for k in range(len(b[0])):
                resultado = (0, 0)
                for h in range(len(b)):
                    resultado = lc.cplxsum(lc.cplxmult(a[j][h], b[h][k]), resultado)
                r[j][k] = resultado
    return r

def unitario(c,a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxmult(a[j][k],a[j][k])
    return r
def vectensor(A,B):
    na = len(A)
    nb = len(B)
    nr = nb * na
    print(nr)
    R = [(0,0)] * nr
    index = 0
    for j in range(na):
        for k in range(nb):
            R[index] = lc.cplxmult(A[j], B[k])
            index = index + 1
    return R
def hermitanio(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):

        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxcon(a[k][j])
    resultado = (a == r)
    print(resultado)
    return r
def funmat(a,v):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):

        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxsum(lc.cplxmult(a[j][k],v[k]),lc.cplxmult(v[k],[j][k]))

    return r
def productointernov(a,b):
    n = len(a)
    print(n)
    r = [(0, 0)] * n
    for k in range(n):
            r[k] = lc.cplxmult(a[k], b[k])
    return r


def sumanorma(lista):
    n = len(a)
    suma = 0
    for numero in lista:
        suma += (numero ** 2)
    return suma


def raiznorma(a):
    n = len(a)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = (sumanorma(a))**0.5
    return r
def distancia(a,b):
    na = len(a)
    nb = len(b)
    r = [(0,0)] * na
    for k in range(na):
        r[k] = a[k] - b[k]
    return r
def valorabsoluto(a):
    n = len(a)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = list(map(lambda n: abs(n), a))
    return r
def normadistancia(lista):
    n = len(a)
    suma = 0
    for numero in lista:
        suma += (numero ** 2)
    return suma


def raizdistancia(a):
    n = len(a)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = (normadistancia(a))**0.5
    return r
def transpuesta(a):
    r=[[(0,0) for x in a] for x in a[0]]
    for j in range(len(a[0])):
        for k in range(len(a)):
            r[j][k]=a[k][j]
    return r

if __name__ == '__main__':
    print("vectores")
    v = [(2,8),(8,9),(6,7)]
    w = [(7,0),(9,10),(2,3)]
    print(v)
    print(w)
    print("suma de vectores")
    print(suvectores(v,w))
    print(" inverso adictivo  de vectores")
    print(invector(v))
    print(" multiplicacion de escalar a vector")
    print(multesc((1,0),v))
    a = [[(2,3),(3,4),(3,2)],
         [(1,1),(1,1),(1,1)],
         [(2,2),(3,3),(4,4)]]
    b = [[(4,4),(3,6),(3,7)],
         [(1,2),(1,2),(1,2)],
         [(1,1),(2,2),(3,3)]]
    print("matrices")
    print(a)
    print(b)
    print("suma de matriz")
    print(summa(a,b))
    print(" inversa adictiva de una matriz")
    print(invma(a))
    print("multiplicacion escalar con matriz")
    print(mulma((1,0),a))
    print("traspuesta de una matriz")
    print(trama(a))
    print("conjuncion de matriz")
    print(conma(a))
    print("adjunta daga de matriz/ vector")
    print(addaga(a))
    print("Producto de dos matrices (de tamaños compatibles)")
    print(multmat(a,b))
    print("matriz y vector")
    s = [(2,0),(0,1),(1,1)]
    c = [[(1.1),(1,1)],
         [(2,1),(1,2)],
         [(1,1),(1,1)]]
    print(s)
    print(c)
    print("Función para calcular una matriz sobre un vector.")
    print(c,s)
    print("Producto interno de dos vectores")
    v = [(2,8),(8,9),(6,7)]
    w = [(7,0),(9,10),(2,3)]
    s = [2,3,4]
    p = [3,4,6]
    print(productointernov(v,w))
    print("norma de un vector")
    print(sumanorma(s))
    print(raiznorma(s))
    print("distancia de dos vectores")
    print(distancia(s,p))
    print(valorabsoluto(distancia(s,p)))
    print(normadistancia(distancia(s,p)))
    print(raizdistancia(distancia(s,p)))
    print("Revisar si una matriz es unitaria")
    print(unitario(a,a))
    print("Revisar si una matriz es Hermitiana")
    print(hermitanio(a))
    t = [(0,2),(1,6)]
    R = [(0,-5),(3,4),(-2.1,0)]
    print("Producto tensor de dos matrices/vectores")
    print(vectensor(t,R))