from controller import ClienteController
from view import ClienteView

controller = ClienteController()
view = ClienteView()


controller.criar_cliente("Ana Silva", 28, "ana@email.com", "11987654321", "São Paulo")
controller.criar_cliente("Bruno Santos", 35, "bruno@email.com", "21987654321", "Rio de Janeiro")

clientes = controller.listar_clientes()
view.mostrar_clientes(clientes)

##xdxd
cliente = controller.buscar_cliente("ana@email.com")
view.mostrar_cliente(cliente)


controller.atualizar_cliente("ana@email.com", {"cidade": "Campinas"})
cliente_atualizado = controller.buscar_cliente("ana@email.com")
view.mostrar_cliente(cliente_atualizado)


controller.deletar_cliente("bruno@email.com")
view.mostrar_mensagem("Cliente Bruno deletado.")


clientes = controller.listar_clientes()
view.mostrar_clientes(clientes)
