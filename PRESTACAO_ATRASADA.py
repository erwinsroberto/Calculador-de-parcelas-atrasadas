valor= float(input("Informe o valor da compra:"))
taxa= float(input("Informe o valor da taxa:"))
tempo_atraso= int(input("Informe o tempo em atraso:"))
prestacao = valor + (valor *(taxa/100)* tempo_atraso)
print("Prestação em atraso:", prestacao)
from time import sleep

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
l.reverse()
for i in l:
        sleep(3)
        print 
print ("fim do código :)")