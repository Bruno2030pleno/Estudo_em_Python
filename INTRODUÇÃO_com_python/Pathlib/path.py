import pathlib as path

# caminho = path.Path('c:\\user\\')
# print(caminho)
# caminho_pai = caminho / 'pai'
# print(caminho_pai)

# caminho = path.Path('/home/brunodev/Estudo_em_Python/MEUS_PROGRAMAS/leitura.py')
# print(caminho.suffix)
caminho = 'nova_lista.txt'
with path.Path(caminho).open() as f:
    print(f.read())