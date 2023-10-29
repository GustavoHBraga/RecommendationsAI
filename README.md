# 🧬📊🛒 Projeto de Recomendações com IA Generativa 
Este projeto consiste em uma aplicação que utiliza IA generativa para enviar recomendações de produtos com base nos perfis de compra de cada cliente

<br>

## 📃 Descrição dos Diretórios:
<ul>  <b>config/:</b> Contém as configurações para o envio de e-mails (EmailConfig.py) e a configuração da API OpenAI (OpenAIConfig.py).</ul>

<ul> <b>exceptionHandler/:</b> Lida com exceções específicas da OpenAI (openai_exceptions.py).</ul>

<ul> <b>utils/:</b> Contém utilitários para análise de dados e manipulação de arquivos (AnalysisAI.py e FileManipulation.py).</ul>

<ul> <b>app-multiprocessing.py:</b> Script principal que coordena a análise e envio de e-mails para os clientes.</ul>

<br>


# 📋 Configuração e Execução:

### Pré-requisitos:

<ul>Python 3.x</ul>
<ul>Bibliotecas Python (instaláveis via pip): smtplib, email, dotenv, openai, tiktoken</ul>

<br>

### Configuração do Ambiente:

<p>1. Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis:</p>

```bash
  STMP_EMAIL_LOGIN=seu_email@gmail.com
  STMP_EMAIL_PASSWORD=sua_senha
  OPENAI_API_KEY=sua_api_key
  STMP_EMAIL_TO=destinatario@example.com
```
<p>Use o <b>https://temp-mail.org/en/</b> para criar um E-mail aleátorio para enviar as recomendações</p>

![image](https://github.com/GustavoHBraga/RecommendationsAI/assets/70377322/b11e1eeb-bace-4a63-a39d-1fd4c0c15b87)
<br>
![image](https://github.com/GustavoHBraga/RecommendationsAI/assets/70377322/c1142e7a-30b9-4441-8852-991c7a833f06)

<br>


# ✅Execução
<p>1. Execute o codigo abaixo:</p>

```bash
  python app-multiprocessing.py
```

<br>


# Detalhes sobre os Componentes:

<ul>  <b>EmailConfig.py:</b>: Gerencia o envio de e-mails utilizando a biblioteca smtplib.</ul>
<ul>  <b>OpenAIConfig.py:</b>: Configura a comunicação com a API OpenAI para a geração de recomendações.</ul>
<ul>  <b>AnalysisAI.py:</b>: Contém funções para análise de perfis de compra, recomendações e geração de e-mails.</ul>
<ul>  <b>FileManipulation.py</b>: Utilitário para leitura e escrita de arquivos.</ul>
<ul>  <b>app-multiprocessing.py</b>b> Coordena o processo de análise e envio de e-mails utilizando multiprocessamento.</ul>
