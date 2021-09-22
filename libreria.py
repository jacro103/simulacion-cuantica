import math

def cplxsum(a,b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return ( real, imag )

if __name__ == '__main__':
    print(cplxsum((3,5),(-2.6,6.8))) # (3 + 5i) + (-2.6 + 6.8i) = (0.4 + 11.8i)


def cplxrest(c,d):
    real = c[0] - d[0]
    imag = c[1] - d[1]
    return (real, imag)

if __name__ == '__main__':
    print(cplxrest((7,9),(-4,8))) # (7 + 9i) - (-4 + 8i) = (11 - 1i)


def cplxmult(a,b):
    real = (a[0] * b[0])-(a[1] * b[1])
    imag = (a[0] * b[1])+(a[1] * b[0])
    return (real, imag)

if __name__ == '__main__':
    print(cplxmult((2,5),(-3,4))) # (2 + 5i) + (-3 + 4i) = (-26 - 7i)

def cplxdiv(a,b):
    real = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    imag = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    return (real, imag)

if __name__ == '__main__':
    print(cplxdiv((9,3),(-7,4))) # (9 + 3i) / (-7 + 4i) = (-0,7846153846 - 0,8769230769i)

def cplxmol(a,b):
    real = (a * a + b * b)**0.5

    return (real)

if __name__ == '__main__':
    print(cplxmol(3, 4)) # (3 + 4i) = 5

def cplxcon(a):
    real = a[0]
    imag = -a[1]
    return (real, imag)

if __name__ == '__main__':
    print(cplxcon([6,3])) # (6 + 3i) = (6 - 3i)


def cplxpol(a):
    real = (a[0] * a[0] + a[1] * a[1])**0.5
    imag = math.atan(a[1]/a[0])
    return (real, imag)

if __name__ == '__main__':
    print(cplxpol([4, 7])) # (4 + 7i) = (8.06225774829855 + 1.0516502125483738i)



if __name__ == '__main__':
    print(cplxsum((3, 5), (-2.6, 6.8)))  # (3 + 5i) + (-2.6 + 6.8i) = (0.4 + 11.8i)
    a = complex("3+5j")
    b = complex("-2.6+6.8j")
    print(a + b)
    v = [(3, 5), (2, 5), (-3.4, 5)]

