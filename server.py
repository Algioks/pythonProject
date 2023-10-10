import json
import socket
import matplotlib.pylab as plt
import game_of_life

class Server :
    def __init__ (self, ip : str = "127.0.0.1" , port : int = 12345, amount_of_client : int = 5):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen(amount_of_client)
        print("init")
    
    def start(self):
        while True:
            client_socket, client_address = self.socket.accept()
            self.handle_client(client_socket)
            print("start")
              
    def handle_client(self, client_socket : socket.socket):
        count = 0
        while True:
            plot_data = client_socket.recv(1024 * 50)
            plot_data_decoded = plot_data.decode("utf-8")
            deserialize_object = json.loads(plot_data_decoded) 
            print(f"received object {count}")
            count += 1
                

if __name__ == '__main__':
    
    server = Server()
    server.start()
    
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind((IP, PORT))
    # server_socket.listen(1)
    # print(f"serving on {IP}:{PORT}")

    # client_socket, client_address = server_socket.accept()

    # msg = "hi from server!"
    # client_socket.send(msg.encode("utf-8"))

    # we will for data and plot it
    # while True:
    #     plot_data = client_socket.recv(1024 * 50)
    #     plot_data_decoded = plot_data.decode("utf-8")
    #     deserialize_object = json.loads(plot_data_decoded)
        
        # x_values = deserialize_object.keys()
        # y_values = deserialize_object.values()
        # game_of_life.show_map(deserialize_object)
    # plt.show()
    # plt.plot(x_values, y_values)
    # plt.show()
    
    #client sent every 2 sec and server plot it.

#create client object