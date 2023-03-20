boletim = list()
cadastroAluno = 's'

while cadastroAluno == 's':
    print("SIM")
    nomeAluno = str(input('Nome: '))
    Nota1 = float(input('Nota1: '))
    Nota2 = float(input('Nota2: '))
    Nota3 = float(input('Nota3: '))
    Nota4 = float(input('Nota4: '))
    media = (Nota1 + Nota2 + Nota3 + Nota4) / 4
    if media < 6:
        boletim.append([nomeAluno, [Nota1, Nota2, Nota3, Nota4], media, "REPROVADO"])
    elif media >= 6:
        boletim.append([nomeAluno, [Nota1, Nota2, Nota3, Nota4], media, "APROVADO"])
    cadastroAluno = input('Deseja cadastrar mais um aluno? (s ou n)').lower()

print('-=' * 30)
print(f'{"No.":<4}{"Nome do Aluno":<10}{"Média":>8}{"Situação":>25}')
print('- * 26')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2}{a[3]:>25}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? Digite o número da primeira coluna (999 encerra): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')

print(boletim)