import os
from translate import Translator  # biblioteca do tradutor

opcao1 = 'es'
opcao2 = 'pt'
opcao3 = 'en'

# para limpar o console


def clear(): return os.system('cls')


print('Bem vindo ao tradutor')
print('Pressione enter pra continuar')
input()
clear()

print('Temos suporte para ingles(en), espanhol(es) e portugues')
print('Pressione enter pra continuar')
input()
clear()

idiomaInicial = input(
    'Por favor digite idioma do texto que quer traduzir: ').lower()
clear()

while idiomaInicial == '':

    print("Idioma nao inserido")
    idiomaInicial = input(
        'Por favor digite idioma do texto que quer traduzir: ').lower()
    clear()

while idiomaInicial not in (opcao1, opcao2, opcao3):
    print("Idioma nao suportado")
    idiomaInicial = input(
        'Por favor digite idioma do texto que quer traduzir: ').lower()
    clear()

textoParaTraduzir = input('Por favor digite o texto que deseja traduzir: ')
clear()

while textoParaTraduzir == '':
    print("Texto nao inserido")
    textoParaTraduzir = input(
        'Por favor digite o texto que deseja traduzir: ')
    clear()

selecionarIdioma = input(
    'Por favor selecione o idioma para que deseja traduzir: ').lower()

texto = textoParaTraduzir

while selecionarIdioma == '':
    print("Idioma nao inserido")
    selecionarIdioma = input(
        'Por favor selecione o idioma para que deseja traduzir: ').lower()
    clear()

while selecionarIdioma != opcao1 and selecionarIdioma != opcao2 and selecionarIdioma != opcao3:
    print("Idioma nao suportado")
    selecionarIdioma = input(
        'Por favor selecione o idioma para que deseja traduzir: ').lower()
    clear()

idioma = selecionarIdioma
translator = Translator(to_lang=idioma, from_lang=idiomaInicial)

with open('./textotraduzido.txt', 'w') as a:
    traduzido = translator.translate(texto).capitalize()
    a.write(traduzido)
    if idioma == 'es':
        print('Texto traduzido com sucesso para espanhol')
    elif idioma == 'pt':
        print('Texto traduzido com sucesso para portugues')
    elif idioma == 'en':
        print('Texto traduzido com sucesso para ingles')
    print('Pressione enter pra vizualizar')
    input()
    clear()

with open('./textotraduzido.txt') as b:
    textotraduzido = b.read()
    print(textotraduzido)
    print('Pressione enter pra finalizar')
    input()
    clear()

with open('./textotraduzido.txt', 'w') as done:
    done.close()
