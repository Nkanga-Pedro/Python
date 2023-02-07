# Fundamento para Python

# As 3 Formas de Apresentar os resultados
id=1
nome='Nkanga-Pedro'
idade=31
salario=299.256
sexo='masculino'

print(f'o cidadao {nome} possui o codigo de {id} do sexo {sexo} e com salario de {salario}')
print('o cidadao {} possui o codigo de {} do sexo {} e com salario de {}'.format(nome,id,sexo,salario))
print('o cidadao %s possui o codigo de %.03d do sexo %s e com salario de %.03f' %(nome,id,sexo,salario))

# Fatiamento e String
endereco='nkangapedroinfo@gmail.com'
usuario,dominio=endereco.split('@')
print('o usuario eh {} e o seu dominio eh {}'.format(usuario,dominio))

fat1=endereco[:]
fat2=endereco[2:6]
fat3=endereco[::2]
fat4=endereco[::-1] # A minha nova senha...ok

print(fat1)
print(fat2)
print(fat3)
print(fat4)

# desafio para fundamento
'''
parcela=float(input('insere o valor da parcela'))
qte=int(input('insere a quantidade de meses'))
valor=parcela*qte
print('O valor da compra eh: {}, onde {} eh o resultado do calculo'.format(parcela,valor))
'''

# Condição if e else
nota1=13
nota2=7
media=(nota1+nota2)/2
if media>=13.5:
    print('A media eh de {} e dispensado'.format(media))
elif media<13.5 and media>=9.5:
    print('A media eh {} pode fazer exame'.format(media))
else:
    print('A media de {} e nao tem possibilidade de fazer exame'.format(media))


# Condição repetitiva
for i in range(1,10):
    print(i)
mensagem=['nkanga','pedro','kareem','nuriane','rebeca','diki']
for nome in mensagem:
    print(nome)
for i in range(2,20,2):
    print(i)
i=0
soma=0
while i<=0:
    soma+=i;
    print(soma)