'''total = 0
for x in range(5):
    print(x)
    valor = int(input("valor:"))
    total += valor
print("fora do loop")
print(f"a media foi: {total/5}")'''


while True:
    x = int(input("valor: "))
    if x == 999:
        break
print("fora do loop")