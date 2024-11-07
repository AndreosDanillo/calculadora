while True: # laço de repetição sempre vai ocorrer
    numero = input('Digite o primeiro número: ')
    if numero.isdigit(): # verifiando se digitou um número
        numero_int = int(numero) # tranformando em número inteiro
    else: # caso não seja digitado um número
        print('Você não digitou um número')
        break
    
    operador = input('Qual operador vai ser utilizado: +(Adiçaõ), -(Subtração), /(Divisão), *(Multiplicação): ')
    if operador != '+' and operador != '-' and operador != '/' and operador != '*': # caso seja digitado algo diferente das propostas(+, -, /, *)
        print('Você não digitou o operador corretamente')
        break
    
    numero_2 = input('Digite o segundo número: ') 
    if numero_2.isdigit(): # verifiando se digitou um número
        numero_int_2 = int(numero_2) # tranformando em número inteiro
    else: # caso não seja digitado um número
        print('Você não digitou um número')
        break

    ad = numero_int + numero_int_2 # adição
    sub = numero_int - numero_int_2 # subtração
    div = numero_int / numero_int_2 # divisão
    mult = numero_int * numero_int_2 # multiplicação

    if operador == '+': # caso seja +(adição)
        print(f'Seu resultado foi: {ad}')
        
    elif operador == '-': # caso seja -(subtração)
        print(f'Seu resultado foi: {sub}')
        
    elif operador == '/': # caso seja /(divisão)
        print(f'Seu resultado foi: {div}')
        
    elif operador == '*': # caso seja *(multiplicação)
        print(f'Seu resultado foi: {mult}')

    continuar = input('Deseja continuar (sim/nao):  ') # continuação da calculadora
    if continuar == 'nao': # caso não queira continuar
        print('Obrigado por usar a calculadora')
        break