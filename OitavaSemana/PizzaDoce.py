# Classe filha - subClass()
from pizza import PizzaPadrao

class PizzaDoce(PizzaPadrao):
    def __init__(self, sabor, tamanho, preco, ingredientes, borda_recheada):
        super().__init__(sabor,tamanho,preco,ingredientes)
        self.borda_recheada = borda_recheada
        
    def mostrar_detalhes(self):
        super().mostrar_detlhes()
        print(f'''
                borda recheada: {self.borda_recheada}
            ''')

# criando objetos
pizza_comum = PizzaPadrao("calabresa", "pequeno", 29.90, ["tomate", "oregano", "calabresa", "queijo", "cebola"])
pizza_chocolate = PizzaDoce("chocolate com morango", "pequeno", 31.90, ["chocolate","morango"],"chocolate")

print(" --- pizza comum ---")
pizza_comum.mostrar_detlhes()
print(" --- pizza doce ---")
pizza_chocolate.mostrar_detalhes()

