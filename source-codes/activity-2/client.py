import socket

# Create a TCP socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at localhost on port 8080
client_socket.connect(('localhost', 8080))

# Send a message to the server
message = "Hello from Client!"
client_socket.send(message.encode())

# Receive response from server
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close the connection
client_socket.close()
