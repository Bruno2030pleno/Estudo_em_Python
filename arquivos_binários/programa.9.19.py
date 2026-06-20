# programa 9.19, criando uma imagem em formato bynario
imagem = """
 42 4d
 46 00 00 00
 00 00 
 00 00
 36 00 00 00
 28 00 00 00
 02 00 00 00
 02 00 00 00
 01 00
 18 00
 00 00 00 00
 10 00 00 00
 13 0b 00 00
 13 0b 00 00
 00 00 00 00 
 00 00 00 00
 00 00 ff
 ff ff ff
 00 00
 ff 00 00
 00 ff 00 
 00 00

"""

imagem = bytes.fromhex(imagem)
with open('imagem.bmp', 'wb') as f:
    f.write(imagem)