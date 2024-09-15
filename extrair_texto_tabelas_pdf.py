
"""
Script para extração de texto e tabelas de um arquivo PDF usando a biblioteca pdfplumber.

Versão: 1.97
Autor: Prof. Sauer
Email: sauer@simplificatreinamentos.com.br
Instagram: https://www.instagram.com/prof.alesauer/
Facebook: https://www.facebook.com/prof.alesauer/
YouTube:  https://www.youtube.com/@prof.alesauer
LinkedIn: www.linkedin.com/in/alesauer
Site: www.sauer.pro.br
"""

import pdfplumber

def extrair_texto(pdf_path):
    """
    Extrai todo o texto de um arquivo PDF.
    
    Parâmetro:
    pdf_path (str): Caminho do arquivo PDF.
    
    Retorna:
    str: Texto extraído do PDF.
    """
    with pdfplumber.open(pdf_path) as pdf:
        texto_completo = ''
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
        return texto_completo

def extrair_tabelas(pdf_path):
    """
    Extrai todas as tabelas de um arquivo PDF.
    
    Parâmetro:
    pdf_path (str): Caminho do arquivo PDF.
    
    Retorna:
    list: Lista de tabelas extraídas, onde cada tabela é representada como uma lista de listas.
    """
    with pdfplumber.open(pdf_path) as pdf:
        tabelas = []
        for pagina in pdf.pages:
            tabelas += pagina.extract_tables()
        return tabelas

if __name__ == "__main__":
    # Definindo o caminho do arquivo PDF
    caminho_pdf = "seu_arquivo.pdf"
    
    # Extraindo e exibindo o texto do PDF
    texto = extrair_texto(caminho_pdf)
    print("Texto extraído do PDF:")
    print(texto)

    # Extraindo e exibindo as tabelas do PDF
    tabelas = extrair_tabelas(caminho_pdf)
    print("\nTabelas extraídas do PDF:")
    for tabela in tabelas:
        for linha in tabela:
            print(linha)
