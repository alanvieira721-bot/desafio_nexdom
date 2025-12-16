import os
import requests

# Função para baixar arquivos CSV
def baixar_arquivo(url, pasta_destino):
    # Obter o nome do arquivo a partir da URL
    nome_arquivo = url.split("/")[-1]
    
    # Criar a pasta destino se ela não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Caminho completo para salvar o arquivo
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
    
    # Fazer o download do arquivo
    resposta = requests.get(url)
    
    # Verificar se o download foi bem-sucedido
    if resposta.status_code == 200:
        # Sobrescrever o arquivo se já existir
        with open(caminho_arquivo, 'wb') as f:
            f.write(resposta.content)
        print(f"Arquivo {nome_arquivo} baixado e sobrescrito com sucesso!")
    else:
        print(f"Falha ao baixar o arquivo {nome_arquivo}. Status Code: {resposta.status_code}")

# Links para os arquivos CSV
links = [
    'https://dadosabertos.ans.gov.br/FTP/PDA/taxa_de_resolutividade/pda-048-taxa_de_resolutividade.csv',
    'https://dadosabertos.ans.gov.br/FTP/PDA/IGR/IGR_versao_2023/IGR.csv',
    'https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv'
]

# Caminho da pasta onde os arquivos serão salvos
pasta_destino = r'C:\Users\Ryzen 9\Desktop\Alan\NEXDOM\Fontes\Fontes Brutas'

# Baixar todos os arquivos
for link in links:
    baixar_arquivo(link, pasta_destino)
