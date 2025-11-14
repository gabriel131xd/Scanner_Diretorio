# Scanner de Diretórios HTTP(S)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Security](https://img.shields.io/badge/Security-Ethical%20Use%20Required-red)



Este projeto é um **scanner de diretórios e arquivos** desenvolvido em Python.  
Ele utiliza requisições HTTP(S) para tentar localizar caminhos expostos, sensíveis ou potencialmente vulneráveis dentro de uma aplicação web.

O objetivo principal é **aprendizado**, **estudo de segurança** e **auditoria em ambientes autorizados**.

---

## 🗣 Apresentação do código

Olá, pessoal!  
Este código. Ele é basicamente um **código de varredura** que utiliza a biblioteca `requests` para buscar diretórios e arquivos que possam estar expostos ou vulneráveis a algum tipo de ataque.

Ele foi desenvolvido em **Python** e precisa de uma **wordlist** (`.txt`) para funcionar, pois é a partir dessa lista que o script monta e testa os caminhos na aplicação. Existem outros métodos para fazer essa descoberta de forma mais automática, sem depender de wordlist, mas, para permanecer no **modo ético e controlado**, optei por usar apenas uma wordlist simples.

A ideia é utilizar esse código em **auditorias autorizadas**, estudos e laboratórios de segurança — nunca para atacar sistemas de terceiros sem permissão.

---

## 📌 Como o script funciona

- Lê uma **wordlist** contendo caminhos comuns (por exemplo: `admin/`, `login/`, `.env`, `backup.zip`, etc.).
- Faz requisições HTTP/HTTPS para cada caminho, combinando a URL base com os itens da wordlist.
- Considera como relevantes respostas HTTP como:
  - `200` – OK (recurso existe),
  - `301` / `302` – redirecionamento (recurso existe, mas move/redireciona),
  - `403` – proibido (acesso negado, mas o recurso geralmente existe).
- Utiliza **múltiplas threads** para acelerar o processo de varredura.
- Exibe no terminal apenas os caminhos que retornarem um desses status.

---

## 🔧 Instalação das dependências

Este projeto utiliza a biblioteca `requests`.

Para instalar as dependências, execute:

```bash
pip install requests
