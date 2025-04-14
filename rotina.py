import regex

def validate(texto):
    if texto is None:
        return False
    if texto == '':
        return False
    
    # Remove todos os caracteres não numéricos do texto
    texto = regex.sub(r'\D', '', texto)

    if len(texto) != 11:
        return False
    if all(c == texto[0] for c in texto):
        return False
    try:
        d1, d2 = 0, 0
        dg1, dg2, rest = 0, 0, 0
        digito = 0

        for nCount in range(1, len(texto) - 1):
            digito = int(texto[nCount - 1])
            d1 += (11 - nCount) * digito
            d2 += (12 - nCount) * digito

        rest = d1 % 11
        dg1 = 0 if rest < 2 else 11 - rest
        d2 += 2 * dg1
        rest = d2 % 11
        dg2 = 0 if rest < 2 else 11 - rest
        nDigitVerif = texto[-2:]
        nDigResult = f"{dg1}{dg2}"
        return nDigitVerif == nDigResult
    except Exception as e:
        return False
    return True
      
