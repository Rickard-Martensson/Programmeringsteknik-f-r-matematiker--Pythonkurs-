även en klocka som stannat visar rätt två gånger om dagen

# 2

För många elif statements som leder till samma sak.
skriv istället något i stil med

if Question in {"C", "Celsius"}.

om du inte vill att det ska spela någon roll med stora/små bokstäver i indata kan du också skriva

if Question.toLower() in {"C", "Celsius"}.

Snyggt med en loop dock!

# 3

Saknar totalt dokumentation. Använd min standardtemplate nästa gång

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

Alltså 1. en kort beskrivning (skriv gärna komplexiteten här) 2. Beskrivning av indata 3. Beskrivning 4. Exempel på input och output.

# Förenklade definitionerna lite

def fahrenheit_to_celsius(t):
return (t-32) / 1.8

def celsius_to_fahrenheit(t):
return t\*1.8 + 32

# Frågan om vad som ska omvandlas och hur många grader

fraga = int(input('1. Vill du omvandla Fahrenheit till Celsius, tryck 1 \n2. Vill du omvandla Celsius till Fahrenheit, tryck 2: '))

while True:
if fraga == 1:
f = float(input('Vilken temperatur vill du konvertera: '))
print(f,'�F =',format(fahrenheit_to_celsius(f),'.2f'),'�C')
exit()

    elif fraga == 2:
        c = float(input('Vilken temperatur vill du konvertera: '))
        print(c,'�C =',format(celsius_to_fahrenheit(c),'.2f'),'�F')
        exit()
    else:
        print("du skrev fel, försök igen")
