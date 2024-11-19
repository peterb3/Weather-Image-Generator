import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    temperature = message.decode('utf-8')

    print(f"Received request from the client: {message.decode()}")

    if temperature == "Q":
        print("Shutting down...")
        break

    try:
        temperature = int(temperature)

        if temperature < 32:
            reply = "https://static.vecteezy.com/system/resources/previews/016/595/897/original/cold-weather-thermometer-isolated-3d-render-of-winter-icon-png.png"

        elif temperature < 70:
            reply = "https://images.squarespace-cdn.com/content/v1/5acfcc510dbda33931a4a9f9/1525124939291-I3J8K26EKXPD3NU0HZ1K/Program_need_icon_warm.png"

        else:
            reply = "https://static.vecteezy.com/system/resources/previews/008/370/898/original/temperature-weather-thermometers-with-celsius-and-fahrenheit-scales-realistic-3d-weather-thermometer-icon-density-on-white-background-sun-warm-thermostat-meteorology-isolated-icon-free-vector.jpg"

        socket.send_string(reply)

    except ValueError:
        print("Error reading temperature value: {e}")

        reply = "Error"

        socket.send_string(reply)

context.destroy()
