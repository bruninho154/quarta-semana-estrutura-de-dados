#Classe pai - superClass()
class PizzaPadrao:
    def __init__(self, sabor, tamanho, preco, ingredientes):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.ingredientes = ingredientes
        
    def mostrar_detlhes(self):
        print(f'''
            --- detalhes da pizza ---
                sabor: {self.sabor}
                tamanho: {self.tamanho}
                preco: {self.preco:.2f}
                ingredientes:''')
        
        for ingrediente in self.ingredientes:
            print(f'                  - {ingrediente}')

pizza_calabresa = PizzaPadrao("calabresa", "pequeno", 50.00, ["tomate", "oregano", "calabresa", "queijo", "cebola"])        
pizza_marguerita = PizzaPadrao("marguerita", "medio", 55.00, ["tomate", "oregano", "queijo"])

#pizza_calabresa.mostrar_detlhes()
#pizza_marguerita.mostrar_detlhes()
