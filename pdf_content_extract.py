import os
import PyPDF2 as pdf
from PyPDF2 import PdfReader

base_path = os.path.expanduser('~')
path = os.path.join(base_path, 'Desktop', 'Estacio-2025.1','desenvolvimento_rapido_de_aplicacoes_em_python', 'concluido')

file_path = os.path.join(path, 'tema-3-manipulacao_de_dados_em_arquivos.pdf')

def get_pdf_metadata(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            info = reader.metadata
            return info

    else:
        print(f"O Arquivo {pdf_path} não encontrado.")

def extract_text_from_pdf(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            results = []
            for i in range(0, len(reader.pages)):
                selected_page = reader.pages[i]
                text = selected_page.extract_text()
                results.append(text)
            return ' '.join(results)


print(get_pdf_metadata(file_path))
print(extract_text_from_pdf(file_path))