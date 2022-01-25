def fahrenheit_to_celsius(t):
    t_celcius = (t - 32) / 1.8
    return t_celcius


def celcius_to_farenheit(tc):
    t_farenheit = tc * 1.8 + 32
    return t_farenheit


while True:

    Question = input("Vill du konvertera från Celsius (C), eller Farenheit (F)?")
    if Question == ("C"):
        svar1 = input("Ange en temperatur i Celsius: ")
        tc = celcius_to_farenheit(float(svar1))
        print(svar1, " grader Celsius blir", tc, "grader Farenheit.")

    elif Question == ("Celsius"):
        svar1 = input("Ange en temperatur i Celsius: ")
        tc = celcius_to_farenheit(float(svar1))
        print(svar1, " grader Celsius blir", tc, "grader Farenheit.")

    elif Question == ("c"):
        svar1 = input("Ange en temperatur i Celsius: ")
        tc = celcius_to_farenheit(float(svar1))
        print(svar1, " grader Celsius blir", tc, "grader Farenheit.")
        20

    elif Question == ("F"):
        svar2 = input("Ange en temperatur i Fahrenheit: ")
        t = fahrenheit_to_celsius(float(svar2))
        print(svar2, "grader Farenheit blir", t, "grader Celsius.")

    elif Question == ("Farenheit"):
        svar2 = input("Ange en temperatur i Fahrenheit: ")
        t = fahrenheit_to_celsius(float(svar2))
        print(svar2, "grader Farenheit blir", t, "grader Celsius.")

    elif Question == ("f"):
        svar2 = input("Ange en temperatur i Fahrenheit: ")
        t = fahrenheit_to_celsius(float(svar2))
        print(svar2, "grader Farenheit blir", t, "grader Celsius.")

    else:
        print("Ajdå, nu vart det fel vi försöker igen!")
    while True:
        answer = str(input("Vill du konvertera mera? (y/n): "))
        if answer in ("y", "n"):
            break
        print("Nu vart det lite fel, försök igen med y för ja och n för nej :)")
    if answer == "y":
        continue
    else:
        print("Ha det gött!")
        break
