salario = int(input('Qual é o Seu salário atual?'))
aumento = int(input('Qual a porcentagem de aumento?'))
novo = int(salario + (salario * aumento / 100))
print("Seu novo salário será de: R${}".format(novo))
