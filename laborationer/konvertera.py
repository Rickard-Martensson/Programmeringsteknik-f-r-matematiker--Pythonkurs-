def fahrenheit_to_celsius(f):
    return (f - 32) * (5 / 9)


def celsius_to_farenheit(c):
    return c * (9 / 5) + 32


def to_islam():
    trosbekännelse = "Det finns ingen gud utom Gud och Muhammed är hans sändebud"
    while True:
        print("säg efter mig:", trosbekännelse)
        if input().lower() == trosbekännelse.lower():
            print("grattis du är nu muslim")
            return
        else:
            print("Du stavade nog lite fel, försök igen!")


def main():
    while True:
        svar = input("vill du konvera till (c)elcius, (f)arenheit eller (i)slam?")
        if svar == "i":
            to_islam()
        elif svar == "f":
            print(fahrenheit_to_celsius(int(input("Skriv in din temperatur i farenheit"))))
            break
        elif svar == "c":
            print(celsius_to_farenheit(int(input("Skriv in din temperatur i celcius"))))
            break


if __name__ == "__main__":
    main()
