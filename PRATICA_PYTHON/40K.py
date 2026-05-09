#WARHAMMER 40K | SPACE MARINE 2 | CHAPTER SELECTOR RANDOM - 08.05.26

import random
from chapters40k import lista_chapters_D
from chapters40k import lista_chapters
from bancodenomes import sim_sim
#from bancodenomes import nao_nao

classe = ['Tatico🔫','Assalto🚀','Vanguarda🗡️','Baluarte🏳️','Sniper🎯','Pesado🛡️','Techmarine⚙️']
rc = random.choice(lista_chapters_D)

print(f'\n', '-'*80) #só enfeite

print('\nSeletor de Capitulo e Classe aleatorio para Space Marines 2\n')
r = input('Pronto?')
print('')

qclasse = input(f'Quer uma classe aleatória?')
print('')

if qclasse in sim_sim:
       classes = random.choice(classe)
       print(f'A classe aleatoria é {classes}.')

else:
    ec = input('Qual classe?')
    print(f'\nClasse escolhida: {ec}')

#if r in sim_sim:
print(f'Capitulo: {rc}')

if rc == 'DeathWatch':
   print(rc)
   dw = input('Agora na DeathWatch, pronto para saber seu capitulo de origem?')

   if dw in sim_sim:
    dc = random.choice(lista_chapters)
    print(f'Capitulo: {dc}')

   else:
    print(f'Então agora voce e um Black Shield da {rc}.')

print('')

print(f'\n', '-'*80) #só enfeite