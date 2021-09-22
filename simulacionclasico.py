import unittest

import libreria as lc
# EXPERIMENTOS CANICAS
def multiplicarMatrizMatrizBool(a,b):
    r = [[0 for x in b[0]] for x in a]
    for j in range(len(a)):
        for k in range(len(b[0])):
            e = 0
            for h in range(len(b)):
                e += a[j][h]*b[h][k]
            r[j][k]= e
    return r

def clikearBool(a,click):
    while click>1:
        a=multiplicarMatrizMatrizBool(a,a)
        click-=1
    return a

def simuladorBool(a,click,estado):
    a1 =clikearBool(a,click)
    estado=multiplicarMatrizMatrizBool(a1,lc.transpuesta([estado]))
    return estado
# EXPERIMENTO MULTIPLE RENDIJA CLASICO
def multiplicacionClasico(c,d):
    a1,b1,a2,b2=c[0],c[1],d[0],d[1]
    e = (0,0)
    if (a1==0 or a2==0):
        e = (0,1)
    else:
        e = (a1*a2,b1*b2)
    return e
def sumaClasico(a,b):
    a1,b1,a2,b2=a[0],a[1],b[0],b[1]
    r =0
    if (b1==b2):
        r = (a1+a2,b1)
    else:
        r = (a1*b2+a2*b1,b1*b2)
    return r
def multiplicarMatrizMatrizClasico(c,d):
    r=[[0 for x in d[0]] for x in c]
    for j in range(len(c)):
        for k in range(len(d[0])):
            e=(0,1)
            for h in range(len(d)):
                e=sumaClasico(multiplicacionClasico(c[j][h],d[h][k]),e)
            r[j][k]=e
    return r
def simuladorClasico(a,estado):
    r=multiplicarMatrizMatrizClasico(a,a)
    estadoFinal=multiplicarMatrizMatrizClasico(r,lc.transpuesta([estado]))
    return r,estadoFinal
# EXPERIMENTO MULTIPLE RENDIJA CUANTICO
def multiplicacionCuantico(c,d):
    a1,b1,a2,b2=c[0],c[1],d[0],d[1]
    r = lc.cplxmult(a1, a2)
    return (r, b1 * b2)
def sumaCuantico(a,b):
    a1,b1,a2,b2=a[0],a[1],b[0],b[1]
    r=lc.cplxsum(a1,a2)
    return (r,b1+b2)
def multiplicarMatrizMatrizCuantico(c,d):
    r=[[0 for x in d[0]] for x in c]
    for j in range(len(c)):
        for k in range(len(d[0])):
            e =((0,0),1)
            for h in range(len(d)):
                e =sumaCuantico(multiplicacionCuantico(c[j][h],d[h][k]),e)
            r[j][k]= e
    return r
def simuladorCuantico(a,v):
    a = multiplicarMatrizMatrizCuantico(a,a)
    return a[v]

if __name__ == '__main__':
    unittest.main()
