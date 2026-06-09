# arvore de diretorios sendo percorrida
import os
import sys

for raiz, diretorios, arquivo in os.walk(sys.argv[1]):
    print('\ncaminhos:', raiz)
    for d in diretorios:
        print(f' {d}/')
    for f in arquivo:
        print(f' {f}/')
    print(f'{len(diretorios)} diretorios(s), {len(arquivo)}, arquivos(s)') 

