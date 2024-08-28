def main():
    try:
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade:")
        peso = input("Digite seu peso: ")
        cidade = input("Digite sua cidade: ")

        print(f'Olá, Meu nome é {nome}, eu tenho {idade} anos, meu peso é {peso} e moro em {cidade}')
    except:
        print("Error, tente novamente")

main()