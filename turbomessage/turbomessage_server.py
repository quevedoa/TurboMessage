import grpc
import turbomessage_pb2
import turbomessage_pb2_grpc
from concurrent import futures

class TurboMessage(turbomessage_pb2_grpc.TurboMessageServicer):
    numMaxCorreos = 5
    bd = {} # Base de datos de usuarios como llaves y arreglo de correos como valores

    ## Big ifs: chance no jale que el objeto de usuario de gRPC funcione como llave para bd
    def checarUsuario(self, request, context):
        for usuario in TurboMessage.bd.keys():
            if (request.username == usuario.username) and (request.password == usuario.password):
                return turbomessage_pb2.Status(exito=True, razon="Usuario y contraseña correctos.")
        return turbomessage_pb2.Status(exito=False, razon="Usuario o contraseña está incorrecto.")
    
    def registrarUsuario(self, request, context):
        for usuario in TurboMessage.keys():
            if (request.username == usuario.username):
                return turbomessage_pb2.Status(exito=False, razon="Usuario ya ha sido registrado.")
        TurboMessage.bd[request] = []
        return turbomessage_pb2.Status(exito=True, razon="Usuario registrado exitosamente.")
    
    def mandarCorreo(self, request, context):
        destino = request.destinatario
        for usuario in TurboMessage.bd.keys():
            if usuario.username == destino:
                if len(TurboMessage.bd[usuario]) >= TurboMessage.numMaxCorreos:
                    return turbomessage_pb2.Status(exito=False, razon="El destinatario tiene la bandeja llena.")
                else:
                    TurboMessage.bd[usuario].append(request)
                    return turbomessage_pb2.Status(exito=True, razon="Correo enviado exitosamente.")
        return turbomessage_pb2.Status(exito=False, razon="Usuario destino no existe.")
    
    ## Chance el stream no jale y sea mejor mandar el arreglo completo
    def leerCorreos(self, request, context):
        
    
    def borrarCorreo(self, request, context):
        return super().borrarCorreo(request, context)
    