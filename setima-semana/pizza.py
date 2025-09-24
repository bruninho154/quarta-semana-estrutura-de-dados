class Pizza:
    # Atributos da Classe (Construtor padrão)
    def __init__(self, sabor, tamanho, preco):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
    
    # Método nosso criado para descrever
    def descricao(self):
        return f"Pizza de {self.sabor}, Tamanho: {self.tamanho}Preço: R$ {self.preco:.2f}"

# Criando objetos da classe Pizza
pizza1 = Pizza("Calabresa", "Família", 52.00)
pizza2 = Pizza("Mussarela", "Média", 49.90)
print(pizza1.descricao())
print(pizza2.descricao())