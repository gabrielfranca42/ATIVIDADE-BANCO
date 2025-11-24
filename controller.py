from model import ClienteModel

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()

    def criar_cliente(self, nome, idade, email, telefone, cidade):
        cliente = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "telefone": telefone,
            "cidade": cidade#xdxd
        }
        return self.model.inserir(cliente)

    def listar_clientes(self):
        return self.model.listar_todos()

    def buscar_cliente(self, email):
        return self.model.buscar_por_email(email)

    def atualizar_cliente(self, email, novos_dados):
        return self.model.atualizar(email, novos_dados)

    def deletar_cliente(self, email):
        return self.model.deletar(email)
