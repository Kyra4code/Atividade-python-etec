
def main():
    num = int(input('Digite o número: '))
    
    if num >= 0 and num <= 10:
        print('Ta certo')
        main()

    elif num >= 11 and num <= 20:
        print('ta certo')
        main()

    elif num >= 21 and num <= 30:
        print('ta certo') 
        main()

    elif num >= 31 and num <= 40:
        print('ta certo')
        main()

    else:
        print('ta errado')
        main()

main()