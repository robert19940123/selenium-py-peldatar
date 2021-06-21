age = int(input("Hány éves vagy?"))
drink = input("Mit szeretnél inni?")


if drink != "kóla" and drink != "sör":
    print("Csak sört és kólát tudunk adni!")
    exit()
if age > 60 and drink == "kóla":
    print("A koffein megemelheti a vérnyomásod!")
elif age < 18 and drink == "sör":
    print("Sajnos nem adhatok!")
else:
    print(f"Parancsolj, itt a {drink}!")















