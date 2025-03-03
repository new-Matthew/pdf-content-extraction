import os
import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

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

def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'{filename}_{page_num+1}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)
            print(f'PDF criado com o nome: {new_filename}')

def split_pdf_page(pdf_path, start_page:int=0, stop_page:int=0):
    with(open(pdf_path, 'rb')) as file:
        reader = PdfReader(file)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'{filename}_from_{start_page+1}_to_{stop_page+1}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)
def fetch_all_pdf_files(parent_folder:str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith('.pdf'):
                target_files.append(os.path.join(path, name))
        return target_files

def merge_pdf(list_pdfs, output_filename='final_pdf.pdf'):
    merger = PdfMerger()
    with open(output_filename, 'wb') as f:
        for file in list_pdfs:
            print(file)
            merger.append(file)
        merger.write(f)

pdf_list = fetch_all_pdf_files(path)
merge_pdf(pdf_list)

#print(*fetch_all_pdf_files(path), sep='\n')
# print(split_pdf_page(file_path, 1, 2))
# print(split_pdf(file_path))
# print(get_pdf_metadata(file_path))
# print(extract_text_from_pdf(file_path))
