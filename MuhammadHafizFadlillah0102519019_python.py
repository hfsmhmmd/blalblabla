m1=[[6,8],[10,4]]
m2=[[4,2],[5,2]]
def plus(a,b):
    hasil=[]
    for x in range(0, len(m1)):
        c=[]
        for y in range(0, len(m2)):
            temp=(a[x][y] + b[x][y])
            c.append(temp)
        hasil.append(c)
    return print("Hasil Pertambahan A + B =", *hasil, sep='\n')
def multiple (a,b):
    hasil = []
    for x in range(0, len(a)):
        row = []
        for y in range(0, len(a[0])):
            total = 0
            for z in range(0, len(a)):
                total = total + (a[x][z] * b[z][y])
            row.append(total)
        hasil.append(row)
    return print("Hasil Perkalian A x B =", *hasil, sep='\n')

def minus(a,b):
    hasil=[]
    for x in range(0, len(a)):
        c=[]
        for y in range(0, len(b)):
            temp = (a[x][y] - b[x][y])
            c.append(temp)
        hasil.append(c)
    return print("Hasil Pengurangan A - B =", *hasil, sep='\n')

print("A & B : ")
print("Matrix A", *m1,sep='\n')
print("Matrix B", *m2,sep='\n')
plus(m1, m2)
multiple(m1,m2)
minus(m1,m2)