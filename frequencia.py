import string

frequencias = {}

mensagem = input("Digite o texto aqui: ")


def contar(letra, texto):
    resultado = 0
    for caractere in texto:
        if caractere == letra:
            resultado += 1
    return resultado


for i in string.ascii_lowercase:
    frequencias[i] = contar(i, mensagem)/len(mensagem.replace(" ", ''))

print(frequencias)
