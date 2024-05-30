import socket

def send_socket_name(server_address, server_port, socket_name):
    # Создаем сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Соединяемся с сервером
        sock.connect((server_address, server_port))
        
        # Отправляем название сокета на сервер
        sock.sendall(socket_name.encode())
    finally:
        sock.close()

def main():
    # Запрашиваем название сокета и данные сервера с клавиатуры
    socket_name = input("Введите название сокета: ")
    server_address = input("Введите адрес сервера: ")
    server_port = int(input("Введите порт сервера: "))
    
    # Отправляем название сокета на сервер
    send_socket_name(server_address, server_port, socket_name)

if __name__ == "__main__":
    main()