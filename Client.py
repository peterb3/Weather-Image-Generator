# Example usage of Server.py image generation file

import zmq

context = zmq.Context()

print("Client attempting to connect to server...")

socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:5555")

while True:
    temperature = "75"

    socket.send_string(temperature)

    response = socket.recv()

    image_link = response.decode()

    if response == "Error":
        print("Error sending temperature data")

    else:
        print("Server sent back image link")
