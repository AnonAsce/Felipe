lista = []
quantidade = []
faturamento = 0
while True:
    produto = input('Insira o nome do produto:')
    if produto.lower() == 'sair':
        break
while True:
    print('Digite -1 para sair do preço e quantidade!')
    quant = int(input('Insira a quantidade do produto:'))
    preço = float(input('Insira o preço do produto:'))
    if preço == -1 or quant == -1:
        quantidade.append(quant)
    quantidade.append(preço)
    registro = (produto, quant, preço)
    lista.append(registro)
    for i in lista:
        faturamento = faturamento + int(i[1])*(i[2])
        print(f'O faturamento e de:{faturamento}')
