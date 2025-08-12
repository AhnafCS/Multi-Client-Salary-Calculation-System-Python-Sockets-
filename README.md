This is a basic client–server application built with Python’s socket and threading modules.
The server listens for connections from multiple clients simultaneously, receives the number of hours worked, and calculates the salary based on the following rules:

> ≤ 40 hours: Tk 200 per hour

> (>) 40 hours: Tk 8000 base salary + Tk 300 for each extra hour worked over 40

The server sends the calculated salary back to the client.
Clients can send multiple requests in one session and terminate the connection by sending "Disconnect".

Features:

>Multi-client handling via threading

>Custom message framing with fixed-length headers

>Clean message sending and receiving functions

>Termination with "Disconnect" command

Usage:

1.Run the server:
python SERVER.py

2.Run one or more clients:
python CLIENT.py

3.Enter hours worked or type "Disconnect" to exit.

Tech stack: Python 3, sockets, threading
