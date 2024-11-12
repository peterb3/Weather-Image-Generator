# Example usage of Server.py image generation file

import zmq

def send_temp(temp: str) -> str:
    socket.send_string(temp)

    response = socket.recv()

    image_link = response.decode()

    if response == "Error":
        print("Error sending temperature data")

    else:
        print("Server sent back image link")
        return image_link

def end_server() -> None:
    socket.send_string("Q")

if __name__ == "__main__":
    context = zmq.Context()

    print("Client attempting to connect to server...")

    socket = context.socket(zmq.REQ)

    socket.connect("tcp://localhost:5555")

    tests = ["20", "50", "85"]

    for test in tests:
        print(send_temp(test))

    end_server()