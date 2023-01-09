from time import sleep
lista = list()
exam = list()
while True:
    nome = str(input('  Matéria(Se o nome da mesma for grande, abrevie): '))
    while True:
        nota_prova = float(input(' Nota da prova: '))
        if nota_prova <= 10:
            break
        print('  404... Apenas de 0 a 10!')
    while True:
        pim = float(input('  Nota PIM: '))
        if pim <= 10:
            break
        print('  404... Apenas de 0 a 10!')
    while True:
        ava = float(input('   Nota AVA: '))
        if ava <= 10:
            break
        print('  404... Apenas de 0 a 10!')
    média = (((nota_prova * 7) + (pim * 2) + (ava)) / 10)
    if média < 5.7:
        aprov = (5 * 2) - média
        exam.append([nome, média, aprov])
    if média > 5.7:
        lista.append([nome, [nota_prova, pim, ava], média])
    while True:
        resp = str(input('    Deseja continuar?  [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('  404... Apenas S ou N')
    if resp in 'N':
        break
if len(lista) > 0:
    print()
    print('#' * 30)
    print(f'{"APROVADOS":^30}')
    print('¬' * 30)
    print(f'{"Nº":<4}{"Nome":<15}{"Média":>8}')
    for i, alu in enumerate(lista):
        print(f'{i:<4}{alu[0]:<15}{alu[2]:>8.2f}')
    print('_' * 30)
print()
if len(exam) > 0:
    print('#' * 70)
    print(f'{"DE EXAME":^70}')
    print('¬' * 70)
    print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}{"Nota necessária para aprovação":>45}')
    for i, alu in enumerate(exam):
        print(f'{i:<4}{alu[0]:<10}{alu[1]:>8.2f}{alu[2]:>30.2f}')
    print('_' * 70)
    print()
while True:
    resp = str(input('Digite [N] para parar a visualização da tabela: ')).upper().strip()[0]
    if resp in 'N':
        break
print('Fechando Programa..........')
sleep(4)
