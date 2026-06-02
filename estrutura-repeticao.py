nome = input("Nome: ")
continuar = "s"

while continuar.lower() == "s":
    materia = input("\nMateria: ")
    soma_notas = 0
    
    for n in range(1, 4 + 1):
        while True:
            nota = float(input(f"Digite a nota {n}: "))
            
            if 0 <= nota <= 10:
                break
            else:
                print("Nota invalida! Digite um numero de 0 a 10")
        soma_notas += nota

    frequencia = int(input("Frequencia: "))
    media = soma_notas / 4

    print(f"Ola {nome}, para passar nas disciplinas o minimo esperado e voce ter uma media acima de 6 e uma frequencia acima de 50")
    print(f"Sua media em {materia} e: {media}")
    print(f"Sua frequencia em {materia} e: {frequencia}")

    if media >= 6 and frequencia >= 50:
        print("Situacao: Aprovado")
    else:
        print("Situacao: Reprovado")

    continuar = input("Deseja cadastrar outra disciplina?(s/n): ")

print(f"\nAte logo, {nome}!")
