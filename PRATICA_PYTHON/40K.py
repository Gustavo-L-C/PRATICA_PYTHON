#WARHAMMER 40K | SPACE MARINE 2 | CHAPTER SELECTOR RANDOM - 08.05.26

import random
from chapters40k import lista_chapters_D
from chapters40k import lista_chapters
from bancodenomes import sim_sim
#from bancodenomes import nao_nao

classe = ['Tatico🔫','Assalto🚀','Vanguarda🗡️','Baluarte🏳️','Sniper🎯','Pesado🛡️','Techmarine⚙️']

print(f'\n', '-'*80) #só enfeite

print('\nSeletor de Capitulo e Classe aleatorio para Space Marines 2\n')
r = input('Pronto?')
print('')


if r in sim_sim:
    rc = random.choice(lista_chapters_D)
    print(f'Capitulo {rc}')

    if rc == 'DeathWatch':
        print(rc)
        dw = input('Agora na DeathWatch, pronto para saber seu capitulo?')

        if dw in sim_sim:
            dc = random.choice(lista_chapters)
            print(f'Capitulo {dc}')

        else:
            print(f'Então agora voce e um Black Shield da {rc}.')

else:
    print('Ok')

print('')
qclasse = input(f'Quer escolher uma classe para {rc}?')
print('')

if qclasse in sim_sim:
    #eclasse = input('Quer escolher a classe radom ou manual?')
    #manu = ['MANUAL','manual','Manual']

    #if eclasse in manu:
    #   ec = input('\nOk, qual classe: ')
    #   print(f'\nClasse: {ec}')
        classes = random.choice(classe)
        print(f'A classe para {rc} é {classes}.')

else:
        print('Ok')


print(f'\n', '-'*80) #só enfeite