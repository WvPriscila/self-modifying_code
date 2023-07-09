def Copiar(nome_arquivo):
    lista_encontrada = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if '[' in linha and ']' in linha:
                lista_str = linha[linha.index('[')+1:linha.index(']')]
                lista = [valor.strip() for valor in lista_str.split(',')]
                lista_encontrada.extend(lista)
                arquivo.close()
    return lista_encontrada


def Colocar(nome_arquivo, lista):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for i, linha in enumerate(linhas):
        if 'U =' in linha:
            elementos = ', '.join(str(item) for item in lista)  # Formata os elementos da lista como uma string
            linhas[i] = f'U = [{elementos}]\n'  # Atualiza a linha para definir a variável U com os elementos formatados
            break

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)


def buscar(nome_arquivo, palavra):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if palavra in linha and palavra == "oii":
                    print("oii")
                    arquivo.close()
                    Cop = Copiar("E.py")
                    Colocar("A.py", Cop)

        return None
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except:
        print("Ocorreu um erro ao ler o arquivo.")



