#Creado Por Ayrton David Aranibar Castillo : estudiante Ing Sistemas
import numpy as np
#Borra la notacion cientifica
np.set_printoptions(precision=4,suppress=True)
A=int(input("cuantas variables tiene el problema?"))
B=int(input("cuantas restricciones tiene el problema?"))
X=A+B+2
Y=B+1
matriz = np.zeros((Y,X))
matriznueva=matriz.copy()
print(matriz)
def capturar_datos():
    for i in range(Y):
        for j in range(X):
            # i==0 significa mientras coloquemos valores en la funcion objetivo
            if j==0:
                matriz[i,j]=0
            elif i==0:
                if j==0:
                    matriz[i,j]=1
                elif j<=A and j>0:
                    print("ingrese la ",j," variable, funcion objetivo:")
                    matriz[i,j]=float(input())*-1
                else:
                    matriz[i,j]=0
            #Colocamos valores en las restricciones
            elif i>0 and j<X-B:
                if (j!=X-1-B):
                    print("ingrese la ",j," variable, ",i," restriccion: ")
                    matriz[i,j]=float(input())
                else:
                    print("ingrese el coeficiente de restriccion de la ",i," restriccion: ")
                    matriz[i,j]=float(input())
            #Añadimos las variables S que son 1 o 0
            elif j-(A+1)==i and i>0:
                matriz[i,j]=1
            else:
                matriz[i,j]=0
    matriz[0,0]=1
capturar_datos()
print(matriz)

def encontrar_col_pivote(matriz):
    matriz=matriz.copy()
    min=0
    pos_col=0
    for i in range(X):
        if i==0:
            min=matriz[0,i]
            pos_col=0
        elif matriz[0,i]<min:
            min=matriz[0,i]
            pos_col=i
    print("el pivote esta en la columna: ",pos_col+1)
    return pos_col
def encontrar_fil_pivote(matriz):
    matriz=matriz.copy()
    min=0
    pos_fil=0
    pos_col=0
    for i in range(X):
        if i==0:
            min=matriz[0,i]
            pos_col=0
        elif matriz[0,i]<min:
            min=matriz[0,i]
            pos_col=i
    for j in range(B+1):
        if j==1:
            min=matriz[j,A+1]/matriz[j,pos_col]
            pos_fil=j
        elif min>matriz[j,A+1]/matriz[j,pos_col] and j>0:
            min=matriz[j,A+1]/matriz[j,pos_col]
            pos_fil=j
    print("el pivote esta en la fila: ",pos_fil+1)
    return pos_fil

def pivote_a_uno(matriz):
    matriz=matriz.copy()
    columna_piv=encontrar_col_pivote(matriz)
    fila_piv=encontrar_fil_pivote(matriz)
    num=matriz[fila_piv,columna_piv]
    print("el numero pivote es el",num)
    tabla2=matriz.copy()
    for i in range(X):
        tabla2[fila_piv,i]=matriz[fila_piv,i]/num
    return(tabla2)
def transformar_a_cero(matriz):
    columna_piv=encontrar_col_pivote(matriz)
    fila_piv=encontrar_fil_pivote(matriz)
    matriznueva=matriz.copy()
    for i in range(Y):
        for j in range (X):
            if i!=fila_piv:
                matriznueva[i,j]=matriznueva[i,j]-(matriz[i,columna_piv]*matriznueva[fila_piv,j])
    return(matriznueva)
def resultado(matriz,A,B):
    matriz=matriz.copy()
    vari=A
    rest=B
    for i in range(vari):
        for j in range(rest):
            if (matriz[j+1,i+1]==1):
                print("La variable ",i+1," =",matriz[j+1,A+1])
    print("Z=",matriz[0,A+1])
    
c=1
while c==1:
    min=10000000
    for i in range(X):
        if (min>matriz[0,i]):
            min=matriz[0,i]
    if (min<0):
        min=10000000
        matriz=pivote_a_uno(matriz).copy()
        matriz=transformar_a_cero(matriz).copy()
        print(matriz)
    else:
        resultado(matriz, A, B)
        c=0
        break