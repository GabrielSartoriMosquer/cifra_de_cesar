# VARIÁVEIS GLOBAIS
minusculas = 'abcdefghijklmnopqrstuvwxyz'  # Alfabeto minúsculo
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Alfabeto maiúsculo

# FUNÇÃO PARA DECIFRAR UMA FRASE
def decifrar():
    frase_final = ''  # Inicializa a frase decifrada como vazia
    chave = int(input('Insira a chave que foi utilizada: '))  # Usuário insere o número da chave (quantas letras foram "deslocadas")
    frase = input('Digite a frase cifrada: ')  # Frase que será decifrada

    # Função interna para decifrar um único caractere
    def decifrar_caractere(caractere, sequencia, chave):
        posicao_atual = sequencia.index(caractere)  # Encontra a posição do caractere no alfabeto
        posicao_decifrada = (posicao_atual - chave) % 26  # Subtrai a chave e aplica o operador % para garantir que a posição volte ao início do alfabeto se necessário
        return sequencia[posicao_decifrada]  # Retorna o caractere decifrado

    # Percorre cada caractere da frase
    for caractere in frase:
        if caractere in minusculas:  # Se for letra minúscula
            caractere_original = decifrar_caractere(caractere, minusculas, chave)
        elif caractere in maiusculas:  # Se for letra maiúscula
            caractere_original = decifrar_caractere(caractere, maiusculas, chave)
        else:
            caractere_original = caractere  # Se não for letra (ex: espaço, número, pontuação), mantém como está

        frase_final += caractere_original  # Adiciona o caractere decifrado à nova frase

    # Mostra o resultado final
    print(f'A frase original é: "{frase_final}".\n')

# FUNÇÃO PARA CIFRAR UMA FRASE
def cifrar():
    frase_final = ''  # Inicializa a frase cifrada como vazia
    chave = int(input('Insira a chave que será utilizada: '))  # Usuário insere a chave de cifragem
    frase = input('Digite a frase: ')  # Frase a ser cifrada

    # Função interna para cifrar um único caractere
    def cifrar_caractere(caractere, sequencia, chave):
        posicao_atual = sequencia.index(caractere)  # Encontra a posição da letra
        posicao_cifrada = (posicao_atual + chave) % 26  # Soma a chave e ajusta com % para manter no intervalo do alfabeto
        return sequencia[posicao_cifrada]  # Retorna o caractere cifrado

    # Percorre cada caractere da frase
    for caractere in frase:
        if caractere in minusculas:
            caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
        elif caractere in maiusculas:
            caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
        else:
            caractere_cifra = caractere  # Mantém espaços e outros caracteres

        frase_final += caractere_cifra  # Adiciona à frase cifrada

    # Mostra a frase cifrada
    print(f'A frase cifrada fica: "{frase_final}".\n')

# LAÇO PRINCIPAL DO PROGRAMA
while True:
    objetivo = input('Você deseja cifrar ou decifrar uma frase? Digite s para sair. ').lower().strip()
    
    if objetivo == 's':  # Se o usuário quiser sair
        print('Até logo!')
        break
    
    if objetivo == 'decifrar':
        decifrar()
    elif objetivo == 'cifrar':
        cifrar()
    else:
        print('Resposta inválida. Digite "cifrar" ou "decifrar"\n')
