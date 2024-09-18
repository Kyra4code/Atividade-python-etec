def main():
    salario = float(input("Insira seu salário: "))
    desconto = float(input("Insira seu desconto(%): "))
    calcdes = (desconto / 100) * salario
    salariof = salario -calcdes

    print(f"Seu salario no final é {salariof}")
    print(f"Seu desconto é de {calcdes}")

main()