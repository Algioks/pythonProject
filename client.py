import json
import math
import socket
import time
import game_of_life
import threading

IP = "127.0.0.1"
PORT = 12345


def generate_sine_function_coordinates(num_points: int):
    data = {}
    for num in range(num_points):
        x = num * 0.1
        y = math.sin(x)
        data[x] = y
    return data


def client_thread(client_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    current_map = game_of_life.create_map()
    serialized_init_map = json.dumps(current_map)
    client_socket.send(serialized_init_map.encode("utf-8"))

    for count in range(game_of_life.GENERATIONS):
        print(f"Client {client_id}, iteration = {count}")
        time.sleep(0.5)
        current_map = game_of_life.update_map(current_map)
        serialized_init_map = json.dumps(current_map)
        client_socket.send(serialized_init_map.encode("utf-8"))


threads = []
for client_id in range(3):
    thread = threading.Thread(target=client_thread, args=(client_id,))
    threads.append(thread)
    thread.start()



for thread in threads:
    thread.join()
print("Complete")

"""

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    # message = client_socket.recv(1024)
    # print(message.decode("utf-8"))
    
    current_map = game_of_life.create_map()
    serialized_init_map = json.dumps(current_map)
    client_socket.send(serialized_init_map.encode("utf-8"))

    for count in range(game_of_life.GENERATIONS):
        print("iteration = ", count)
        time.sleep(0.1)
        current_map = game_of_life.update_map(current_map)
        # game_of_life.show_map(current_map)        
        serialized_init_map = json.dumps(current_map)
        client_socket.send(serialized_init_map.encode("utf-8"))
    
    # plot_data = generate_sine_function_coordinates(100)

    # serialized_data = json.dumps(plot_data)

    # client_socket.send(serialized_data.encode("utf-8"))
    # 
    # """
