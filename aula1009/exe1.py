# 1. **Exiba um cardápio:** Crie um **dicionário** para armazenar o cardápio da pizzaria, contendo pelo menos 5 sabores e seus respectivos preços (por exemplo, `{"Mussarela": 30.00, "Calabresa": 32.00}`).
# 2. **Receba o pedido:** Use um **loop `while`** para permitir que o cliente adicione vários sabores ao pedido. O loop deve continuar até que o cliente digite "sair". Armazene os sabores escolhidos em uma **lista**.
# 3. **Calcule o total:** Percorra a lista de pedidos com um **loop `for`** e calcule o valor total a ser pago, somando os preços de cada pizza com base no dicionário do cardápio.
# 4. **Imprima o resumo:** Ao final do pedido, imprima um resumo formatado, mostrando cada pizza pedida e o valor total final.

# 1. Crie um dicionário (dict) para o cardápio.
cardapio = {
    "Mussarela": 30.00,
    "Calabresa": 32.00,
    "Pepperoni": 35.00,
    "Quatro Queijos": 38.00,
    "Frango com Catupiry": 40.00
}

pedido = [] #Lista vazia
print("🍕Bem-vindo à pizzaria Sabores!")
print("Faça seu pedido (digite sair para encerrar):")

# 2. Recebe o pedido com um loop while.
while True:
    sabor_escolhido = input("Escolha um sabor: ")
    if sabor_escolhido.lower() == "sair":
        break # Encerra o loop quando o cliente digita 'sair'
    elif sabor_escolhido in cardapio:
        pedido.append(sabor_escolhido)
        print(f"🍕 {sabor_escolhido} adicionado ao seu pedido!")
    else:
        print(" ❌ Esse sabor não está no cardápio. Escolha outro.")

# 3. Calcule o total do pedido com um loop for.
total = 0
for sabor in pedido:
    total += cardapio[sabor]

# 4. Imprimir o resumo
print("🛒 ---- Resumo do Pedido ----")
if pedido: # Verifica se existe algum valor em pedido
    for sabor in pedido:
        print(f"➡️ {sabor}: R$ {cardapio[sabor]:.2f}") # Devolve o valor do sabor da pizza se ela estiver no dicionário cardapio.
    print(f"💵 Total a pagar: R${total:.2f}")
else:
    print("❌ Nenhuma pizza foi pedida. Volte sempre.")
    
