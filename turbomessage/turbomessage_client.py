import grpc
import os
import sys
import turbomessage_pb2
import turbomessage_pb2_grpc

### CONTEXT CONTINUITY
## - Resuelve que la bandeja de salida no tiene limite
## - Debe de poder leer de su bandeja de salida también

class Cliente_TurboMessage():

    num_maxCorreos = 5

    def __init__(self, target):
        self.target = target
        self.channel = grpc.insecure_channel(target)
        self.stub = turbomessage_pb2_grpc.TurboMessageStub(self.channel)

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def show_paginaInicial(self):
        self.clear_screen()
        print((" " * 30) + "Bienvenido a TurboMessage")
        print("Ingresar con usuario - 1")
        print("Registrar usuario nuevo - 2")

        bandera = True
        while bandera:
            decision = input("Eliga el número de la opción que desea -> ")
            if decision == '1':
                self.show_paginaLogin()
                bandera = False
            elif decision == '2':
                self.show_paginaRegistro()
                bandera = False
            else:
                print("Opción no válida. Intente de nuevo.\n")
    
    def show_paginaLogin(self):
        self.clear_screen()
        print((" " * 30) + "Página de Login")

        while True:
            username = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")

            usuarioPotencial = turbomessage_pb2.Usuario(username=username, password=password)
            respuesta = self.stub.checarUsuario(usuarioPotencial)
            if respuesta.exito == True:
                self.usuario = usuarioPotencial
                self.clear_screen()
                self.show_bandejaEntrada()
                break
            else:
                print(respuesta.razon + "\n")
            
            while True:
                decision = input("Desea regresar a página de inicio? (s/n) -> ")
                if decision == "s":
                    self.clear_screen()
                    self.show_paginaInicial()
                    break
                elif decision == "n":
                    break


    def show_paginaRegistro(self):
        self.clear_screen()
        print((" " * 30) + "Página de Registro") 

        while True:
            username = input("Ingrese el usuario que desea registrar: ")
            password = input("Ingrese la contraseña que desea usar: ")

            usuarioPotencial = turbomessage_pb2.Usuario(username=username, password=password)
            respuesta = self.stub.registrarUsuario(usuarioPotencial)
            if respuesta.exito == True:
                self.usuario = usuarioPotencial
                self.clear_screen()
                self.show_bandejaEntrada()
                break
            else:
                print(respuesta.razon + "\n")
            
            while True:
                decision = input("Desea regresar a página de inicio? (s/n) -> ")
                if decision == "s":
                    self.clear_screen()
                    self.show_paginaInicial()
                    break
                elif decision == "n":
                    break

    def show_bandejaEntrada(self):
        print((" " * 30) + "Bienvenido " + self.usuario.username)
        print("Bandeja de Entrada:")
        self.fetch_bandejaEntrada()
        print()
        print("Bandeja de Salida:")
        self.fetch_bandejaSalida()
        print()
        print("Opciones de acciones a realizar:")
        print((" " * 4) + "1. Mandar un correo nuevo")
        print((" " * 4) + "2. Leer un correo")
        print((" " * 4) + "3. Borrar un correo")
        print((" " * 4) + "4. Refrescar bandeja de entrada")
        print((" " * 4) + "5. Salir de TurboMessage")
        print()

        bandera = True
        while bandera:
            decision = input("Escriba la opción que usted desea -> ")

            bandera = False
            if decision == '1':
                self.clear_screen()
                self.mandarCorreo()
            elif decision == '2':
                self.leerCorreo()
            elif decision == '3':
                self.borrarCorreo()
            elif decision == '4':
                self.clear_screen()
                self.show_bandejaEntrada()
            elif decision == '5':
                print("\nAdios.")
                self.close_channel()
                sys.exit(1)
            else:
                bandera = True
                print("Esa opción no existe. Intente de nuevo.")

    def mandarCorreo(self):
        if len(self.listaCorreosSalida) < Cliente_TurboMessage.num_maxCorreos:
            print((" " * 30) + "Escribe tu correo")
            tema = input("Tema: ")
            destino = input("Destino: ")
            print()
            print("Contenido: [Para finalizar contenido escriba la palabra 'fin' en una nueva línea y pique enter.]")
            contenido = ""
            siguienteLinea = ""
            while siguienteLinea != "fin":
                contenido = contenido + siguienteLinea + "\n"
                siguienteLinea = input()

            while True:
                decision_mandar = input("Desea mandar el correo? (s/n) -> ")
                if decision_mandar == "s":
                    correo = turbomessage_pb2.Correo(tema=tema, emisor=self.usuario.username, destinatario=destino, mensaje=contenido)
                    respuesta = self.stub.mandarCorreo(correo)
                    if respuesta.exito == True:
                        self.listaCorreosSalida.append(correo)
                        print("Correo enviado.")
                        break
                    else:
                        print(respuesta.razon + " Intente de nuevo más tarde.")
                        break
                elif decision_mandar == "n":
                    print("Correo no enviado.")
                    break
            
            print()
            while True:
                decision_regresar = input("Desear regresar a la bandeja de entrada? (s/n) -> ")
                if decision_regresar == "s":
                    break
            self.clear_screen()
        else:
            self.clear_screen()
            print("Borra correos de la bandeja de salida para poder mandar un correo.")
        
        self.show_bandejaEntrada()

    def leerCorreo(self):
        while True:
            decisionBandeja = input("Indique de que bandeja desea leer (entrada/salida) -> ")
            if (decisionBandeja == "entrada") or (decisionBandeja == "salida"):
                break
        if (decisionBandeja == "entrada" and len(self.listaCorreos) == 0) or (decisionBandeja == "salida" and len(self.listaCorreosSalida) == 0):
            self.clear_screen()
            print("No hay correos por ahora.")
            self.show_bandejaEntrada()
        else:
            while True:
                try:
                    num_correo = input("Indique qué número de correo desea leer -> ")
                    if (len(self.listaCorreos) >= int(num_correo)) and (int(num_correo) > 0) or (len(self.listaCorreosSalida) >= int(num_correo)) and (int(num_correo) > 0):
                        if decisionBandeja == "entrada":
                            correo = self.listaCorreos[int(num_correo) - 1]
                            respuesta = self.stub.correoLeido(correo)
                            exito = respuesta.exito
                        else:
                            correo = self.listaCorreosSalida[int(num_correo) - 1]
                            exito = True
                        self.clear_screen()

                        if exito == True:
                            print("Tema: " + correo.tema)
                            print("Emisor: " + correo.emisor)
                            print("Destinatario: " + correo.destinatario)
                            print("\n<" + ("-" * 40) + ">")
                            print(correo.mensaje)
                            print("\n<" + ("-" * 40) + ">")
                            print()

                            decision = "n"
                            while decision != "s":
                                decision = input("Desea regresar a la bandeja de entrada? (s/n) -> ")
                        else:
                            print(respuesta.razon)
                        self.clear_screen()
                    else:
                        self.clear_screen()
                        print("Ese número es inválido. \n")
                    self.show_bandejaEntrada()
                    break
                except ValueError:
                    pass


    def borrarCorreo(self):
        while True:
            decisionBandeja = input("Indique de que bandeja desea borrar (entrada/salida) -> ")
            if (decisionBandeja == "entrada") or (decisionBandeja == "salida"):
                break
        if (decisionBandeja == "entrada" and len(self.listaCorreos) == 0) or (decisionBandeja == "salida" and len(self.listaCorreosSalida) == 0):
            self.clear_screen()
            print("No hay correos por ahora.")
            self.show_bandejaEntrada()
        else:
            while True:
                try:
                    num_correo = input("Indique qué número de correo desea borrar -> ")
                    if (len(self.listaCorreos) >= int(num_correo)) and (int(num_correo) > 0) or (len(self.listaCorreosSalida) >= int(num_correo)) and (int(num_correo) > 0):
                        if decisionBandeja == "entrada":
                            correo = self.listaCorreos[int(num_correo) - 1]
                            respuesta = self.stub.borrarCorreoEntrada(correo)
                            exito = respuesta.exito
                        else:
                            correo = self.listaCorreosSalida[int(num_correo) - 1]
                            respuesta = self.stub.borrarCorreoSalida(correo)
                            exito = respuesta.exito

                        self.clear_screen()
                        if exito == True:
                            print("Correo borrado exitosamente.\n")
                        else:
                            print("Correo no existe.\n")
                    else:
                        self.clear_screen()
                        print("Ese número es inválido.\n")
                    self.show_bandejaEntrada()
                    break
                except ValueError:
                    pass

    def fetch_bandejaEntrada(self):
        i = 1
        self.listaCorreos = []
        for correo in self.stub.leerCorreosEntrada(self.usuario):
            self.listaCorreos.append(correo)
            stringCorreo = str(i) + ". " + correo.emisor + " | " + correo.tema
            print(stringCorreo)
            i += 1
    
    def fetch_bandejaSalida(self):
        i = 1
        self.listaCorreosSalida = []
        for correo in self.stub.leerCorreosSalida(self.usuario):
            self.listaCorreosSalida.append(correo)
            stringCorreo = str(i) + ". " + correo.destinatario + " | " + correo.tema
            if correo.leido:
                stringCorreo = stringCorreo + " (LEIDO)"
            else:
                stringCorreo = stringCorreo + " (NO LEIDO)"
            print(stringCorreo)
            i += 1
            

    def close_channel(self):
        self.channel.close()

if __name__ == "__main__":
    cliente = Cliente_TurboMessage("localhost:50200") 
    cliente.show_paginaInicial()