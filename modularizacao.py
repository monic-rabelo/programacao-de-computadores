def cadastrar_materia():
    materias_validas = [
        "matematica",
        "historia",
        "fisica",
        "educação fisica",
        "educacao fisica",
    ]
    while True:
        materia = input("\nMatéria: ")
        materia_ajustada = (
            materia.lower()
            .replace("á", "a")
            .replace("ç", "c")
            .replace("ã", "a")
            .replace("í", "i")
            .replace("ó", "o")
        )

        if materia_ajustada in materias_validas:
            return materia
        print(
            "Matéria inválida! Nesta escola só existem: Matemática, História, Física e Educação Fisica."
        )


def calcular_nota():
    soma_notas = 0
    for n in range(1, 5):
        while True:
            nota = float(input(f"Digite a nota {n}: "))
            if 0 <= nota <= 10:
                soma_notas += nota
                break
            print("Nota inválida! Digite um número de 0 a 10")
    return soma_notas / 4


def calcular_frequencia():
    frequencia = int(input("Frequência: "))
    return frequencia


def gerar_relatorio(nome, disciplinas, notas, faltas):
    print("\nDados cadastrados:")
    for i in range(len(disciplinas)):
        print(f"\nDisciplina: {disciplinas[i]}")
        print(f"Média: {notas[i]}")
        print(f"Frequência: {faltas[i]}")

        if notas[i] >= 6 and faltas[i] >= 50:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")

    print(f"\nAté logo, {nome}!")


nome = input("Nome: ")
disciplinas = []
notas = []
faltas = []
continuar = "s"

while continuar.lower() == "s":
    materia = cadastrar_materia()
    media = calcular_nota()
    frequencia = calcular_frequencia()

    disciplinas.append(materia)
    notas.append(media)
    faltas.append(frequencia)

    print(
        f"Olá {nome}, para passar o mínimo esperado é média acima de 6 e frequência acima de 50"
    )
    print(f"Sua média em {materia} é: {media}")
    print(f"Sua frequência em {materia} é: {frequencia}")

    if media >= 6 and frequencia >= 50:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

    continuar = input("\nDeseja cadastrar outra disciplina?(s/n): ")

gerar_relatorio(nome, disciplinas, notas, faltas)
