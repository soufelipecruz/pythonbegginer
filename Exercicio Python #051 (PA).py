print('==='*15)
print('10 TERMOS DE UMA PA')
print('==='*15)
prim_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
pa = prim_termo + (10 - 1) * razao
for c in range(prim_termo, pa + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')
