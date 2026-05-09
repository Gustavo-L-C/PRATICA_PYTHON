#09.05.26
# SLEEP

import time

#___________________________________________________________
def executar_com_delay(funcao, segundos, *args, **kwargs):
    time.sleep(segundos)
    return funcao(*args, **kwargs)
#___________________________________________________________

def funcao_um():
    print("Iniciando função um...")

def funcao_dois():
    print("Iniciando função dois...")

# Chamada das funções com delay
funcao_um()
time.sleep(2)  # Pausa por 2 segundos
funcao_dois()