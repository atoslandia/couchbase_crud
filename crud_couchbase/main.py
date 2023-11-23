import persistencia


# criação de produtos
banana = {
    "nome": "banana",
    "preco": 5.99,
    "quantidade": "um caxo"
}
agua = {
    "nome": "agua",
    "marca": "indaia",
    "preco": 3,
    "litro": 1
}

# operações crud sendo executadas
print("INSERCAO DE PRODUTOS:")
persistencia.criar_produto("detergente", detergente)
persistencia.criar_produto("banana", banana)
persistencia.criar_produto("agua", agua)

print("\nBUSCA:")
persistencia.buscar_produto("detergente")
persistencia.buscar_produto("banana")
persistencia.buscar_produto("agua")

print("\nREMOCAO:")
persistencia.deletar_produto("agua")
detergente = {
    "nome": "detergente",
    "marca": "ype",
    "preco": 4.55,
    "ml": 500
}

print("\nATUALIZACAO:")
detergente["preco"] = 3.15
persistencia.atualizar_produto("detergente", detergente)
