# Projek Aljabar Matriks - Buat modul matriks
# Nama : Fahra Naisyla Putri Nurina
# NPM : 2515061115

def transpose(matriks):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            hasil[j][i] = matriks[i][j]
    return hasil

def determinan(matriks):
    if len(matriks) == 2:
        return matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0]
    elif len(matriks) == 3:
        a, b, c = matriks[0][0], matriks[0][1], matriks[0][2]
        d, e, f = matriks[1][0], matriks[1][1], matriks[1][2]
        g, h, i = matriks[2][0], matriks[2][1], matriks[2][2]
    
        det = (a*e*i + b*f*g + c*d*h) - (c*e*g + a*f*h + b*d*i)
        return det
    else:
        raise ValueError("Matriks harus berukuran 2x2 atau 3x3")
    
def invers(matriks):
    det = determinan(matriks)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinannya nol")
    
    if len(matriks) == 2:
        a, b = matriks[0][0], matriks[0][1]
        c, d = matriks[1][0], matriks[1][1]
        return [[d/det, -b/det], [-c/det, a/det]]
    
    elif len(matriks) == 3:
        adjugate = [[0,0,0],[0,0,0],[0,0,0]]
        a, b, c = matriks[0][0], matriks[0][1], matriks[0][2]
        d, e, f = matriks[1][0], matriks[1][1], matriks[1][2]
        g, h, i = matriks[2][0], matriks[2][1], matriks[2][2]

        adjugate[0][0] = e*i - f*h
        adjugate[0][1] = f*g - d*i
        adjugate[0][2] = d*h - e*g
        adjugate[1][0] = c*h - b*i
        adjugate[1][1] = a*i - c*g
        adjugate[1][2] = b*g - a*h
        adjugate[2][0] = b*f - c*e
        adjugate[2][1] = c*d - a*f
        adjugate[2][2] = a*e - b*d

        return [[adjugate[i][j] / det for j in range(3)] for i in range(3)]
    else:
        raise ValueError("Matrik harus berukuran 2x2 atau 3x3")
