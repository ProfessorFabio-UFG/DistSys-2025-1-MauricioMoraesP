# 📨 Sistema Publisher-Subscriber com ZeroMQ (Python)

Este projeto implementa um sistema **Publisher/Subscriber** utilizando a biblioteca **ZeroMQ (PyZMQ)** com interface interativa via prompt.

Permite:
- Envio de mensagens para múltiplos tópicos.
- Assinatura dinâmica de tópicos.
- Comunicação entre processos ou máquinas via TCP.

---

## 📁 Estrutura do Projeto

```
DistSys-2025-1-MauricioMoraesP/
├── constPS.py              # Arquivo com as constantes de IP e porta
├── publisher_interactive.py  # Publicador interativo
├── subscriber_interactive.py # Assinante interativo
└── README.md               # Este arquivo
```

---
#### Instale com:

```bash
pip install pyzmq
```
---

## ▶️ Como Executar

#### 1. Abra dois terminais de máquinas distintas na aws.

#### 🧑‍💻 Terminal 1 - Rodar o Subscriber

```bash
python3 subscriber_interactive.py
```

Você verá:

```
=== Subscriber Iniciado ===
Digite tópicos para assinar (ex: TIME, ALERTA).
Digite 'start' para começar a escutar mensagens.
```

- Digite os nomes dos tópicos que deseja assinar (ex: `ALERTA`, `TIME`).
- Depois digite `start` para começar a receber mensagens.

---

#### 📢 Terminal 2 - Rodar o Publisher

```bash
python3 publisher_interactive.py
```

Você verá:

```
=== Publisher Iniciado ===
Digite mensagens no formato: <TOPICO> <MENSAGEM>
Exemplo: ALERTA Sistema será reiniciado
Digite 'sair' para encerrar.
```

- Envie mensagens no formato:
  ```bash
  ALERTA Teste do sistema
  ```

- O subscriber que assinou `ALERTA` receberá:
  ```
  ALERTA [12:34:56] Teste do sistema
  ```

---