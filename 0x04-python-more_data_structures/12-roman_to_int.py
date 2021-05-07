#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not 'str':
        return 0
    letras = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    numero = 0
    s = roman_string
    lenght = len(s)
    for i in range(lenght):
        mul = 1
        if (i is not lenght - 1):
            if ((s[i] is 'C' and s[i + 1] in ['D', 'M']) or
                    (s[i] is 'X' and s[i + 1] in ['L', 'C']) or
                    (s[i] is 'I' and s[i + 1] in ['V', 'X'])):
                mul = -1
        numero += mul * letras[s[i]]
    return numero
