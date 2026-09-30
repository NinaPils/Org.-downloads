import os
import shutil

# 1. FUNÇÃO AUXILIAR: Move o arquivo para a pasta correta
def mover_arquivo(caminho_origem, pasta_alvo, nome_pasta_destino, nome_arquivo):
    # Define o caminho final da pasta separando os arquivos por categoria
    caminho_destino = os.path.join(pasta_alvo, nome_pasta_destino)
    
    # Cria a pasta de destino se ela não existir
    os.makedirs(caminho_destino, exist_ok=True)
    
    # Move o arquivo para a pasta de destino
    shutil.move(caminho_origem, os.path.join(caminho_destino, nome_arquivo))
    print(f"✅ Arquivo '{nome_arquivo}' movido para a pasta '{nome_pasta_destino}'.")

# 2. FUNÇÃO PRINCIPAL: Organiza a pasta alvo
def organizar_arquivos(downloads):
    PASTA_ALVO = downloads
    
    # Confirmação com enter 
    input("Pressione Enter para iniciar a organização dos arquivos...")
    
    # Listar tudo que tem dentro da pasta alvo
    itens = os.listdir(PASTA_ALVO)
    PASTA_ALVO = downloads

    # Define as regras de organização
    REGRAS_ORGANIZACAO = {
        'Arquivos_de_Video': ['.mp4', '.avi', '.mov', '.mkv'],
        'Arquivos_de_Imagem': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Arquivos_Texto': ['.txt', '.md'],
        'Arquivos_Compactados': ['.zip', '.rar', '.7z'],
        'Pastas_de_Documentos': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Aplicativos': ['.exe', '.msi', '.bat', '.sh']
    }
    PASTA_OUTROS = 'Outros_Arquivos'

    # Laço para passar por cada item da pasta
    for item in itens:
        caminho_completo = os.path.join(PASTA_ALVO, item)
        
        # Ignora se for uma pasta, queremos apenas arquivos
        if os.path.isdir(caminho_completo):
            continue
            
        # Pega a extensão do arquivo em letras minúsculas (.jpg, .mp4, etc.)
        _, extensao = os.path.splitext(item)
        extensao = extensao.lower()
        
        foi_organizado = False
        
        # Verifica em qual regra a extensão se encaixa
        for pasta_destino, extensoes_validas in REGRAS_ORGANIZACAO.items():
            if extensao in extensoes_validas:
                mover_arquivo(caminho_completo, PASTA_ALVO, pasta_destino, item)
                foi_organizado = True
                break
        
        # Se não se encaixou em nenhuma regra, vai para "Outros"
        if not foi_organizado:
            mover_arquivo(caminho_completo, PASTA_ALVO, PASTA_OUTROS, item)

    print("Organização concluída com sucesso!")

# 3. EXECUÇÃO DO CÓDIGO
# Substitua o caminho abaixo pela pasta que você quer organizar
caminho_da_pasta = r"C:\Users\Pichau\Downloads" 
organizar_arquivos(caminho_da_pasta)
