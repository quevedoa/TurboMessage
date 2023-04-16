import grpc
import os
import turbomessage_pb2
import turbomessage_pb2_grpc

class Cliente_TurboMessage():

    def __init__(self, target):
        self.target = target
        self.channel = grpc.insecurhowe_channel(target)
        self.stub = turbomessage_pb2_grpc.TurboMessageStub(self.channel)
    


    def close_channel(self):
        self.channel.close()


def run_client():
    with grpc.insecure_channel("localhost:500200") as channel:
        stub = turbomessage_pb2_grpc.TurboMessageStub(channel)

        def clear_screen():
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

        def reset_ui():
            clear_screen()
            show_main_menu()

        def fetch_bandeja_de_entrada():
            for correo in stub.leerCorreos()
            
        def show_main_menu():
            print((" " * 30) + ("Bienveido a Trubo Message"))
            print("Bandeja de Entrada")
            fetch_bandeja_de_entrada()

if __name__ == "__main__":
    run_client()