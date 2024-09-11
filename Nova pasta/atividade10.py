def main():
    try:
        print("INSIRA VALORES INFINITAMENTE E QUANDO DIZER CHEGA ESSES NUMEROS SERAO CALCULADOS A MEDIA DELES:")

        while True:
            valor1 = [float(input("Insira o valor: "))]

            if valor1.lower() == "chega":
                break


        calc = sum(valor1) / len(valor1)
        print(f"A média desses valores e {calc}")
    except:
        print("ERROR!")

main()