PDF Content Extraction

Este projeto tem como objetivo a extração de conteúdo de arquivos PDF para manipulação posterior.

Configuração do Caminho

Defina o caminho até a pasta que contém o PDF a ser manipulado:

import os

base_path = os.path.expanduser('~') é a mesma coisa que "C:\\Users\\SeuUsuario"
path = os.path.join(base_path, 'Desktop', 'caminho', 'até', 'diretório', 'do', 'pdf')

Definição do Arquivo

Especifique o nome do arquivo PDF a ser manipulado:

file_path = os.path.join(path, 'arquivo-a-ser-manipulado')

Agora, o sistema estará pronto para processar o arquivo PDF conforme sua necessidade.