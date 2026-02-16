import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8005))
server.listen()
print("Server is listening...")
konekcija, adresa = server.accept()

print("konekcija prihvacena od:", adresa)

podaci = konekcija.recv(1024)
dekodovani_podaci = podaci.decode("utf-8")
print("stigli podaci od klijenta", podaci)

time.sleep(2)

konekcija.close()
server.close()