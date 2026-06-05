# geração de uma pagfina web a partir de um dicionario
filmes = {
'drama':['cidadão kane', 'o poderoso chefão'],
'comedia':['tempos mordenos', 'american pie','dr. dolittle'] ,
'policial':['chuva negra', 'desejo de matar', 'dificial de matar'],
'guerra': ['rambo', 'platoon', 'tora tora tora']          
}

with open('filmes.html', 'w', encoding='utf-8') as pagina:
    pagina.write("""
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Primeira Página</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
    </style>
</head>
<body> """)
    for c, v in filmes.items():
        pagina.write(f'<h1>{c}</h1>\n')
        for e in v:
            pagina.write(f'<h2>{e}</h2>\n')
    pagina.write(f'</body></html>')            










        