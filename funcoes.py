# As funcoes
def soma(x,y):
    s=x+y
    print(f'A soma eh {s}')

soma(3,4)

def produto(x,y):
    prod=x*y
    return prod

valor=produto(3,4)
print('o produto dos dois valores sao {}'.format(valor))

def recursao(x):
    if x<=1:
        return 1
    else:
        return (x*recursao(x-1))
    return x

valor=recursao(4)
print(valor)

divisao=lambda x:x/2
valor=divisao(4)
print(valor)

nomec=lambda nome='nkanga',sobrenome='pedro':nome+'-'+sobrenome
print(nomec())

lista=[1,2,3,4,5,6,7,8,9,10]
soma=lambda total:sum(lista)
res=soma(lista)
print(res)

def quadrado(n):
    return n**2
resultado=map(quadrado,lista)

for valor in resultado:
    print(valor)