import json
import socket
import matplotlib.pylab as plt

IP = "127.0.0.1"
PORT = 12345

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(1)
    print(f"serving on {IP}:{PORT}")

    client_socket, client_address = server_socket.accept()

    msg = "hi from server!"
    client_socket.send(msg.encode("utf-8"))

    # we will for data and plot it
    plot_data = client_socket.recv(1024 * 5)
    plot_data_decoded = plot_data.decode("utf-8")
    deserialize_object = json.loads(plot_data_decoded)

    x_values = deserialize_object.keys()
    y_values = deserialize_object.values()

    plt.plot(x_values, y_values)
    plt.show()
