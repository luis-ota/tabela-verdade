import ttg
from tabulate import tabulate

# Função principal para a calculadora lógica
def tabela():
    print('\n\n')
    print('                 === Calculadora Logica ===')

    # Exemplos de operações lógicas e suas descrições
    exemplos = [["Operadores Lógicos", "Exemplos de Operações"],
                ["Negação: 'not', '-', '~'", "~p, not p, -p"],
                ["Disjunção: 'or'", "p or q"], ["NOR: 'nor'", "p nor q"],
                ["Disjunção Exclusiva: 'xor', '!='", "p xor q, p != q"],
                ["Conjunção: 'and'", "p and q"], ["NAND: 'nand'", "p nand q"],
                ["Implicação : '=>', 'implies'", "p => q, p implies q"],
                ["Bicondicional: '='", "p = q"]]

    # Exibe a tabela de exemplos formatada
    print(tabulate(exemplos, headers="firstrow", tablefmt="fancy_grid"))

    # Loop principal para continuar pedindo 
    # fórmulas até que o usuário escolha encerrar
    while True:
        # Solicita ao usuário que digite uma fórmula
        operacao = input("\nDigite a fórmula: ")
        
        # Inicializa listas e dicionário para armazenar 
        # variáveis e contagem de operações
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

        # Adiciona espaços em branco ao redor dos operadores
        # para garantir uma divisão adequada
        operacao = operacao.replace('(', ' ( ').replace(')', ' ) ')


        for i in operacao.split():
            # Itera sobre os elementos da fórmula divididos por espaços
            if len(i) == 1 and i.isalpha():
                letras.append(i.lower())

            # Verifica se é uma operação mais complexa e adiciona a última letra à lista
            # no caso quando tem algo do tipo: '-p', '~q', '(p', 'q)', '(-p'
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
                elif i[0] in ['-', '~'] or i.lower() == 'not':
                    operacoes['not'] += 1
                elif i == '=>' or i == 'implies':
                    operacoes['implicação'] += 1
                elif i == '!=':
                    operacoes['xor'] += 1

                else:
                    # Contagem para operadores específicos
                    for op in operacoes:
                        operacoes[op] += i.lower().count(op)

        # Remove duplicatas e ordena as variáveis
        letras = sorted(set(letras))

        try:
            # Gera a tabela verdade usando a biblioteca ttg
            table = str(ttg.Truths(letras, [operacao.lower()])).replace(
                '1', 'V').replace('0', 'F')
        except:
            # Trata exceção se a fórmula for inválida
            print('Você digitou uma fórmula inválida, tente novamente.\n')
            continuar = input('\nDeseja continuar? (S/N): ')
            if continuar.lower() != 's':
                break
            continue

        # Exibe resultados
        print('\nVariáveis: ', letras)
        print('\nOperações:')
        for op, count in operacoes.items():
            print(f'{op}: {count}')
        print('\nTabela Verdade:')
        print(table)
        
        # Pergunta ao usuário se deseja continuar ou encerrar o programa
        continuar = input('\nDeseja continuar? (S/N): ')
        if continuar.lower() != 's':
            break

# Executa a função tabela() se este script for executado como o programa principal
if __name__ == '__main__':
    tabela()