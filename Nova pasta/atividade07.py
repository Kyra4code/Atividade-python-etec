def main():
    x = int(input("Insira o primeiro valor: "))
    y = int(input("Insira o segundo valor: "))
    z = int(input("Insira o terceiro valor: "))

    if x > y and x > z:
        print(f"O primeiro valor inserido {x} é maior")
    elif y > x and y > z:
        print(f"O segundo valor inserido {y} é maior")
    elif z > x and z > y:
        print(f"O terceiro numero inserido {z} é maior")
    else:
        print("Existe alguns numeros iguais")

main()