def fahrenheit_to_celsius(f: int):
    """
    Converts a temperature in farenheit to a temperature in celcius

    Args:
        f (int): [a temperature in farenheit]

    Returns:
        [float]: [a temperateture in celcius]

    Example usage:
    122 -> 50.0
    -40 -> -40.0
    """
    return (f - 32) * (5 / 9)


def celsius_to_farenheit(c: int):
    """
    Converts a temperature in celcius to a temperature in farenheit

    Args:
        f (int): [a temperature in celcius]

    Returns:
        [float]: [a temperateture in farenheit]

    Example usage:
    50 -> 122.0
    -40 -> -40.0
    """
    return c * (9 / 5) + 32


def to_islam():
    """
    Forces the user to recite the Shahada, converting them to the one true faith
    """
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
