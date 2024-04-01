'''import math
num = int(input("digite um numero: "))
if num > 0:
    raiz = math.sqrt(num)
    print("a raiz quadradada é: ", raiz)
else:
    print("numero invalido")'''
pesos = []
for x in range(5):
    peso = float(input(f"Digite seu peso {x + 1}: "))
    pesos.append(peso)
    
maior_peso = max(pesos)
menor_peso = min(pesos)

print(f"O maior peso lido foi: {maior_peso} kg")
print(f"O menor peso lido foi: {menor_peso} kg")
