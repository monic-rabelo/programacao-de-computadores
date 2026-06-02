nome = input("Nome: ")
materia = input("Matéria: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

media = (nota1+nota2+nota3+nota4)/4
print(f"Olá {nome}, sua média em {materia} é {media}")
