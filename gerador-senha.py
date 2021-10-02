from random import choice
import string

tamanho = 12  # tamanho da senha
senha = ''  # inicio da senha, apenas declarando variavel
entrada = string.digits + string.ascii_letters + string.punctuation  # caracteres na senha

# gerar a senha
for i in range(tamanho):
    senha = senha + choice(entrada)

print(f'Sua senha gerada é: {senha}')
