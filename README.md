# Weather-Image-Generator
This microservice receives temperature data as a string and returns an image URL representing the temperature. It uses ZeroMQ as a communication pipe between the client program and the server.

## Table of Contents
- Installation
- Usage
- Example Request and Response
- UML Diagram

## Installation
1. Clone the repository:
   ```python
   git clone <repo-url>
   cd <repo-url>
   ```
2. Install the required dependencies:
   ```python
   pip install pyzmq
   ```

## Usage
Run the application:
  ```python
  python Server.py
  ```
* Request Temperature Image: Send a temperature as a string to the server to receive an image URL, example request show below.
* Shutdown Server: Send "Q" as a message to shut down the server.

## Example Request and Response
### Requesting Data
To send a request, connect to the socket on local host port 5555 through ZeroMQ, then send temperature value as a string (utf-8 encoded by default).
Note: Ending the server is done the same way as sending a temperature request, except the string being sent is "Q".
### Receiving Data
To receive data, after sending a temperature string to the microservice, set a variable to receive a response from the service using:
  ```python
  <variable> = socket.recv()
  ```
This string will either contain the URL to an image, or an error message if the temperature data was incorrectly sent.
### Client Code Example
This code shows how to programmatically request and receive data from the microservice:
  ```python
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
  ```

## UML Diagram
![microservice-UML](https://github.com/user-attachments/assets/65b9cb22-8181-4735-82ac-a9c619f8e9e8)

