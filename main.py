import os
from translate import Translator  # biblioteca do tradutor

# opcoes validas de idiomas
opcoes =  ['es','pt','en','it']

# para limpar o console
def clear(): return os.system('cls')

#codigo
print('Bem vindo ao tradutor')
print('Pressione enter pra continuar')
input()
clear()

print('Temos suporte para portuguuês, espanhol, inglês e italiano')
print('Pressione enter pra continuar')
input()
clear()

idiomaInicial = input(
    'Por favor digite idioma do texto que quer traduzir: ').lower()
clear()

while idiomaInicial == '':
    print("Idioma não inserido")
    idiomaInicial = input(
        'Por favor digite idioma do texto que quer traduzir: ').lower()
    clear()

while idiomaInicial not in opcoes:
    print("Idioma não suportado")
    idiomaInicial = input(
        'Por favor digite idioma do texto que quer traduzir: ').lower()
    clear()

textoParaTraduzir = input('Por favor digite o texto que deseja traduzir: ')
clear()

while textoParaTraduzir == '':
    print("Texto não inserido")
    textoParaTraduzir = input(
        'Por favor digite o texto que deseja traduzir: ')
    clear()

idiomaFinal = input(
    'Por favor selecione o idioma para que deseja traduzir: ').lower()


while idiomaFinal == '':
    print("Idioma não inserido")
    idiomaFinal = input(
        'Por favor selecione o idioma para que deseja traduzir: ').lower()
    clear()

while idiomaFinal not in opcoes:
    print("Idioma não suportado")
    idiomaFinal = input(
        'Por favor selecione o idioma para que deseja traduzir: ').lower()
    clear()

traduzido = Translator(from_lang=idiomaInicial, to_lang=idiomaFinal).translate(textoParaTraduzir)

with open('./textotraduzido.txt', 'w') as a: #cria o arquivo e escreve o texto traduzido
    a.write(traduzido)
    if idiomaFinal == opcoes[0]:
        print('Texto traduzido com sucesso para espanhol')
    elif idiomaFinal == opcoes[1]:
        print('Texto traduzido com sucesso para português')
    elif idiomaFinal == opcoes[2]:
        print('Texto traduzido com sucesso para inglês')
    else:
        print('Texto traduzido com sucesso para italiano')
    print('Pressione enter pra vizualizar')
    input()
    clear()

with open('./textotraduzido.txt') as b: #le o arquivo e mostra o texto traduzido
    textotraduzido = b.read()
    print(textotraduzido)
    print('Pressione enter pra finalizar')
    input()
    clear()

with open('./textotraduzido.txt', 'w') as reset: #limpa o arquivo
    reset.close()
