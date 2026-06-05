import os
import shutil

def organizar_pasta(caminho):
    # Garante que o caminho está correto para o Python
    caminho = os.path.abspath(caminho)
    
    if not os.path.exists(caminho):
        return f"Erro: A pasta '{caminho}' não existe!"
        
    arquivos_movidos = 0
    
    # Mapeamento de pastas genéricas para testar
    extensoes = {
        "Documentos": [".txt", ".pdf", ".docx", ".doc", ".xlsx", ".pptx"],
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Outros": [] # Tudo que não encaixar vai para cá
    }

    # Anda por tudo que está dentro da pasta
    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)
        
        # Ignora se for uma pasta (só queremos mover arquivos soltos)
        if os.path.isdir(caminho_completo):
            continue
            
        # Pega a extensão do arquivo (ex: .txt)
        nome_arquivo, extensao = os.path.splitext(item)
        extensao = extensao.lower()
        
        # Define para qual pasta o arquivo vai
        pasta_destino = "Outros"
        for nome_pasta, lista_extensoes in extensoes.items():
            if extensao in lista_extensoes:
                pasta_destino = nome_pasta
                break
                
        # Cria a subpasta (ex: Documentos) se ela não existir
        caminho_pasta_destino = os.path.join(caminho, pasta_destino)
        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            
        # Move o arquivo para dentro da subpasta
        shutil.move(caminho_completo, os.path.join(caminho_pasta_destino, item))
        arquivos_movidos += 1

    return f"Sucesso! {arquivos_movidos} arquivos foram organizados."

if __name__ == "__main__":
    # Caminho direto e sem erros para a sua pasta na Área de Trabalho
    pasta_para_testar = r"C:\Users\Dell\Desktop\Cursos Tech\testes-bagunça"
    
    # Força a criação da pasta caso ela tenha sumido
    if not os.path.exists(pasta_para_testar):
        os.makedirs(pasta_para_testar)
        
    resultado = organizar_pasta(pasta_para_testar)
    print(resultado)
    input("Aperte ENTER para fechar...")