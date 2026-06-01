from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador Google Chrome
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print("=== AUTOMAÇÃO INICIADA ===")
print("1. Escaneie o QR Code no navegador.")
print("2. Pressione ENTER aqui neste terminal APÓS suas conversas carregarem totalmente.")
input() # Pausa o script e aguarda você apertar ENTER no terminal

mensagem_automatica = "Olá! Recebemos sua mensagem. Em breve um de nossos representantes irá atendê-lo."

print("Monitorando novas mensagens...")

# Loop principal para manter o bot rodando continuamente
while True:
    try:
        # Busca todas as marcações verdes de mensagens não lidas na tela
        mensagens_nao_lidas = driver.find_elements(By.XPATH, "//span[contains(@aria-label, 'não lida')]")
        
        # O loop 'for' percorre cada uma das conversas não lidas encontradas
        for conversa in mensagens_nao_lidas:
            print("Nova mensagem detectada! Abrindo a conversa...")
            
            # Clica na bolinha verde para abrir o chat da pessoa
            conversa.click()
            time.sleep(2) # Aguarda 2 segundos para o chat carregar na tela
            
            # Localiza a caixa de texto onde digitamos as mensagens no WhatsApp
            caixa_de_texto = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
            
            # Escreve a mensagem definida lá em cima
            caixa_de_texto.send_keys(mensagem_automatica)
            time.sleep(1)
            
            # Aperta ENTER para enviar
            caixa_de_texto.send_keys(Keys.RETURN)
            print("Resposta automática enviada com sucesso!")
            time.sleep(2) 
            
            # Pressiona a tecla ESC para sair da conversa atual e voltar o foco pra lista
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            
    except Exception as e:
        # Se não encontrar nenhuma mensagem nova, ele cai aqui silenciosamente e tenta de novo
        pass
        
    # Aguarda 3 segundos antes de fazer uma nova varredura buscando novas mensagens
    time.sleep(3)