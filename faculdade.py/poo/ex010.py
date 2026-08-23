while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Dgite outro número: '))
        print(f'{a/b:.2f}')
        print('Sucesso!')
        break
    except ZeroDivisionError:
        print('ERRO --- Divisão por zero!')
    except ValueError:
        print('ERRO --- Digite um número inteiro válido.')
    except:
        print('Erro na execução.')

print('Fim do Programa.')
