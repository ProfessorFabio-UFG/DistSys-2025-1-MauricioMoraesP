import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
p = f"tcp://{HOST}:{PORT}"
s.connect(p)

print("=== Subscriber Iniciado ===")
print("Digite tópicos para assinar (ex: TIME, ALERTA).")
print("Digite 'start' para começar a escutar mensagens.\n")

assinaturas = set()

while True:
    topico = input("Assinar tópico (ou 'start' para iniciar): ")

    if topico.lower() == "start":
        if not assinaturas:
            print("Nenhum tópico assinado!")
            continue
        break
    if topico.strip() == "":
        continue

    s.setsockopt_string(zmq.SUBSCRIBE, topico.upper())
    assinaturas.add(topico.upper())
    print(f">>> Assinado: {topico.upper()}")

print(f"\nEscutando tópicos: {', '.join(assinaturas)}...\n")
try:
    while True:
        msg = s.recv()
        print(bytes.decode(msg))
except KeyboardInterrupt:
    print("\nEncerrando assinante...")
