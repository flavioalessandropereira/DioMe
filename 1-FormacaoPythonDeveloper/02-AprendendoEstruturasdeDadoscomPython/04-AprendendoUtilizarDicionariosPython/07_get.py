contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# get verifica se há exitência da chave
resultado = contatos.get("chave")  # None
print(resultado)

# get verifica se há exitência da chave
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
