qtdInsulina =int(input("Quanto você toma de insulina por dia: "))

fatorSensi = 1500 / qtdInsulina
teste = int(input("Quantos testes foram feitos: "))

valorTeste: int

vet: [int] = [0 for valorTeste in range(teste)]

for i in range (0, teste):
    valorTeste = vet[i] = int(input("Valor da glicemia: "))
    insulina = (valorTeste - 120) / fatorSensi
    if valorTeste > 120:
        print(f"Tomar {insulina} de insulina")
    elif valorTeste < 80:
        print("Você precisa ingerir açucar!")
    else:
        print("")

soma = 0
for i in range(0, teste):
    soma = soma + vet[i]

media = soma / teste

if media >= 80 and media < 120:
    print("Voce esta com a glicose controlada")
elif media > 120:
    print("Voce precisa cuidar da sua glicose melhor!")
else:
    print("Voce precisa cuidar da sua hipoglicemia")