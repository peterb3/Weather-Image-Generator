import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    temperature = message.decode('utf-8')

    print(f"Received request from the client: {message.decode()}")

    try:
        temperature = int(temperature)

        if temperature < 32:
            reply = "https://static.vecteezy.com/system/resources/previews/016/595/897/original/cold-weather-thermometer-isolated-3d-render-of-winter-icon-png.png"

        elif temperature < 70:
            reply = "https://www.clipartmax.com/png/middle/0-8774_medium-image-weather-symbols.png"

        else:
            reply = "https://th.bing.com/th/id/R.dfec3f5ff84642815d6f9c8dd809f189?rik=MIypIBjoUFKYZw&riu=http%3a%2f%2fwww.clipartbest.com%2fcliparts%2fMiL%2fMAr%2fMiLMArXpT.png&ehk=1KhyzZh0wXHGQjpqSUJFIztwFqMuGYjpXvJj4pLzRIc%3d&risl=&pid=ImgRaw&r=0"

        socket.send_string(reply)

    except ValueError:
        print("Error reading temperature value: {e}")

        reply = "Error"

        socket.send_string(reply)
