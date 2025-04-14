import regex

TAM_MAX_CPF = 11

def validate_cpf_entry (to_validate: str)->str:
    if to_validate is None:
        return 'CPF nulo'
    
    if to_validate == '':
        return 'CPF vazio'
    
    return 'OK'

    
def validate_cpf_len  (to_validate: str)->str:
    to_validate = regex.sub(r'\D', '', to_validate)
    if len(to_validate) != TAM_MAX_CPF:
        return f'CPF com {len(to_validate)} caracteres'
    
    return 'OK'

def check_equal_chars (to_validate: str)->str:
    first_char = to_validate[0] 
    equal_chars = 1
    for c in range(1, len(to_validate)):
        if to_validate[c] == first_char:
            equal_chars += 1
        else:
            break

    if (equal_chars == TAM_MAX_CPF):
        return f'CPF com todos caracteres iguais'   
    
    return 'OK'


def calculate_module(dv_to_check: int, soma: int, msg: str) -> int:
    rest = soma % TAM_MAX_CPF
    generated_dv = 0 if rest < 2 else 11 - rest
    if generated_dv != int(dv_to_check):
        return msg
    
    return 'OK'

def validate_first_dv (to_validate: str)->str:
    dv = 0
    for nCount in range(1, len(to_validate) - 1):
        dv += (TAM_MAX_CPF - nCount) * int(to_validate[nCount - 1])
        
    dv_to_check = to_validate[TAM_MAX_CPF-2]
    return calculate_module(dv_to_check, dv, 'Dv1 invalido')

def validate_second_dv (to_validate: str)->str:
    dv = 0
    for nCount in range(0, len(to_validate) - 1):
        dv += (TAM_MAX_CPF - nCount) * int(to_validate[nCount])
    
    dv_to_check = to_validate[TAM_MAX_CPF-1]
    return calculate_module(dv_to_check, dv, 'Dv2 invalido')

def validate_cpf(cpf_to_validate: str)->str: 
    result_message = validate_cpf_entry(cpf_to_validate)
    if (result_message != 'OK'):
        return result_message
    
    result_message = validate_cpf_len(cpf_to_validate)
    if (result_message != 'OK'):
        return result_message
    
    result_message = check_equal_chars(cpf_to_validate)
    if (result_message != 'OK'):
        return result_message

    result_message = validate_first_dv(cpf_to_validate)
    if (result_message != 'OK'):
        return result_message

    result_message = validate_second_dv(cpf_to_validate)
    if (result_message != 'OK'):
        return result_message

    return 'OK'





