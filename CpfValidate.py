from dataclasses import dataclass
import regex

@dataclass
class CpfValidador:
    TAM_MAX_CPF = 11
    cpf_to_validate: str = ''

    @classmethod
    def _validate_cpf_entry (cls, to_validate: str)->str:
        if to_validate is None:
            return 'CPF nulo'
    
        if to_validate == '':
            return 'CPF vazio'
    
        return 'OK'

    
    @classmethod
    def _validate_cpf_len  (cls, to_validate: str)->str:
        to_validate = regex.sub(r'\D', '', to_validate)
        if len(to_validate) != cls.TAM_MAX_CPF:
            return f'CPF com {len(to_validate)} caracteres'
        
        return 'OK'

    @classmethod
    def _check_equal_chars (cls, to_validate: str)->str:
        first_char = to_validate[0] 
        equal_chars = 1
        for c in range(1, len(to_validate)):
            if to_validate[c] == first_char:
                equal_chars += 1
            else:
                break

        if (equal_chars == cls.TAM_MAX_CPF):
            return f'CPF com todos caracteres iguais'   
        
        return 'OK'


    @classmethod
    def _calculate_module(cls, dv_to_check: int, soma: int, msg: str) -> int:
        rest = soma % cls.TAM_MAX_CPF
        generated_dv = 0 if rest < 2 else 11 - rest
        if generated_dv != int(dv_to_check):
            return msg
        
        return 'OK'

    @classmethod
    def _validate_first_dv  (cls, to_validate: str)->str:
        dv = 0
        for nCount in range(1, len(to_validate) - 1):
            dv += (cls.TAM_MAX_CPF - nCount) * int(to_validate[nCount - 1])
            
        dv_to_check = to_validate[cls.TAM_MAX_CPF-2]
        return cls._calculate_module(dv_to_check, dv, 'Dv1 invalido')

    @classmethod
    def _validate_second_dv (cls, to_validate: str)->str:
        dv = 0
        for nCount in range(0, len(to_validate) - 1):
            dv += (cls.TAM_MAX_CPF - nCount) * int(to_validate[nCount])
        
        dv_to_check = to_validate[cls.TAM_MAX_CPF-1]
        return cls._calculate_module(dv_to_check, dv, 'Dv2 invalido')

    @classmethod
    def validate(cls, cpf_to_validate: str)->str: 
        result_message = cls._validate_cpf_entry(cpf_to_validate)
        if (result_message != 'OK'):
            return result_message
        
        result_message = cls._validate_cpf_len(cpf_to_validate)
        if (result_message != 'OK'):
            return result_message
        
        result_message = cls._check_equal_chars(cpf_to_validate)
        if (result_message != 'OK'):
            return result_message

        result_message = cls._validate_first_dv(cpf_to_validate)
        if (result_message != 'OK'):
            return result_message

        result_message = cls._validate_second_dv(cpf_to_validate)
        if (result_message != 'OK'):
            return result_message

        return 'OK'





