# programa 9.20, cria um arquivo bmp a partir  do desenho 
import sys

# O desenho com o seu nome 'BRUNO' adaptado do passo anterior
desenho = [
    "  bbbbb   rrrr    u   u  n   n   oooo   ",
    "  b    b  r   r   u   u  nn  n  o    o  ",
    "  b    b  r   r   u   u  n n n  o    o  ",
    "  bbbbb   rrrr    u   u  n  nn  o    o  ",
    "  b    b  r r     u   u  n   n  o    o  ",
    "  b    b  r  r    u   u  n   n  o    o  ",
    "  bbbbb   r   r    uuu   n   n   oooo   "
]

def bytes_little_endian(numero, nbytes=4, sinal=False):
    """Converte um número inteiro para uma sequência de bytes (Little Endian)."""
    return numero.to_bytes(nbytes, "little", signed=sinal)

def padding(valor, tamanho=4):
    """Calcula o próximo múltiplo de 4 para o alinhamento de linhas do BMP."""
    if resto := valor % tamanho:
        return valor + tamanho - resto
    return valor

# Tabela de conversão de letras para cores no formato RGB
# Espaço " " vira preto, e as iniciais viram suas respectivas cores
letra_para_cor = {
    " ": (0, 0, 0),       # Preto
    "b": (0, 0, 255),     # Azul
    "r": (255, 0, 0),     # Vermelho
    "u": (0, 255, 255),   # Ciano
    "n": (255, 255, 0),   # Amarelo
    "o": (0, 255, 0)      # Verde
}

# Multiplicador de pontos: Cada caractere vira um bloco de 32x32 pixels para a imagem não ficar minúscula
multiplicador = 32

# Verifica se todas as linhas têm o mesmo tamanho
largura_desenho = len(desenho[0])
for linha, z in enumerate(desenho):
    if len(z) != largura_desenho:
        raise ValueError(f"As linhas do desenho precisam ter o mesmo tamanho! Linha incorreta: {linha}")

# Expandindo o desenho usando o multiplicador
desenho_expandido = []
for linha in desenho:
    nova_linha = []
    for letra in linha:
        nova_linha.append(letra * multiplicador)
    for _ in range(multiplicador):
        desenho_expandido.append("".join(nova_linha))

largura = len(desenho_expandido[0])
altura = len(desenho_expandido)

# Convertendo os caracteres em bytes de cores
dados_binarios = []
for linha in desenho_expandido:
    linha_binaria = []
    for caractere in linha:
        # Importante: O formato BMP armazena as cores invertidas -> BGR (Blue, Green, Red)
        linha_binaria.append(bytes(letra_para_cor[caractere][::-1]))
    dados_binarios.append(b"".join(linha_binaria))

# Adicionando o "Padding" (o formato BMP exige que cada linha de bytes seja múltipla de 4)
largura_bytes = largura * 3
largura_com_padding = padding(largura_bytes)
if largura_bytes != largura_com_padding:
    for p, d in enumerate(dados_binarios):
        dados_binarios[p] = b"".join([dados_binarios[p], bytes(largura_com_padding - largura_bytes)])

# Calcula o tamanho final da área de dados da imagem
tamanho_pixels = padding(largura * 3) * altura

# Montagem do Cabeçalho BMP (File Header - 14 bytes)
cabecalho_bmp = [
    b"BM",                                    # Assinatura do arquivo
    bytes_little_endian(54 + tamanho_pixels), # Tamanho total do arquivo (bytes)
    bytes(4),                                 # Reservado (zeros)
    bytes_little_endian(54)                   # Onde começam os dados dos pixels (offset)
]

# Montagem do Cabeçalho DIB (Image Header - 40 bytes)
cabecalho_dib = [
    bytes_little_endian(40),                  # Tamanho deste cabeçalho
    bytes_little_endian(largura),             # Largura da imagem
    bytes_little_endian(-altura, sinal=True), # Altura negativa (escreve de cima para baixo)
    bytes_little_endian(1, 2),                # Quantidade de planos (sempre 1)
    bytes_little_endian(24, 2),               # Bits por pixel (24 bits = Cores Reais)
    bytes_little_endian(0),                   # Compressão (0 = Nenhuma)
    bytes_little_endian(tamanho_pixels),      # Tamanho dos dados de pixel
    bytes_little_endian(2835),                # Resolução Horizontal
    bytes_little_endian(2835),                # Resolução Vertical
    bytes_little_endian(0),                   # Cores na paleta
    bytes_little_endian(0)                    # Cores importantes
]

# Gravando tudo no arquivo final imagem.bmp
nome_arquivo = "nome_bruno.bmp"
with open(sys.argv[1], "wb") as f:
    f.write(b"".join(cabecalho_bmp))
    f.write(b"".join(cabecalho_dib))
    for linha in dados_binarios:
        f.write(linha)

print(f"Sucesso! Arquivo '{nome_arquivo}' gerado com tamanho {largura}x{altura} pixels.")