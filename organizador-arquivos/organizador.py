import os
import shutil

# 1. Defina o caminho da pasta que está bagunçada (ex: sua pasta de Downloads)
# Nota: Ajuste o caminho abaixo para o seu computador
pasta_alvo = os.path.expanduser("~/Downloads")

# 2. Defina os tipos de arquivos e suas respectivas pastas de destino
extensoes = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}

# 3. Função principal que organiza os arquivos
def organizar_pasta():
    if not os.path.exists(pasta_alvo):
        print("Pasta não encontrada.")
        return

    # Passa por cada arquivo da pasta
    for arquivo in os.listdir(pasta_alvo):
        caminho_completo = os.path.join(pasta_alvo, arquivo)
        
        # Ignora se for uma pasta em vez de um arquivo
        if os.path.isdir(caminho_completo):
            continue
            
        # Pega a extensão do arquivo (ex: .pdf)
        _, extensao = os.path.splitext(arquivo)
        
        # Procura a pasta correta para a extensão
        movido = False
        for pasta_destino, lista_extensoes in extensoes.items():
            if extensao.lower() in lista_extensoes:
                # Cria a pasta de destino se ela não existir
                nova_pasta = os.path.join(pasta_alvo, pasta_destino)
                os.makedirs(nova_pasta, exist_ok=True)
                
                # Move o arquivo
                shutil.move(caminho_completo, os.path.join(nova_pasta, arquivo))
                print(f"Movido: {arquivo} -> Pasta {pasta_destino}")
                movido = True
                break
                
        if not movido:
            print(f"Ignorado (sem regra definida): {arquivo}")

if __name__ == "__main__":
    print("Iniciando a organização da pasta...")
    organizar_pasta()
    print("Organização concluída!")
