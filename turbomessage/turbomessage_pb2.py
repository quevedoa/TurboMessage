# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: turbomessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12turbomessage.proto\x12\x0cturbomessage\"D\n\x06Status\x12\x12\n\x05\x65xito\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x12\n\x05razon\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_exitoB\x08\n\x06_razon\"Q\n\x07Usuario\x12\x15\n\x08username\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08password\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0b\n\t_usernameB\x0b\n\t_password\"\xc8\x01\n\x06\x43orreo\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04tema\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x65misor\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0c\x64\x65stinatario\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07mensaje\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05leido\x18\x06 \x01(\x08H\x05\x88\x01\x01\x42\x05\n\x03_idB\x07\n\x05_temaB\t\n\x07_emisorB\x0f\n\r_destinatarioB\n\n\x08_mensajeB\x08\n\x06_leido2\xa2\x04\n\x0cTurboMessage\x12\x41\n\x10registrarUsuario\x12\x15.turbomessage.Usuario\x1a\x14.turbomessage.Status\"\x00\x12>\n\rchecarUsuario\x12\x15.turbomessage.Usuario\x1a\x14.turbomessage.Status\"\x00\x12<\n\x0cmandarCorreo\x12\x14.turbomessage.Correo\x1a\x14.turbomessage.Status\"\x00\x12\x45\n\x12leerCorreosEntrada\x12\x15.turbomessage.Usuario\x1a\x14.turbomessage.Correo\"\x00\x30\x01\x12\x44\n\x11leerCorreosSalida\x12\x15.turbomessage.Usuario\x1a\x14.turbomessage.Correo\"\x00\x30\x01\x12\x43\n\x13\x62orrarCorreoEntrada\x12\x14.turbomessage.Correo\x1a\x14.turbomessage.Status\"\x00\x12\x42\n\x12\x62orrarCorreoSalida\x12\x14.turbomessage.Correo\x1a\x14.turbomessage.Status\"\x00\x12;\n\x0b\x63orreoLeido\x12\x14.turbomessage.Correo\x1a\x14.turbomessage.Status\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'turbomessage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATUS._serialized_start=36
  _STATUS._serialized_end=104
  _USUARIO._serialized_start=106
  _USUARIO._serialized_end=187
  _CORREO._serialized_start=190
  _CORREO._serialized_end=390
  _TURBOMESSAGE._serialized_start=393
  _TURBOMESSAGE._serialized_end=939
# @@protoc_insertion_point(module_scope)
