# 1- crie um programa que aceite pedidos de um ecomerce até que o clinte digite sair.

print(" faça o seu pedido ou digite 'sair' para encerrar")
pedido = "" #string porque sair e um texto
lista = ["Smartphone","SmartTV","Geladeira","videoGame","fogão","Rélogio","Notebook"]
print("◄ PRODUTOS DISPONIVEIS EM ESTOQUE ►")
for produto in lista:
    print(f'Tesmos disponivel o/a {produto}')
    
while pedido.lower != 'sair':
    pedido = input("digite um produto da lista: ")
    if pedido in lista:
        print(f"► {pedido} adicionado ao seu carrinho! ")
    elif pedido.lower() == 'sair':
        print('pedido encerrado com sucesso ‼')
    else:
        print("Esse produto não esta na lista. Escolha outro: ")