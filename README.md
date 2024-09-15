
# 📝 Extração de Texto e Tabelas de PDF com pdfplumber

Este repositório contém exemplos de como utilizar a biblioteca `pdfplumber` para extrair textos e tabelas de arquivos PDF.

## 📌 Conteúdo

1. [Instalação](#instalacao)
2. [Extração de Texto](#extracao-de-texto)
3. [Extração de Tabelas](#extracao-de-tabelas)
4. [Conclusão](#conclusao)

## 📥 Instalação

Para utilizar o script, primeiro instale a biblioteca `pdfplumber`:

```bash
pip install pdfplumber
```

## 💡 Extração de Texto

O script permite extrair o texto de um arquivo PDF, página por página. Isso é útil quando você precisa fazer uma análise textual ou simplesmente recuperar informações do documento.

```python
import pdfplumber

def extrair_texto(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto_completo = ''
        for pagina in pdf.pages:
            texto_completo += pagina.extract_text()
        return texto_completo
```

## 💡 Extração de Tabelas

Além de texto, também podemos extrair tabelas, que são detectadas automaticamente no PDF. Isso é muito útil para processar relatórios, faturas, ou qualquer PDF que contenha dados tabulares.

```python
def extrair_tabelas(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tabelas = []
        for pagina in pdf.pages:
            tabelas += pagina.extract_tables()
        return tabelas
```

## 🏁 Conclusão

A biblioteca `pdfplumber` é uma excelente ferramenta para quem precisa trabalhar com arquivos PDF de forma programática, especialmente para extração de texto e tabelas. Dependendo da complexidade do arquivo PDF, algumas manipulações adicionais podem ser necessárias, mas a biblioteca facilita muito o processo.
