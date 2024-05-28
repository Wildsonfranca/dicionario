# Crie um dicionário em Python com os seguintes dados de uma pessoa:
# - Nome
# - CPF
# - RG
# - Data de Nascimento
# - Gênero
# - E-mail
# - Telefone
# - Tipo sanguíneo
# - Profissão
# - Empresa
# Criando um dicionário vazio
informacoes_usuario = {}

# Solicitando ao usuário que insira suas informações
nome = input("Digite seu nome: ")
cpf = input('Informe seu cpf:')
rg = input('Informe seu RG:')
data_nascimento = input('Informe sua data de nascimento:')
genero = input('Informe seu genero:')
email = input('Inorme seu e-mail:')
telefone =input('Informe seu telefone:')
tipo_sanguineo = input('Informe seu tipo sanguineo:')
profissao = input('Informe sua profissõa:')
empresa = input('informe onde vovê trabalha:')


# Adicionando as informações ao dicionário
informacoes_usuario['nome'] = nome
informacoes_usuario['CPF']  = cpf
informacoes_usuario['RG'] = rg
informacoes_usuario['Data de Nascimento'] = data_nascimento
informacoes_usuario['Genero'] = genero
informacoes_usuario['E-mail'] =email
informacoes_usuario['Telefone'] = telefone
informacoes_usuario['Tipo Sanguineo'] = tipo_sanguineo
informacoes_usuario['Profissão'] = profissao
informacoes_usuario['Empresa']  = empresa

# Mostrando as informações armazenadas no dicionário
print("\nInformações do usuário:")
for chave, valor in informacoes_usuario.items():
    print(f"{chave}: {valor}")
