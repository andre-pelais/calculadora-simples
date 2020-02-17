# Calculadora em Python

# Mensagens que serão mostradas na tela no momento em que o programa for aberto
print('******* Calculadora em Python *******')

print('Selecione o número da operação desejada:')  

print('1 - Soma')

print('2 - Subtração')

print('3 - Multiplicação')

print('4 - Divisão')

# Iniciando os inputs
a = input('Qual operação você deseja (1/2/3/4)? ') # Esta variável recebe o valor que define a operação desejada.

b = int(input('Digite o primeiro valor: ')) # Esta variável recebe o primeiro valor.

c = int(input('Digite o segundo valor: ')) # Esta variável recebe o segundo valor.

if a == '1':  # O if servirá pra iniciar os condicionais e realizará a soma, a variável d receberá o valor dos operadores.
	d = b + c
	print('A resposta é: %s' %(d))
elif a == '2':  # Este elif realiza a subtração.
	d = b - c
	print('A resposta é: %s' %(d)) 
elif a == '3': # Este elif realiza a multiplicação.
	d = b * c
	print('A resposta é: %s' %(d))
elif a == '4': # Este elif realiza a divisão.
	d = b / c
	print('A resposta é: %s' %(d))
else: # Se o valor digitado for diferente de 1 a 4, o programa mostra que a opção é inválida.
	print('Opção inválida!!')
