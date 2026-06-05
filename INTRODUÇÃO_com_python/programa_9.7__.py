# criação de uma pagina inicial em python
# with open('pagina.html', 'w', encoding='utf-8') as pagina:
#     pagina.write('<!DOCTYPE html>\n')
#     pagina.write('<html lang="pt-BR">\n')
#     pagina.write('head> <meta charset="UTF-8">\n')
#     pagina.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
#     pagina.write('<title>Minha Primeira Página</title>\n')
#     pagina.write('<style> body { font-family: Arial, sans-serif; padding: 20px;}</style></head>\n')
#     pagina.write('<body><h1>Página Padrão HTML5</h1><p>Esta é uma estrutura básica e limpa pronta para você começar a desenvolver.</p></body>/html>\n')
#     for linha in range(10):
#         pagina.write(f'<p>{linha}<p>')
#     pagina.write('<body>\n')
#     pagina.write('<html>\n')    

with open('pagina.html', 'w', encoding='utf-8') as pagina:
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
    for linha in range(10):
        pagina.write(f'<p>{linha}</p>')
    pagina.write("""              
</body>

</html>""")

   