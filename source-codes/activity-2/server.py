import socket

# Define server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))  # Attribute: port = 8080
server_socket.listen(1)

print("Server is ready and listening on port 8080...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print(f"Client connected from: {client_address}")

# Receive data from client
message = client_socket.recv(1024).decode()
print("Message from client:", message)

# Send response
client_socket.send("Hello from Server!".encode())

# Close sockets
client_socket.close()
server_socket.close()
