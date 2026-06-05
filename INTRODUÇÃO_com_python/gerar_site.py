import webbrowser

# 1. Código HTML super simples
codigo_html = "<h1>Olá Bruno!</h1><p>Versão simplificada funcionando!</p>"

# 2. Cria e escreve o arquivo HTML
with open("site_simples.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(codigo_html)

# 3. Abre diretamente no seu navegador padrão
webbrowser.open("site_simples.html")
print("Sucesso! O site simples foi gerado e aberto.")
