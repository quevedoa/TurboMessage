import grpc
import turbomessage_pb2
import turbomessage_pb2_grpc
from concurrent import futures
import threading

class TurboMessage(turbomessage_pb2_grpc.TurboMessageServicer):
    bd = {} # Base de datos de usuarios como llaves y arreglo de correos como valores
    bd_salida = {}
    usuarios = []

    numMaxCorreos = 5
    folio_correos = 0

    lock_registroUsuario = threading.Lock()
    lock_mandarCorreo = threading.Lock()
    lock_borrarCorreoEntrada = threading.Lock()
    lock_borrarCorreoSalida = threading.Lock()
    lock_leerCorreosEntrada = threading.Lock()
    lock_leerCorreosSalida = threading.Lock()
    lock_correoLeido = threading.Lock()

    def checarUsuario(self, request, context):
        for usuario in TurboMessage.usuarios:
            if (request.username == usuario.username) and (request.password == usuario.password):
                return turbomessage_pb2.Status(exito=True, razon="Usuario y contraseña correctos.")
        return turbomessage_pb2.Status(exito=False, razon="Usuario o contraseña está incorrecto.") 
    
    def registrarUsuario(self, request, context):
        for usuario in TurboMessage.usuarios:
           if (request.username == usuario.username):
               return turbomessage_pb2.Status(exito=False, razon="Usuario ya ha sido registrado.") 
        
        TurboMessage.lock_registroUsuario.acquire()
        TurboMessage.usuarios.append(request)
        TurboMessage.bd[request.username] = []
        TurboMessage.bd_salida[request.username] = []
        print(TurboMessage.usuarios)
        TurboMessage.lock_registroUsuario.release()

        return turbomessage_pb2.Status(exito=True, razon="Usuario registrado exitosamente.")
    
    def mandarCorreo(self, request, context):
        destino = request.destinatario
        emisor = request.emisor

        for usuario in TurboMessage.usuarios:
            if usuario.username == destino:
                TurboMessage.lock_mandarCorreo.acquire()
                if len(TurboMessage.bd[destino]) >= TurboMessage.numMaxCorreos:
                    TurboMessage.lock_mandarCorreo.release()
                    return turbomessage_pb2.Status(exito=False, razon="El destinatario tiene la bandeja llena.")
                else:
                    nuevoCorreo = turbomessage_pb2.Correo(id=TurboMessage.folio_correos, tema=request.tema, emisor=request.emisor, destinatario=request.destinatario, mensaje=request.mensaje, leido=False)
                    TurboMessage.folio_correos += 1
                    TurboMessage.bd[destino].append(nuevoCorreo)
                    TurboMessage.bd_salida[emisor].append(nuevoCorreo)
                    TurboMessage.lock_mandarCorreo.release()
                    return turbomessage_pb2.Status(exito=True, razon="Correo enviado exitosamente.")

        return turbomessage_pb2.Status(exito=False, razon="Usuario destino no existe.")
    
    def leerCorreosEntrada(self, request, context):
        try:
            TurboMessage.lock_leerCorreosEntrada.acquire()
            correosUsuario = TurboMessage.bd[request.username]
            for correo in correosUsuario:
                yield correo
            TurboMessage.lock_leerCorreosEntrada.release()
        except Exception:
            print("Error!")

    def leerCorreosSalida(self, request, context):
        try:
            TurboMessage.lock_leerCorreosSalida.acquire()
            correosUsuario = TurboMessage.bd_salida[request.username]
            for correo in correosUsuario:
                yield correo
            TurboMessage.lock_leerCorreosSalida.release()
            # correosSalida = []
            # TurboMessage.lock_leerCorreos.acquire()
            # for arrCorreos in TurboMessage.bd.values():
            #     for correo in arrCorreos:
            #         if correo.emisor == request.username:
            #             correosSalida.append(correo)
            # for correo in correosSalida:
            #     yield correo
            # TurboMessage.lock_leerCorreos.release()
        except Exception:
            print(Exception)
    
    def correoLeido(self, request, context):
        correosUsuario = TurboMessage.bd_salida[request.emisor]
        for i in range(0, len(correosUsuario)):
            if correosUsuario[i].id == request.id:

                TurboMessage.lock_leerCorreosEntrada.acquire()
                correoLeido = correosUsuario[i]
                correosUsuario[i] = turbomessage_pb2.Correo(id=correoLeido.id, tema=correoLeido.tema, emisor=correoLeido.emisor, destinatario=correoLeido.destinatario, mensaje=correoLeido.mensaje, leido=True)
                TurboMessage.lock_leerCorreosEntrada.release()

                return turbomessage_pb2.Status(exito=True, razon="Correo leido exitosamente.")
        return turbomessage_pb2.Status(exito=False, razon="No existe correo.")

    def borrarCorreoEntrada(self, request, context):
        correosUsuario = TurboMessage.bd[request.destinatario]
        for i in range(0, len(correosUsuario)):
            if correosUsuario[i].id == request.id:

                TurboMessage.lock_borrarCorreoEntrada.acquire()
                correosUsuario.pop(i)
                TurboMessage.lock_borrarCorreoEntrada.release()

                return turbomessage_pb2.Status(exito=True, razon="Correo borrado exitosamente.")
        return turbomessage_pb2.Status(exito=False, razon="No existe correo.")
    
    def borrarCorreoSalida(self, request, context):
        correosUsuario = TurboMessage.bd_salida[request.emisor]
        for i in range(0, len(correosUsuario)):
            if correosUsuario[i].id == request.id:

                TurboMessage.lock_borrarCorreoSalida.acquire()
                correosUsuario.pop(i)
                TurboMessage.lock_borrarCorreoSalida.release()

                return turbomessage_pb2.Status(exito=True, razon="Correo borrado exitosamente.")
        return turbomessage_pb2.Status(exito=False, razon="No existe correo.")

def empezarServidor_TurboMessage():
    puerto = "50200"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    turbomessage_pb2_grpc.add_TurboMessageServicer_to_server(TurboMessage(), servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    print("Comenzando servidor de TurboMessage...")
    empezarServidor_TurboMessage()