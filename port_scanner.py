import socket

def port_scan(target_ip, start_port, end_port):

    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")

    try:
        for port in range(start_port, end_port + 1):

            # Bir socket oluşturur (1. parametre IPv4 ve 2. parametre TCP bağlantısı seçildiğini belirtir)
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(1) # Bağlantı 1 sn içinde kurulmalıdır

            # Bağlantıyı başlatır (Sonuç 0 gelirse açık demektir)
            result = scan.connect_ex((target_ip, port))

            if result == 0: print(f"[+] Port {port} is open")
            else:           print(f"[-] Port {port} is closed")

            # Bağlantıyı sonlandırır
            scan.close()

    # Hata çeşitlerine göre farklı hata mesajları döndürür
    except socket.gaierror:
        print(f"[ERROR] DNS resolution error. Unable to resolve {target_ip} address")
    except socket.error as error:
        print(f"[ERROR] Socket error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")

    print("Port scanning process has been completed")


target_ip  = input("Target IP: ")
start_port = int(input("Starting Port: "))
end_port   = int(input("Ending Port: "))

port_scan(target_ip, start_port, end_port)

