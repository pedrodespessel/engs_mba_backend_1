import json # Nativo do py - trabalhar com json
import os # Nativo do py - trabalhar com diretorios

# Verifica se o arquivo já existe e carrega os dados antigos
if os.path.exists('produtos.json'):
    with open('produtos.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)  # Lê os produtos antigos e transforma em lista Python
else:
    produtos = []  # Se não existir, começa com lista vazia'

def cadastrar_produtos():
    while True:
        nome = input('insira o nome:')
        preco = float(input('insira o preço:'))
        produtos.append({
            'nome': nome,
            'preco': preco
        })
        continuar = input('deseja cadastrar mais? (s/n)')
        if continuar.lower() == 'n':
            break
        # Cria o arquivo json - propriedade 'w' é pra escrever, 'r' é pra ler
    with open('produtos.json', 'w', encoding='utf-8') as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)
        print('Banco de Dados atualizado com Sucesso!')

def listar_produtos():
    print('\n\nprodutos cadastrados:')
    for produto in produtos:
        print(f'nome: {produto['nome']}, preço: {produto['preco']}')

def exibir_menu():
    print('\n\n\n\nSistema de Cadastro de Produtos!\n')
    print('1. Cadastrar produto')
    print('2. Listar produtos')
    print('3. Sair')
    escolha = int(input('Escolha uma opção:'))
    if escolha == 1:
        cadastrar_produtos()
    elif escolha == 2:
        listar_produtos()
    else:
        print('você saiu do menu!')

exibir_menu()