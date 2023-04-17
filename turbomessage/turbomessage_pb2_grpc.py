# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import turbomessage_pb2 as turbomessage__pb2


class TurboMessageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registrarUsuario = channel.unary_unary(
                '/turbomessage.TurboMessage/registrarUsuario',
                request_serializer=turbomessage__pb2.Usuario.SerializeToString,
                response_deserializer=turbomessage__pb2.Status.FromString,
                )
        self.checarUsuario = channel.unary_unary(
                '/turbomessage.TurboMessage/checarUsuario',
                request_serializer=turbomessage__pb2.Usuario.SerializeToString,
                response_deserializer=turbomessage__pb2.Status.FromString,
                )
        self.mandarCorreo = channel.unary_unary(
                '/turbomessage.TurboMessage/mandarCorreo',
                request_serializer=turbomessage__pb2.Correo.SerializeToString,
                response_deserializer=turbomessage__pb2.Status.FromString,
                )
        self.leerCorreos = channel.unary_stream(
                '/turbomessage.TurboMessage/leerCorreos',
                request_serializer=turbomessage__pb2.Usuario.SerializeToString,
                response_deserializer=turbomessage__pb2.Correo.FromString,
                )
        self.borrarCorreo = channel.unary_unary(
                '/turbomessage.TurboMessage/borrarCorreo',
                request_serializer=turbomessage__pb2.Correo.SerializeToString,
                response_deserializer=turbomessage__pb2.Status.FromString,
                )
        self.correoLeido = channel.unary_unary(
                '/turbomessage.TurboMessage/correoLeido',
                request_serializer=turbomessage__pb2.Correo.SerializeToString,
                response_deserializer=turbomessage__pb2.Status.FromString,
                )


class TurboMessageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registrarUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def checarUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mandarCorreo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def leerCorreos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def borrarCorreo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def correoLeido(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TurboMessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registrarUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.registrarUsuario,
                    request_deserializer=turbomessage__pb2.Usuario.FromString,
                    response_serializer=turbomessage__pb2.Status.SerializeToString,
            ),
            'checarUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.checarUsuario,
                    request_deserializer=turbomessage__pb2.Usuario.FromString,
                    response_serializer=turbomessage__pb2.Status.SerializeToString,
            ),
            'mandarCorreo': grpc.unary_unary_rpc_method_handler(
                    servicer.mandarCorreo,
                    request_deserializer=turbomessage__pb2.Correo.FromString,
                    response_serializer=turbomessage__pb2.Status.SerializeToString,
            ),
            'leerCorreos': grpc.unary_stream_rpc_method_handler(
                    servicer.leerCorreos,
                    request_deserializer=turbomessage__pb2.Usuario.FromString,
                    response_serializer=turbomessage__pb2.Correo.SerializeToString,
            ),
            'borrarCorreo': grpc.unary_unary_rpc_method_handler(
                    servicer.borrarCorreo,
                    request_deserializer=turbomessage__pb2.Correo.FromString,
                    response_serializer=turbomessage__pb2.Status.SerializeToString,
            ),
            'correoLeido': grpc.unary_unary_rpc_method_handler(
                    servicer.correoLeido,
                    request_deserializer=turbomessage__pb2.Correo.FromString,
                    response_serializer=turbomessage__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'turbomessage.TurboMessage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TurboMessage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registrarUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.TurboMessage/registrarUsuario',
            turbomessage__pb2.Usuario.SerializeToString,
            turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def checarUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.TurboMessage/checarUsuario',
            turbomessage__pb2.Usuario.SerializeToString,
            turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mandarCorreo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.TurboMessage/mandarCorreo',
            turbomessage__pb2.Correo.SerializeToString,
            turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def leerCorreos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/turbomessage.TurboMessage/leerCorreos',
            turbomessage__pb2.Usuario.SerializeToString,
            turbomessage__pb2.Correo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def borrarCorreo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.TurboMessage/borrarCorreo',
            turbomessage__pb2.Correo.SerializeToString,
            turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def correoLeido(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/turbomessage.TurboMessage/correoLeido',
            turbomessage__pb2.Correo.SerializeToString,
            turbomessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
