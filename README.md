# 📂 Organizador Automático de Pastas (Python)

Este é um script em Python desenvolvido para resolver um problema muito comum do dia a dia: a bagunça nas pastas do computador (como a pasta de Downloads ou Área de Trabalho). 

O programa analisa a pasta indicada, identifica as extensões dos arquivos soltos e os move automaticamente para subpastas organizadas de acordo com a sua categoria (Imagens, Documentos, Vídeos, etc.).

## 🚀 Funcionalidades
- **Organização Inteligente:** Separa arquivos por tipo de forma automática.
- **Tratamento de Erros:** Ignora pastas já existentes para não gerar duplicidade.
- **Segurança de Caminhos:** Configurado para ler caminhos do Windows sem quebrar a execução do código.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- Biblioteca nativa `os` (para manipulação de caminhos e pastas)
- Biblioteca nativa `shutil` (para movimentação segura de arquivos)

## 💻 Como usar
1. Insira o caminho da pasta que deseja organizar na variável `pasta_para_testar`.
2. Execute o arquivo `organizador.py`.
3. Os arquivos soltos serão movidos para as suas respectivas pastas e o terminal exibirá a contagem de sucesso.
