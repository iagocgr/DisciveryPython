""" 
Se eu fosse Isaac Newton, eu explicaria a linguagem Python como uma ferramenta matemática poderosa e versátil, 
que permite resolver problemas complexos de forma simples e elegante. Eu diria que Python é baseada em alguns princípios fundamentais, como:

A legibilidade do código é importante, por isso Python usa a indentação significativa para definir blocos de código
Python é uma linguagem dinâmica e de alto nível, que abstrai muitos detalhes de baixo nível e facilita a expressão de ideias
Python é uma linguagem multi-paradigma, que suporta vários estilos de programação, como estruturada, orientada a objetos, funcional e reflexiva
Python é uma linguagem extensível, que pode ser integrada com outras linguagens e sistemas, e possui uma biblioteca padrão abrangente que oferece muitas funcionalidades2
Eu também mostraria alguns exemplos de código Python para ilustrar esses conceitos, como: 
""" 


# Exemplo de indentação significativa
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

# Exemplo de linguagem dinâmica e de alto nível
texto = "Olá, mundo!"
print(texto.upper()) # Converte o texto para maiúsculas
print(len(texto)) # Calcula o comprimento do texto

# Exemplo de linguagem multi-paradigma
# Programação estruturada
soma = 0
for i in range(1, 11):
    soma += i
print(soma)

# Programação orientada a objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos.")

p = Pessoa("Isaac", 84)
p.apresentar()

# Programação funcional
def quadrado(x):
    return x**2

lista = [1, 2, 3, 4, 5]
nova_lista = list(map(quadrado, lista)) # Aplica a função quadrado a cada elemento da lista
print(nova_lista)

# Programação reflexiva
def somar(a, b):
    return a + b

print(type(somar)) # Imprime o tipo da função somar
print(dir(somar)) # Imprime os atributos da função somar
print(somar.__name__) # Imprime o nome da função somar
print(somar.__code__) # Imprime o código da função somar

# Exemplo de linguagem extensível e com biblioteca padrão
import math # Importa o módulo de matemática
import random # Importa o módulo de números aleatórios
import requests # Importa o módulo de requisições HTTP (requer instalação prévia)

print(math.pi) # Imprime o valor de pi
print(random.randint(1, 10)) # Gera um número inteiro aleatório entre 1 e 10
r = requests.get("https://www.python.org") # Faz uma requisição GET ao site oficial do Python
print(r.status_code) # Imprime o código de status da resposta
