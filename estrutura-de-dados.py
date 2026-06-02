nome = input("Nome: ")

materias_validas = ["matematica", "historia", "fisica", "educação fisica", "educacao fisica"]

disciplinas = []
notas = []
faltas = []

continuar = "s"

while continuar.lower() == "s":
    while True:
        materia = input("\nMatéria: ")

        materia_ajustada = materia.lower().replace("á", "a").replace("ç", "c").replace("ã", "a").replace("í", "i").replace("ó", "o")
           
        if materia_ajustada in materias_validas:
            break
        else:
            print("Matéria inválida! Nesta escola só existem: Matemática, História, Física e Educação Fisica.")
    
    soma_notas = 0
    for n in range(1, 5):
        while True:
            nota = float(input(f'Digite a nota {n}: '))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida! Digite um número de 0 a 10")

        soma_notas += nota

    frequencia = int(input("Frequência: "))

    media = soma_notas / 4

    disciplinas.append(materia)
    notas.append(media)
    faltas.append(frequencia)

    print(f"Olá {nome}, para passar nas disciplinas o mínimo esperado e você ter uma média acima de 6 e uma frequência acima de 50")
    print(f"Sua média em {materia} é: {media}")
    print(f"Sua frequência em {materia} é: {frequencia}")

    if media >= 6 and frequencia >= 50:
        print('Situação: Aprovado')
    else:
        print('Situação: Reprovado')
      
    continuar = input("Deseja cadastrar outra disciplina?(s/n): ")

print("Dados cadastrados:")
for i in range(len(disciplinas)):
    print(f"\nDisciplina: {disciplinas[i]}")
    print(f"Média: {notas[i]}")
    print(f"Frequência: {faltas[i]}")
      
    if notas[i] >= 6 and faltas[i] >= 50:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

print(f"\nAté logo, {nome}!")
