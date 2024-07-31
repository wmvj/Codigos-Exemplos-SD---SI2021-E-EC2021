import rpyc

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 12345)
    remote_service = conn.root

    result = remote_service.add_numbers(5, 3)
    print("Resultado:", result)

    conn.close()
