#Criação da função exibir_cardapio()
def exibir_cardapio():
    cardapio = {
    "Mussarela": 30.00,
    "Calabresa": 32.00,
    "Pepperoni": 35.00,
    "Quatro Queijos": 38.00,
    "Frango com Catupiry": 40.00
        }
    print("--- Cardápio da Pizzaria Sabores ---")
    for pizza, preco in cardapio.items():
        print(f"🍕 {pizza}: R$ {preco:.2f}")
    return cardapio

# Criação de função receber_pedido        
def receber_pedido(cardapio):
    pedido = []
    while True:
        sabor = input("Digite o Sabor da Pizza (ou Sair para finalizar)")
        if sabor == "sair":
            break
        elif sabor in cardapio:
            pedido.append(sabor)
            print(f"{sabor} Adicionado com sucesso!")
        else:
            print("Esse sabor não está disponivel. Escolha outro sabor.")
    return pedido

#Criação da função calcular_totaal()
def calcular_total(pedido, cardapio):
    total = 0 
    for pizza in pedido:
        total += cardapio[pizza]
    return total

#criação de função main()
def main():
    cardapio = exibir_cardapio()
    pedido = receber_pedido(cardapio)
    total = calcular_total(pedido, cardapio)
    
    print(" resumo do pedido ")
    for pizza in pedido:
        print(f"pizza de {pizza} R$ {cardapio[pizza]:.2f}")
    print(f" Total a pagar : R$ {total:.2f}")
    
#esos
main()