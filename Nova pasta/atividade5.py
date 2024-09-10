def main():
    salario = float(input("Insira seu salário: "))
    desconto = float(input("Insira seu desconto: "))
    calcdes = (desconto / 100) * salario - salario

    print(f"Seu desconto é de {calcdes}") 

main()