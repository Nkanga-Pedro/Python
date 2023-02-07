# Estrutura de Dados
'''
lista=[1,2,3,4,5,6,7,8,9]
for i in lista:
    if i==4:
        continue
    if i==8:
        break
    print(i)
'''

'''
print(lista)
lista.append(12)
print(lista)
valor=lista.index(1)
print(valor)
lista.pop()
print(lista)
lista.remove(3)
print(lista)
lista.sort()
print(lista)
lista.extend([12,14,13])
print(lista)
lista.clear()
print(lista)
'''
'''
tup=(1,2,4,5,6)
print(tup)
valor=tup.count(4)
print(valor)

lista=[1,2,3,4,5,6,6,8,8,2,3,0]
print(lista)
valor=set(lista)
print(valor)
valor2=(3,5,7)
dif=valor.difference(valor2)
print(dif)

print(type(lista))
print(type(tup))
print(type(valor))

produto={'id':1,'nome':'teclado','modelo':'pt','tamanho':'grande'}
print(produto)
item=produto.items
for item in produto.items():
    print(item)
print(produto.keys())
print(produto.items())
print(produto.values())

produto.clear()
print(produto)
del produto
print(produto)
'''
produto={
    'mouse':20,
    'portatil':650,
    'teclado':50,
    'monitor':120,
    'desktop':450,
    'auricular':50,
    'curso':230,
    'formacao':300
}
print(produto)
item='teclado'
while True:
    if item=='fim':
        break
    if item in produto:
        print(f'produto {item} encontrado tem o preco de {produto[item]}')
    else:
        print('Produto nao encontrado')
