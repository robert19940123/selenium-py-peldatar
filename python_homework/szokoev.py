def szokoev(year):

    if (year % 400) == 0:
        print(f'A megadott év ({my_year}) szökőév!')
    elif (year % 100) == 0:
        print(f'A megadott év ({my_year}) nem szökőév!')
    elif (year % 4) == 0:
        print(f'A megadott év ({my_year}) szökőév!')
    else:
        print(f'A megadott év ({my_year}) nem szökőév!')


while True:
    my_year = int(input("Adjon meg egy évszámot!"))
    szokoev(my_year)
    print()
    if my_year == 0:  #hogy ki lehessen lepni :)
        break





























