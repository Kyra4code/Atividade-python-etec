def main():
    peso = float(input("insira seu peso: "))
    altura = float(input("Insira sua altura: "))

    IMC = peso + (altura * altura)

    if IMC <= 16.9:
        print("Você muito abaixo do peso")
    elif IMC >= 17 and IMC <= 18.9:
        print("Você abaixo do peso")
    elif IMC >= 19 and IMC <= 26.9:
        print("Você tem o peso normal")
    elif IMC >= 27 and IMC <= 31.9:
        print("você acima do peso")
    elif IMC >= 32:
        print("Você é obeso")

main()