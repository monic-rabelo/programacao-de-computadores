nome = input("Nome: ")
materia = input("Matéria: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

frequencia = int(input("Frequência: "))
media = (nota1+nota2+nota3+nota4)/4

print(f"Olá {nome}, para passar nas disciplinas o mínimo esperado e você ter uma média acima de 6 e uma frequência acima de 50")
print(f"Sua média em {materia} é: {media}")
print(f"Sua frequência em {materia} é: {frequencia}")

if media >= 6 and frequencia >= 50:
  print('Situação: Aprovado')

else:
  print('Situação: Reprovado')
