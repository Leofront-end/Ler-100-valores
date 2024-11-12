valores = []
divisivelPorTres = 0
for x in range(1,101):
    numero = input("Digite um numero ou ' ' para sair: ")
    if numero == ' ':
        print("Sair")
        break
    else:
        numero = int(numero)
        if numero % 3 == 0:
            divisivelPorTres += numero
        valores.append(numero)
print(valores)
print(f'A somatoria dos numeros divisiveis por 3 resultou em {divisivelPorTres}')