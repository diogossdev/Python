def quantidade_divisores(n:int) -> int:
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores

def primo(p:int) -> bool:
    if quantidade_divisores(p) == 2:
        return True
    else:
        return False

#programa principal

print('Números primos entre 1 e 100')
for j in range(1, 101):
    if primo(j) == True:
        print(j, 'primo')
