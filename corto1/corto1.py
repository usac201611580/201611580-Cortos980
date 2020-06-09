import time #Para generar pausa
# Definiciones utilizadas
def collatz(num):
    secuencia=[num]
    while(num>1):
        if(num%2==0):   #En caso sea un numero par
            num=num//2  #Realiza la operacion en caso de ser par
            secuencia.append(num)   #Agrega el valor a la lista
        else:   #En caso sea numero impar
            num=3*num+1 #Realiza la operaion en caso de ser impar
            secuencia.append(num)   #Agrega el valor a la lista
    return secuencia

# Codigo principal
# 580 ultimos 3 digitos del carne
print("Generando archivo")
archivo =open('collatz.txt','w')   #Abre el archivo para sobreescribir, en caso de no existir lo crea
for i in range(2,581,1):    #Genera la lista desde 2 hasta 580
    archivo.write((str(collatz(i))+str('\n')))
    time.sleep(1)
archivo.close() #Cierra el archivo generado
print("Secuencia de Collatz terminada.")