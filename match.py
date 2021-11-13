# Testando nova funcionalidade do Python 3.10
# Match Case

lista = [1, 2, 3]

match lista:
    case [] | [_]:  # len(lista) == 0 or len(lista) == 1
        print("Um ou nenhum elemento")
    case [1, 2]:  # len(lista) == 2 and lista[0] == 1 and lista[1] == 2
        print("Lista = [1, 2]")
    case [1, *resto]:  # lista[0] == 1 and len(lista) >= 1
        print(f"Um é o primeiro e o {resto=}")  # Fixture do Python3.8 utilizando o "=" na formatação


def chato_das_cores(cor):  # Exemplo de Case Guard
    match cor:
        case r, g, b:  # Valores que são separados por virgulas, serão tuplas independente dos parenteses
            return 'Cadê o alpha?'
        case r, g, b, a if a == 255:
            return 'Tudo transparente? É Sério?'
        case r, g, b, a if r == 255:
            return 'Muito vermelho'
        case r, g, b, a if g == 255:
            return 'Muito verde :('
        case r, g, b, a if b == 255:
            return 'Azul? Sério?'
        case r, g, b, a:
            return 'Agora sim!!'


# Implementado operador AS no Case

def movimento(comando: str) -> str:
    match comando.split():
        case ['pular']:
            return 'Pulando'
        case ['mover']:
            return 'Pra onde?'
        case 'mover', 'direita' | 'esquerda' as direcao:
            return f'Movendo lateralmente para {direcao}'
        case 'mover', 'cima' | 'baixo' as direcao:
            return f'Movendo horizontalmente para {direcao}'


# O caso dos dicionários

dicionario = {}

match dicionario:
    case {'a': 1, 'b': 2}:
        print("match literal")
    case {'a': _, 'b': 2}:
        print('match na chave b')
    case {'a': 1, 'b': _}:
        print('match na chave a')
    case {'a': _, 'b': _}:
        print('nenhum match')
    case {'error': _}:
        print("deu erro")

# Empacotamento

d = {'chave': 'valor', 'outra chave': 'outro valor'}

match d:
    case {'chave': 'valor', **kwargs} if kwargs:
        print(kwargs)

# Match com objetos

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    funcionario: bool = False


# def preço(pessoa: Pessoa, valor: int) -> str:
#     match pessoa:
#         case Pessoa(_, idade) if idade >= 65:
#             return f'Você paga meia {valor/2}'
#         case Pessoa(nome, _, True):
#             return f'{nome.capitalize()} você paga {valor/3}'

#
# print(preço(
#     Pessoa('Matheus', 20, True), 20
# ))


# Match com classes tradicionais

# É necessário implementar "__match__args__" para funcionar da mesma forma que estava com o Dataclass


class Pessoa1:
    __match__args__ = ('nome', 'idade', 'funcionario')  # Ordem que irá validar no posicional

    def __init__(self, nome, idade, funcionario=False):
        self.nome = nome
        self.idade = idade
        self.funcionario = funcionario


# Sem o __match__args__, seria necessário dar nome as variaveis da função, exemplo: "nome=nome, idade=idade"

def preço(pessoa: Pessoa, valor: int) -> str:
    match pessoa:
        case Pessoa(_, idade) if idade >= 65:
            return f'Você paga meia {valor / 2}'
        case Pessoa(nome, _, True):
            return f'{nome.capitalize()} você paga {valor / 3}'


print(preço(
    Pessoa('Matheus', 20, True), 20
))
