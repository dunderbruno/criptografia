import string


def converte_letra_em_numero(letra):
    posicao = 0
    if letra == ' ':
        return 99
    else:
        for i in string.ascii_lowercase:
            posicao += 1
            if i == letra:
                return posicao


def enc(texto, chave):
    texto_cifrado = ''
    for caractere in texto:
        posicao_atual = converte_letra_em_numero(caractere)
        if posicao_atual == 99:
            texto_cifrado += ' '
        else:
            posicao_nova = (posicao_atual + chave) % 26
            texto_cifrado += string.ascii_lowercase[posicao_nova-1]
    return(texto_cifrado)


def dec(texto, chave):
    texto_plano = ''
    for caractere in texto:
        posicao_atual = converte_letra_em_numero(caractere)
        if posicao_atual == 99:
            texto_plano += ' '
        else:
            posicao_nova = (posicao_atual - chave) % 26
            texto_plano += string.ascii_lowercase[posicao_nova-1]
    return(texto_plano)


mensagem_original = input("Digite sua mensagem: ")

mensagem_encriptada = enc(mensagem_original, 3)
print(f"Mensagem Encriptada: {mensagem_encriptada}")

mensagem_decodificada = dec(mensagem_encriptada, 3)
print(f"Mensagem Decodificada: {mensagem_decodificada}")
