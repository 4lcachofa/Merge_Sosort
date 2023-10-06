#Función para dividir el arreglo
def mergesort(arr):
    #Caso base
    if len(arr)<=1:
        return arr
    #Dividir
    #Obtener la mitad del arreglo
    mitad =len(arr)//2
    #Divide el arreglo en mitades uwu
    izq=arr[:mitad]
    der=arr[mitad:]
    #Conquistar 
    #Llamar a la función recursiva 
    izq=mergesort(izq)
    der=mergesort(der)
    #Mezclar xd
    return merge(izq, der)

def merge(izq,der):
    ordenado =[]
    i_izq, i_der=0,0
    #Ciclo para comparar todos los elementardos, pa
    while i_izq<len(izq) and i_der<len(der):
        if izq[i_izq]<der[i_der]:
            ordenado.append(izq[i_izq])
            i_izq +=1
        else:
            ordenado.append(der[i_der])
            i_der +=1
    #Agregar todos los valores restantes
    ordenado.extend(izq[i_izq:])
    ordenado.extend(der[i_der:])
    return ordenado

if __name__=="__main__":
    arr=[2,7,4,1,8,5,6,3,9]
    print('Arreglo sin ordenar', arr)
    ordenado=mergesort(arr)
    print("Arreglo ordenado ", ordenado)
