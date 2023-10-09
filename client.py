import json
import math
import socket

from server import IP, PORT


def generate_sine_function_coordinates(num_points: int):
    data = {}
    for num in range(num_points):
        x = num * 0.1
        y = math.sin(x)
        data[x] = y
    return data


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    message = client_socket.recv(1024)

    print(message.decode("utf-8"))

    plot_data = generate_sine_function_coordinates(100)

    serialized_data = json.dumps(plot_data)

    client_socket.send(serialized_data.encode("utf-8"))
