import os
import PyPDF2 as pdf
from PyPDF2 import PdfReader

base_path = os.path.expanduser('~')
path = os.path.join(base_path, 'Desktop', 'Estacio-2025.1','desenvolvimento_rapido_de_aplicacoes_em_python', 'concluido')

file_path = os.path.join(path, 'tema-3-manipulacao_de_dados_em_arquivos.pdf')

if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        print(reader)
        info = reader.metadata
        print(info.title)
        print(info.author)
        print(info.creator)
        print(info.subject)
        print(len(reader.pages))
        print(reader.pages[10].extract_text())

else:
    print(f"O Arquivo {file_path} não encontrado.")

print(reader.pages[0].extract_text())