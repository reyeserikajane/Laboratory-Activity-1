import socket

# Create a TCP socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to localhost on port 8080
server_socket.bind(('localhost', 8080))

# Listen for incoming connections (max 1 client in this case)
server_socket.listen(1)
print("Server is listening on port 8080...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connection established with client at {client_address}")

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received from client: {data}")

# Send a response back to the client
response = "Hello from Server!"
client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
