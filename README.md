# Whatsapp Message Bot

## Conteúdo

- [Sobre](#sobre)
- [Iniciando](#iniciando)
- [Uso](#uso)
- [Árvore do Projeto](#arvore)

## Sobre <a name = "sobre"></a>

Projeto desenvolvido em Python por mim para automatizar o envio de mensagens para os alunos do Projeto Edutech informando-os que os cursos estavam liberados e sobre os acessos deles no curso e no Google Classroom do curso no Estado do Paraná.

## Iniciando <a name = "iniciando"></a>

Instruções do projeto para funcionar em sua máquina local para fins de desenvolvimento e teste.

### Pré requisitos

Python 3 instalado com as bibliotecas localizadas no arquivo requirements.txt.
Arquivo excel com as seguintes colunas nele:
```
- Telefone
- Mensagem
```

Whtasapp instalado e rodando no telefone para poder fazer a sincronia no whatsapp web
Acesso a internet durante todo o procedimento

### Modo de uso

Executar o arquivo python (ou o arquivo do Jupyter Notebook) na sua IDE de preferência, deixando a planilha na mesma pasta do projeto para que o pandas possa lê-la.
    - O projeto irá abrir uma página web do Whatsapp para sincronizar o seu telefone com o Whatsapp web.
    - Assim que abrir o Whatsapp web ele irá começar a mandar mensagens de forma automática conforme contados indicados na planilha. As mensagens são enviadas a cada 15 segundos.
    - Fique de olho na página para eventuais erros, pois, como o whatsapp depende da conexão da internet, pode ocorrer um erro de execução e o processo ser reiniciado.


## Uso <a name = "uso"></a>

O uso dele foi apenas para facilitar o envio de mensagens para mais de 300 alunos da rede estadual de educação para informar sobre o início das aulas do projeto Edutech.

## Árvore do Projeto <a name = "arvore"></a>

```
WhatsApp_Bot_Message
├─ .gitignore
├─ app.ipynb
├─ app.py
├─ contatos.xlsx
├─ README.md
└─ requirements.txt

```