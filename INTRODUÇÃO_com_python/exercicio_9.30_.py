# modifique o programa 9.8 para gerar uma lista html, usando
# os elementos ul e li. todos os elementos da lista devem estar dentro do elemento ul.
#  e cada item dentro de  um elemento li exemplo
# <ul><li>item</li>item2</li>item3</li>item4></li>



filmes = {
'drama':['cidadão kane', 'o poderoso chefão'],
'comedia':['tempos mordenos', 'american pie','dr. dolittle'] ,
'policial':['chuva negra', 'desejo de matar', 'dificial de matar'],
'guerra': ['rambo', 'platoon', 'tora tora tora']          
}

with open('filmes_lista.html', 'w', encoding='utf-8') as pagina:
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
        pagina.write('<ul>\n')
        for e in v:
            pagina.write(f'<li>{e}</li>\n')
        pagina.write('</ul>\n')
    pagina.write('</body>\n</html>')
               