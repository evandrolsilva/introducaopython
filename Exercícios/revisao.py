#aula1

print("olá mundo!") #sempre inserir quando foi imprimir algo.
input("digite sua idade") #serve para o usuario inputar alguma informção que não é lógica

anonascimento = int(input("digite o ano de nascimento"))
idade = 2022 - anonascimento
print(idade)

print(f"{idade}anos") #f(formatar), na aspa fica a variavél.


anonascimento = int(input("digite o ano de nascimento"))
aniversario = int(input(" Voce ja fez aniversario esse ano? Digite 1 para sim, 2 para não"))
if aniversario==1:
    idade= 2022 - anonascimento
else:
    idade= (2022 - anonascimento) - 1
print(idade)

#operaçõesmatemáticas

x = 10
y = 3

print(x+y) #adição
print(int(x)+int(y)) #int(números inteiros) float(números decimais)
print(x-y) #subtração
print(x*y) #multiplicação
print(x/y) #divisão
print(x**y) #exponeciação
print(x%y) #modulo

print(x>y)
print(x<y)

lista= [2015, 2019, 2023]
saida = []
for i in lista:
     a = i + 2022
     saida.append(a)
print(saida)

