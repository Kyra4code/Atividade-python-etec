def main():
    try:
        print("INSIRA VALORES INFINITAMENTE E QUANDO DIZER CHEGA ESSES NUMEROS SERAO CALCULADOS A MEDIA DELES:")

        while True:
            valor1 = [float(input("Insira o valor: "))]

            if valor1 == "chega":
                break
            elif valor1 != "chega":
                continue


        calc = sum(valor1) / len(valor1)
        print(f"A média desses valores e {calc}")

    except:
        calc = sum(valor1) / len(valor1) #SUM() soma e LEN() soma o numero de elementos inseridos em uma variável
        print(f"A média desses valores e {calc}")



main()