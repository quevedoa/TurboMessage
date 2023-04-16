import grpc
import turbomessage_pb2
import turbomessage_pb2_grpc
from concurrent import futures
import threading

class TurboMessage(turbomessage_pb2_grpc.TurboMessageServicer):
    numMaxCorreos = 5
    folio_correos = 0

    bd = {} # Base de datos de usuarios como llaves y arreglo de correos como valores
    usuarios = []

    def checarUsuario(self, request, context):
        for usuario in TurboMessage.usuarios:
            if (request.username == usuario.username) and (request.password == usuario.password):
                return turbomessage_pb2.Status(exito=True, razon="Usuario y contraseña correctos.")
        return turbomessage_pb2.Status(exito=False, razon="Usuario o contraseña está incorrecto.") 
    
    def registrarUsuario(self, request, context):
        for usuario in TurboMessage.usuarios:
           if (request.username == usuario.username):
               return turbomessage_pb2.Status(exito=False, razon="Usuario ya ha sido registrado.") 
        TurboMessage.usuarios.append(request)
        TurboMessage.bd[request.username] = []
        return turbomessage_pb2.Status(exito=True, razon="Usuario registrado exitosamente.")
    
    def mandarCorreo(self, request, context):
        destino = request.destinatario
        nuevoCorreo = turbomessage_pb2.Correo(id=TurboMessage.folio_correos, tema=request.tema, emisor=request.emisor, destinatario=request.destinatario, mensaje=request.mensaje, leido=False)
        TurboMessage.folio_correos += 1
        for usuario in TurboMessage.usuarios:
            if usuario.username == destino:
                if len(TurboMessage.bd[destino]) >= TurboMessage.numMaxCorreos:
                    return turbomessage_pb2.Status(exito=False, razon="El destinatario tiene la bandeja llena.")
                else:
                    TurboMessage.bd[destino].append(nuevoCorreo)
                    return turbomessage_pb2.Status(exito=True, razon="Correo enviado exitosamente.")
        return turbomessage_pb2.Status(exito=False, razon="Usuario destino no existe.")
    
    ## Chance el stream no jale y sea mejor mandar el arreglo completo
    def leerCorreos(self, request, context):
        correosUsuario = TurboMessage.bd[request.username]
        for correo in correosUsuario:
            yield correo
    
    def borrarCorreo(self, request, context):
        correosUsuario = TurboMessage.bd[request.destinatario]
        for i in range(0, len(correosUsuario)):
            if correosUsuario[i].id == request.id:
                correosUsuario.pop(i)
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