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
        return (matriks[0][0] * (matriks[1][1] * matriks[2][2] - matriks[1][2] * matriks[2][1]) -
                matriks[0][1] * (matriks[1][0] * matriks[2][2] - matriks[1][2] * matriks[2][0]) +
                matriks[0][2] * (matriks[1][0] * matriks[2][1] - matriks[1][1] * matriks[2][0]))
    else:
        raise ValueError("Matriks harus berukuran 2x2 atau 3x3")
    
def invers(matriks):
    det = determinan(matriks)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers karena determinannya nol")
    
    if len(matriks) == 2:
        return [[matriks[1][1] / det, -matriks[0][1] / det],
                [-matriks[1][0] / det, matriks[0][0] / det]]
    elif len(matriks) == 3:
        adjugate = [[(matriks[1][1] * matriks[2][2] - matriks[1][2] * matriks[2][1]),
                     -(matriks[0][1] * matriks[2][2] - matriks[0][2] * matriks[2][1]),
                     (matriks[0][1] * matriks[1][2] - matriks[0][2] * matriks[1][1])],
                    [-(matriks[1][0] * matriks[2][2] - matriks[1][2] * matriks[2][0]),
                     (matriks[0][0] * matriks[2][2] - matriks[0][2] * matriks[2][0]),
                     -(matriks[0][0] * matriks[1][2] - matriks[0][2] * matriks[1][0])],
                    [(matriks[1][0] * matriks[2][1] - matriks[1][1] * matriks[2][0]),
                     -(matriks[0][0] * matriks[2][1] - matriks[0][1] * matriks[2][0]),
                     (matriks[0][0] * matriks[1][1] - matriks[0][1] * matriks[1][0])]]
        return [[adjugate[i][j] / det for j in range(3)] for i in range(3)]
    else:
        raise ValueError("Matrik harus berukuran 2x2 atau 3x3")