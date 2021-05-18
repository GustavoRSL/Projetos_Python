class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome_Produto = nome
        self.preco_Unitario = preço
        self.qtd_Estoque = estoque
    
    # Registrar Produto (1)
    def registrar_Produto(nome, preço, estoque):
        Objeto = Produto(nome,preço,estoque)
        return Objeto
    
    # Listar Produtos (2)
    def listar_Produtos(lista):
        for objeto in lista:
            print(f'Nome do produto: {objeto.nome_Produto} Preço unitário: {objeto.preco_Unitario} Quantidade em estoque: {objeto.qtd_Estoque}' )

    # Deletar Produto (3)
    def deletar_Produto(self, lista):
        lista.remove(self)
        print('Item removido com sucesso!')
    
    # Adicionar estoque (4)
    def adicionar_Estoque(self):
        qtd_adicionada = int(input('Informe a quantidade a ser adicionada no estoque: '))
        self.qtd_Estoque += qtd_adicionada
    
    # Altera valor unitário (5)
    def altera_Valor(self):
        novo_valor = float(input('Informe o novo valor do produto: '))
        if novo_valor > 0:
            self.preco_Unitario = novo_valor
        else:
            print('Erro!!! Insira um valor positivo')
    
    # Remove estoque (6)
    def remove_Estoque(self):
        qtd_removida = int(input('Informe a quantidade a ser retirada no estoque: '))
        self.qtd_Estoque -= qtd_removida
        
    # Procurar Produto
    def procura_Produto(lista):
        nome = input('Informe nome do produto: ')
        for objeto in lista:
            if objeto.nome_Produto == nome:
                return objeto
    

def menu():
    print('#####################################')
    print('Digite 1: Registrar um produto.')
    print('Digite 2: Listar os produtos.')
    print('Digite 3: Remover um produto.')
    print('Digite 4: Adicionar estoque.')
    print('Digite 5: Altera valor unitário.')
    print('Digite 6: Realizar uma venda.')
    print('#####################################')
    
if __name__ == "__main__":
    
    programa = True
    produto = Produto
    lista = []
    
    
    while programa == True:
        menu()
        op = int(input('Digite sua opção: '))
        if op == 1:
            nome = input('Digite nome do produto: ')
            preço = float(input('Digite preço do produto: '))
            estoque = int(input('Digite quantidade do produto em estoque: '))
            lista.append(produto.registrar_Produto(nome,preço,estoque))

        elif op == 2:
            produto.listar_Produtos(lista)
        
        elif op == 3:
            objeto = produto.procura_Produto(lista)
            if objeto != None:
                objeto.deletar_Produto(lista)
            else:
                print('Produto não encontrado!')
        
        elif op == 4:
            objeto = produto.procura_Produto(lista)
            if objeto != None:
                objeto.adicionar_Estoque()
            else:
                print('Produto não encontrado!')
        
        elif op == 5:
            objeto = produto.procura_Produto(lista)
            if objeto != None:
                objeto.altera_Valor()
            else:
                print('Produto não encontrado!')
            
        elif op == 6:
            objeto = Produto.procura_Produto(lista)
            if objeto != None:
                produto.remove_Estoque(objeto)
            else:
                print('Produto não encontrado!')
            
        elif op == 0:
            print('Encerrando programa!')
            programa = False
        
        else:
            print('Comando inválido!')
        