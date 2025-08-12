import socket
import threading
server_port = 8080
format = "utf-8"
buffer_for_lenght = 16

hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
addr = (host_ip, server_port)
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)
server.listen()
print("The server is listening!!")
def serve_a_client(conn, add):
    print("####################")
    print("Connected to", add)
    
    connected = True
    while connected:
        #talk to client
        message_length = conn.recv(buffer_for_lenght).decode(format)
        print("Upcoming message length", message_length)

        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(format)

            if message == "Disconnect":
                conn.send("The session is terminated".encode(format))
                print("Terminating connection with", add)
                print("###################################")
                connected = False

            else:
                print(message)
                hours = int(message)
                if hours <= 40:
                    salary = 200*hours
                    conn.send(f"Hours worked {hours}, Salary {salary}".encode(format))
                if hours > 40:
                    salary = 300*hours + 8000
                    conn.send(f"Hours worked {hours}, Salary {salary}".encode(format))
    conn.close( )

while True:
    conn, add = server.accept()
    thread = threading.Thread(target=serve_a_client, args=(conn, add))
    thread.start()