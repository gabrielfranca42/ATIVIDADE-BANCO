class ClienteView:
    @staticmethod
    def mostrar_clientes(clientes):
        for c in clientes:
            print(f"Nome: {c['nome']}, Idade: {c['idade']}, Email: {c['email']}, Telefone: {c['telefone']}, Cidade: {c['cidade']}")

    @staticmethod
    def mostrar_cliente(cliente):
        if cliente:
            print(f"Nome: {cliente['nome']}, Idade: {cliente['idade']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Cidade: {cliente['cidade']}")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def mostrar_mensagem(msg):
        print(msg)
