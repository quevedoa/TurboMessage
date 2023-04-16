import grpc
import turbomessage_pb2
import turbomessage_pb2_grpc
from concurrent import futures
import threading

class TurboMessage(turbomessage_pb2_grpc.TurboMessageServicer):
    bd = {} # Base de datos de usuarios como llaves y arreglo de correos como valores
    usuarios = []

    numMaxCorreos = 5
    folio_correos = 0

    lock_registroUsuario = threading.lock()
    lock_mandarCorreo = threading.lock()
    lock_borrarCorreo = threading.lock()

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
        TurboMessage.lock_registroUsuario.release()
        
        return turbomessage_pb2.Status(exito=True, razon="Usuario registrado exitosamente.")
    
    def mandarCorreo(self, request, context):
        destino = request.destinatario

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
                    TurboMessage.lock_mandarCorreo.release()
                    return turbomessage_pb2.Status(exito=True, razon="Correo enviado exitosamente.")

        return turbomessage_pb2.Status(exito=False, razon="Usuario destino no existe.")
    
    ## Chance el stream no jale y sea mejor mandar el arreglo completo
    ## Podriamos poner un lock aqui no se
    def leerCorreos(self, request, context):
        correosUsuario = TurboMessage.bd[request.username]
        for correo in correosUsuario:
            yield correo
    
    def borrarCorreo(self, request, context):
        correosUsuario = TurboMessage.bd[request.destinatario]
        for i in range(0, len(correosUsuario)):
            if correosUsuario[i].id == request.id:

                TurboMessage.lock_borrarCorreo.acquire()
                correosUsuario.pop(i)
                TurboMessage.lock_borrarCorreo.release()

                return turbomessage_pb2.Status(exito=True, razon="Correo borrado exitosamente.")
        return turbomessage_pb2.Status(exito=False, razon="Correo a borrar no existe.")

def empezarServidor_TurboMessage():
    puerto = "500200"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    turbomessage_pb2_grpc.add_TurboMessageServicer_to_server(TurboMessage(), servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    print("Comenzando servidor de TurboMessage...")
    empezarServidor_TurboMessage()