# Python Security Labs — Keylogger & Ransomware

Laboratório educacional desenvolvido em Python para explorar conceitos de cibersegurança, incluindo eventos de teclado, comunicação SMTP, criptografia simétrica e recuperação de arquivos.

O projeto tem como objetivo compreender o funcionamento de técnicas associadas a ameaças cibernéticas e estudar seus riscos sob uma perspectiva técnica e defensiva.

> **Aviso de segurança:** Este projeto destina-se exclusivamente a estudos em ambientes controlados e autorizados. Utilize apenas dados fictícios, contas de teste e arquivos descartáveis. Nunca colete informações de terceiros nem execute testes em arquivos ou sistemas sem autorização.

## 📁 Estrutura do projeto

```text
python-security-labs/
├── Keylogger/
│   ├── keylogger.py
│   └── keylogger_send_email.py
├── ransomware/
│   ├── test_files/
│   ├── encrypt.py
│   └── decrypt.py
└── README.md
```

## 🎯 Objetivos

- Estudar o tratamento de eventos de teclado em Python.
- Compreender os fundamentos do protocolo SMTP e do envio de e-mails.
- Explorar a criptografia simétrica utilizando a biblioteca Fernet.
- Entender os processos de criptografia e descriptografia de arquivos.
- Identificar comportamentos que podem indicar atividades maliciosas.
- Desenvolver conhecimentos aplicáveis à análise de ameaças e à defesa cibernética.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Linguagem de programação |
| `pynput` | Tratamento de eventos de teclado |
| `smtplib` | Comunicação com servidores SMTP |
| `email.mime.text` | Construção de mensagens de e-mail |
| `threading.Timer` | Agendamento de tarefas |
| `cryptography.fernet` | Criptografia e descriptografia simétrica |
| `os` | Manipulação e navegação por diretórios e arquivos |

## 🔬 Laboratórios

### 1. Keylogger — Registro de eventos de teclado

**Diretório:** `Keylogger/`

**Arquivo:** `keylogger.py`

Laboratório dedicado ao estudo do tratamento de eventos de teclado e à manipulação de dados em aplicações Python.

**Conceitos abordados:**
- Eventos de pressionamento de teclas.
- Tratamento de teclas especiais.
- Manipulação de arquivos de texto.
- Tratamento de exceções.
- Riscos de exposição de informações sensíveis.

### 2. Keylogger — Comunicação SMTP

**Arquivo:** `keylogger_send_email.py`

Explora conceitos relacionados à comunicação por e-mail e à integração entre componentes de uma aplicação Python.

**Conceitos abordados:**
- Protocolo SMTP.
- Autenticação em servidores de e-mail.
- Construção de mensagens MIME.
- Agendamento de tarefas.
- Tratamento de falhas de comunicação.
- Riscos de exfiltração de informações.

Os testes de comunicação devem utilizar mensagens sintéticas e uma conta de laboratório, sem transmitir registros reais de teclado ou dados confidenciais.

### 3. Ransomware — Criptografia de arquivos

**Diretório:** `ransomware/`

**Arquivo:** `encrypt.py`

Laboratório que explora os fundamentos da criptografia simétrica aplicada a arquivos de teste.

**Conceitos abordados:**
- Geração e armazenamento de chaves criptográficas.
- Uso da biblioteca Fernet.
- Leitura e gravação de arquivos binários.
- Manipulação de diretórios.
- Impactos da criptografia na disponibilidade dos dados.

Os testes devem permanecer restritos à pasta `ransomware/test_files/`, utilizando arquivos descartáveis e cópias de segurança.

### 4. Ransomware — Descriptografia e recuperação

**Arquivo:** `decrypt.py`

Estudo do processo de recuperação de arquivos criptografados por meio da chave correspondente.

**Conceitos abordados:**
- Carregamento de chaves criptográficas.
- Descriptografia com Fernet.
- Tratamento de arquivos binários.
- Integridade e recuperação dos dados.
- Importância do armazenamento seguro de chaves e backups.

A recuperação deve ser testada exclusivamente com arquivos produzidos pelo laboratório. A perda da chave necessária pode impedir a recuperação dos dados.

## ⚙️ Preparação do ambiente

### Pré-requisitos

- Python 3 instalado.
- `pip` disponível.
- Ambiente de testes isolado e autorizado.

### Instalação das dependências

No terminal, instale as bibliotecas utilizadas pelos laboratórios:

```bash
pip install pynput cryptography
```

As bibliotecas `smtplib`, `email.mime.text`, `threading` e `os` fazem parte da biblioteca padrão do Python.

**Observação:** a instalação das dependências não configura automaticamente um servidor SMTP nem suas credenciais. Essa configuração depende do ambiente de teste utilizado.

## 🛡️ Boas práticas de segurança

- Executar os testes em uma máquina virtual ou ambiente isolado.
- Utilizar somente dados fictícios e arquivos descartáveis.
- Não armazenar senhas, tokens ou chaves reais no repositório.
- Não coletar nem transmitir informações de terceiros.
- Manter backups dos arquivos utilizados nos testes.
- Restringir qualquer operação de criptografia ao diretório de laboratório.
- Preservar as chaves necessárias para a recuperação dos arquivos.
- Analisar os comportamentos observados sob uma perspectiva defensiva.

## 📚 Aprendizados

Este projeto permite explorar conceitos de programação Python relacionados a eventos de teclado, protocolos de e-mail, criptografia simétrica e manipulação de arquivos, além de discutir riscos associados a comportamentos comuns em ameaças cibernéticas.

A perspectiva defensiva inclui reconhecer indicadores de atividade suspeita, analisar conexões SMTP inesperadas, monitorar processos que acessam arquivos em grande volume e compreender a importância de backups e controles de acesso.

## 🎓 Finalidade

Projeto de estudo e portfólio em cibersegurança, com foco na compreensão técnica de comportamentos de ameaça, no uso responsável de ferramentas e na conscientização sobre medidas defensivas.
