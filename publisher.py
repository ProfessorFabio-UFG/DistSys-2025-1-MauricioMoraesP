import zmq
from constPS import *
from datetime import datetime

context = zmq.Context()
s = context.socket(zmq.PUB)
p = f"tcp://{HOST}:{PORT}"
s.bind(p)

print("=== Publisher Iniciado ===")
print("Digite mensagens no formato: <TOPICO> <MENSAGEM>")
print("Exemplo: ALERTA Sistema será reiniciado")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Publicar> ")

    if entrada.lower() == "sair":
        break

    if " " not in entrada:
        print("Formato inválido. Use: <TOPICO> <MENSAGEM>")
        continue

    topico, mensagem = entrada.split(" ", 1)
    timestamp = datetime.now().strftime("%H:%M:%S")
    full_message = f"{topico.upper()} [{timestamp}] {mensagem}"
    s.send_string(full_message)
    print(f">>> Enviado: {full_message}")
