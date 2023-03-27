#Algoritimo em Python que calcula valor presente, valor futuro e o pagamento

import math

print("Digite abaixo (FV) para valor futuro ou (PV) para valor presente")
x = input("O que você deseja quer calcular?  ")
r = int(input("Digite a taxa de juros: "))
n = int(input("Digite o número de períodos: "))

if(x == "pv"): 
    fv = float(input("Digite seu valor futuro: "))
    pv = fv/(1+r/100)**n
    print ('O valor presente é R$ ', pv)
elif(x == "fv"):
    pv = float(input("Digite seu valor futuro: "))
    fv = pv/(1+r/100)**n
    print ('O valor futuro será de R$', fv)
else:
    print("inválido")
