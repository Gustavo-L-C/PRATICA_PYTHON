#WARHAMMER 40K CHAPTER SELECTOR RANDOM

import random
from chapters40k import lista_chapters_D
from chapters40k import lista_chapters
from bancodenomes import sim_sim
#from bancodenomes import nao_nao

print('Seletor de Capitulo aleatorio para Space Marines 2\n')
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