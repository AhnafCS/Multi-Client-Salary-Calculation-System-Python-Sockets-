import socket
server_port = 8080
format = "utf-8"
buffer_for_lenght = 16

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
addr = (host_ip, server_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def message_to_be_sent(message):
    message = message.encode(format)

    message_length = str(len(message))
    message_length = message_length.encode(format)


    padding = b" " * (buffer_for_lenght - len(message_length))
    message_length = message_length + padding

    client.send(message_length)
    client.send(message)
    response = client.recv(2048).decode(format)
    print(response)

while True:
    user_input = input("Enter: ")
    message_to_be_sent(user_input) 
    if user_input == "Disconnect":
        break