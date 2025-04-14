from CpfValidate import  CpfValidador


#print(f"Parametro nulo => {validate(None)}")
#print(f"Parametro '' => {validate('')}")
#print(f"Parametro com 10 numeros  => {validate('1'*10)}")
#print(f"Parametro com 12 numeros => {validate('1'*12)}")
#print(f"Parametro com 11 chars => {validate('1'*11)}")
#print(f"Parametro com 12 chars => {validate('x'*12)}")
#print(f"Parametro com 11 chars => {validate('x'*11)}")
print(f"Parametro invalido => {CpfValidador.validate('01834522718')}")
print(f"Parametro invalido => {CpfValidador.validate('01834522758')}")
print(f"Parametro valido => {CpfValidador.validate('01834522757')}")
