def potencia(num):
    result = num**2
    return result

#print (potencia(4));

#passando para lambda, só aceita um argumento

potencia = lambda num:num**2
print(potencia(7));