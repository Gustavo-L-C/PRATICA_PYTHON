#WARHAMMER 40K | SPACE MARINE 2 | CHAPTER SELECTOR RANDOM - 09.05.26

import random
from time import sleep
from chapters40k import lista_chapters_D
from chapters40k import lista_chapters
from bancodenomes import sim_sim

classe = ['Tatico🔫','Assalto🚀','Vanguarda🗡️','Baluarte🏳️','Sniper🎯','Pesado🛡️','Techmarine⚙️']
rc = random.choice(lista_chapters_D)

print('-'*60) #só enfeite

print('Seletor de Capitulo e Classe aleatorio para Space Marines 2\n')
r = input('Pronto? ')
print('')

qclasse = input(f'Quer uma classe aleatória? ')
print('')

if qclasse in sim_sim:
       classes = random.choice(classe)
       print(f'Classe aleatoria: {classes}.')

else:
    ec = input('Qual classe? ')
    print(f'\nClasse escolhida: {ec}')

print(f'Capitulo: {rc}')
sleep(2)

if rc == 'DeathWatch':
   print(rc)
   dw = input('Agora na DeathWatch, pronto para saber seu capitulo de origem? ')

   if dw in sim_sim:
    dc = random.choice(lista_chapters)
    print(f'Capitulo: {dc}')

   else:
    print(f'Então agora voce e um Black Shield da {rc}.')

print('-'*60) #só enfeite