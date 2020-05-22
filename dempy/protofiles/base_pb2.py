# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='dempy',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\nbase.proto\x12\x05\x64\x65mpy\"\x90\x01\n\x06\x45ntity\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12-\n\x08metadata\x18\x04 \x03(\x0b\x32\x1b.dempy.Entity.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01'
)




_ENTITY_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='dempy.Entity.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dempy.Entity.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dempy.Entity.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=166,
)

_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='dempy.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dempy.Entity.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='dempy.Entity.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='dempy.Entity.tags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='dempy.Entity.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ENTITY_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=166,
)

_ENTITY_METADATAENTRY.containing_type = _ENTITY
_ENTITY.fields_by_name['metadata'].message_type = _ENTITY_METADATAENTRY
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENTITY_METADATAENTRY,
    '__module__' : 'base_pb2'
    # @@protoc_insertion_point(class_scope:dempy.Entity.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'base_pb2'
  # @@protoc_insertion_point(class_scope:dempy.Entity)
  })
_sym_db.RegisterMessage(Entity)
_sym_db.RegisterMessage(Entity.MetadataEntry)


_ENTITY_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
