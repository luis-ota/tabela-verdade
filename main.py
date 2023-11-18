import ttg
from tabulate import tabulate


def tabela():
    print('\n\n')
    print('                 === Calculadora Logica ===')

    exemplos = [["Operadores Lógicos", "Exemplos de Operações"],
                ["Negação: 'not', '-', '~'", "~p, not p, -p"],
                ["Disjunção: 'or'", "p or q"], ["NOR: 'nor'", "p nor q"],
                ["Disjunção Exclusiva: 'xor', '!='", "p xor q, p != q"],
                ["Conjunção: 'and'", "p and q"], ["NAND: 'nand'", "p nand q"],
                ["Implicação : '=>', 'implies'", "p => q, p implies q"],
                ["Bicondicional: '='", "p = q"]]

    print(tabulate(exemplos, headers="firstrow", tablefmt="fancy_grid"))

    while True:
        operacao = input("\nDigite a fórmula: ")

        letras = []
        operacoes = {
            'and': 0,
            'or': 0,
            'not': 0,
            'nor': 0,
            'xor': 0,
            'nand': 0,
            'implicação': 0,
            'bicondicional': 0
        }

        # Adiciona espaços em branco ao redor dos operadores para garantir uma divisão adequada
        operacao = operacao.replace('(', ' ( ').replace(')', ' ) ')

        for i in operacao.split():
            if len(i) == 1 and i.isalpha():
                letras.append(i.lower())
            elif i == '=':
                operacoes['bicondicional'] += 1

            elif len(i) > 1:
                if '(' in i and i.split('(')[-1][-1].isalpha():
                    letras.append(i.split('(')[-1][-1].lower())
                elif ')' in i and i.split(')')[0][-1].isalpha():
                    letras.append(i.split(')')[0][-1].lower())
                elif i[0] in ['-', '~'] and i[-1].isalpha():
                    letras.append(i[-1].lower())

                if i.lower() == 'xor':
                    operacoes['xor'] += 1
                elif i.lower() == 'nand':
                    operacoes['nand'] += 1
                elif i.lower() == 'nor':
                    operacoes['nor'] += 1
                elif i[0] in ['-', '~']:
                    operacoes['not'] += 1
                elif i == '=>':
                    operacoes['implicação'] += 1
                elif i == '!=':
                    operacoes['xor'] += 1

                else:
                    for op in operacoes:
                        operacoes[op] += i.lower().count(op)

        letras = sorted(set(letras))

        try:
            table = str(ttg.Truths(letras,
                                   [operacao])).replace('1',
                                                        'V').replace('0', 'F')
        except:
            print('Você digitou uma fórmula inválida, tente novamente.\n')
            continuar = input('\nDeseja continuar? (S/N): ')
            if continuar.lower() != 's':
                break
            continue

        print('\nVariáveis: ', letras)
        print('\nOperações:')
        for op, count in operacoes.items():
            print(f'{op}: {count}')
        print('\nTabela Verdade:')
        print(table)

        continuar = input('\nDeseja continuar? (S/N): ')
        if continuar.lower() != 's':
            break


if __name__ == '__main__':
    tabela()
