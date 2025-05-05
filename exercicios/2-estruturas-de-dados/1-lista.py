# Crie uma lista apenas com elementos numéricos
idades = [12, 13, 21, 45]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
pessoa = ['Vini', 36, 2010, ['Inglês', 'Espanhol'],'Barbara', 42, 2000, ['Alemão', 'Espanhol']]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(pessoa[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(pessoa[::2])
# Remova da lista o último item
pessoa.pop()
print(pessoa)
# Insira na lista um novo item
pessoa.append(['Inglês', 'Espanhol'])
print(pessoa)
# Remova da lista um item específico
pessoa.remove(2010)
print(pessoa)