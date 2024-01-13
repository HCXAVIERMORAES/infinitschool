'''Crie uma tupla para representar as informações de três
palestrantes, cada uma contendo o nome, o tema da
palestra e a instituição à qual estão vinculados.
Exiba na tela as informações do terceiro palestrante,
incluindo nome, tema da palestra e instituição.'''
# Criar uma tupla para representar as informações de três palestrantes
palestrantes = (
    ("Palestrante1", "Tema1", "Instituição1"),
    ("Palestrante2", "Tema2", "Instituição2"),
    ("Palestrante3", "Tema3", "Instituição3")
)

# Exibir as informações do terceiro palestrante
terceiro_palestrante = palestrantes[2]
nome, tema, instituicao = terceiro_palestrante

# Exibir as informações na tela
print("Informações do Terceiro Palestrante:")
print(f"Nome: {nome}")
print(f"Tema da Palestra: {tema}")
print(f"Instituição: {instituicao}")
