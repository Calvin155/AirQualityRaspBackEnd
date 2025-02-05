import time
import random
import bluetooth

def full_mock(client_socket):
    try:

        while True:
            random_number_one_pm = random.randint(0, 30)
            random_number_two_pm = random.randint(30, 49)
            random_number_three_pm = random.randint(50, 75)
            co2 = random.randint(15, 20)
            temp = random.randint(9, 12)
            humidity = random.randint(50, 60)

            data = f"PM1: {random_number_one_pm} µg/m³, PM2.5: {random_number_two_pm} µg/m³, PM10: {random_number_three_pm} µg/m³, CO2: {co2} ppm, Temp: {temp}°C, Humidity: {humidity}%"
            
            client_socket.send(data)
            print("Sent data:", data)
            
            time.sleep(10)

    except Exception as e:
        print(f"Error: {str(e)}")

def start_bluetooth_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)
    
    print("Waiting for connection...")
    
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    full_mock(client_socket)
    
    client_socket.close()
    server_socket.close()


start_bluetooth_server()
