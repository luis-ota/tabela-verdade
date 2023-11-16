# Calculadora Lógica

Bem-vindo à Calculadora Lógica! Este é um programa simples em Python que permite realizar operações lógicas e gerar tabelas verdade para fórmulas lógicas.

## Como Usar

1. Execute o programa `main.py`.
2. Digite a fórmula lógica desejada quando solicitado.
3. O programa exibirá as variáveis, a contagem de operações e a tabela verdade correspondente.
4. Você pode escolher continuar inserindo novas fórmulas ou encerrar o programa.

## Exemplos de Fórmulas Suportadas

- Negação: 'not', '-', '~' (Ex: `~p`, `not p`, `-p`)
- Disjunção: 'or' (Ex: `p or q`)
- NOR: 'nor' (Ex: `p nor q`)
- Disjunção Exclusiva: 'xor', '!=' (Ex: `p xor q`, `p != q`)
- Conjunção: 'and' (Ex: `p and q`)
- NAND: 'nand' (Ex: `p nand q`)
- Implicação: '=>' ou 'implies' (Ex: `p => q`, `p implies q`)
- Bicondicional: '=' (Ex: `p = q`)

## Dependências

- [truth-table-generator]([https://github.com/chrisvoncsefalvay/ttg](https://pypi.org/project/truth-table-generator/)) - Biblioteca para gerar tabelas verdade.
- tabulate - Biblioteca para formatar a tabela de exemplos.

