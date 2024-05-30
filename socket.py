import socket

def send_socket_name(socket_name):
    # Создаем файловый сокет
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    try:
        # Соединяемся с сервером
        sock.connect(socket_name)
        
        # Отправляем название сокета на сервер
        sock.sendall(socket_name.encode())
    finally:
        sock.close()

def main():
    # Запрашиваем название сокета с клавиатуры
    socket_name = input("Введите название сокета: ")
    
    # Отправляем название сокета на сервер
    send_socket_name(socket_name)

if __name__ == "__main__":
    main()