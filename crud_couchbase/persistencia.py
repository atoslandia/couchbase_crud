from bucket import conexao


# funções crud
def criar_produto(chave, produto):
    produto_inserido = conexao.upsert(chave, produto)
    if (produto_inserido.success):
        print("produto inserido:", chave)
    else:
        print("falha ao criar produto")


def buscar_produto(chave):
    try:
        produto = conexao.get(chave)
        print(chave + ":", produto.value)
        return produto
    except Exception as erro:
        print("falha ao buscar produto")


def atualizar_produto(chave, produto):
    produto_para_atualizar = conexao.upsert(chave, produto)
    if (produto_para_atualizar.success):
        print("produto atualizado:", chave)
    else:
        print("falha ao atualizar produto")


def deletar_produto(chave):
    produto_deletado = conexao.remove(chave)
    if (produto_deletado.success):
        print("produto deletado:", chave)
    else:
        print("falha ao deletar produto")
