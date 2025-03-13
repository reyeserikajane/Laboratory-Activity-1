import socket

# Define client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 8080))  # Relation: communicatesWith(ServerService)

# Send message
client_socket.send("Hello from Client!".encode())

# Receive response
response = client_socket.recv(1024).decode()
print("Message from server:", response)

# Close the connection
client_socket.close()
