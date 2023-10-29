def load_data(nome_do_arquivo):
    try:
        return open(nome_do_arquivo, 'r').read()
    
    except IOError as e:
        print(f"Erro: {e}")

def create_file(nome_do_arquivo, messangem):
    try:
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(messangem)

    except IOError as e:
        print(f'Error writing: {e}')