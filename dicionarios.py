pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(pessoa["nome"])  # Acessa o valor associado à chave "nome"
print(pessoa["idade"])  # Acessa o valor associado à chave "idade"
print(pessoa["cidade"])  # Acessa o valor associado à chave "cidade"

print(pessoa.keys())   # Exibe todas as chaves do dicionário
print(pessoa.values()) # Exibe todos os valores do dicionário
print(pessoa.items())  # Exibe todos os pares chave-valor do dicionário

pessoa.update({"profissão": "Engenheiro"})  # Adiciona um novo par chave-valor
print(pessoa)
