# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\")\n\tTimesData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x0b\n\tEmptyDate2]\n\x08Showtime\x12%\n\x0eGetTimesByDate\x12\x05.Date\x1a\n.TimesData\"\x00\x12*\n\x0cGetListTimes\x12\n.EmptyDate\x1a\n.TimesData\"\x00\x30\x01\x62\x06proto3')



_DATE = DESCRIPTOR.message_types_by_name['Date']
_TIMESDATA = DESCRIPTOR.message_types_by_name['TimesData']
_EMPTYDATE = DESCRIPTOR.message_types_by_name['EmptyDate']
Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Date)
  })
_sym_db.RegisterMessage(Date)

TimesData = _reflection.GeneratedProtocolMessageType('TimesData', (_message.Message,), {
  'DESCRIPTOR' : _TIMESDATA,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:TimesData)
  })
_sym_db.RegisterMessage(TimesData)

EmptyDate = _reflection.GeneratedProtocolMessageType('EmptyDate', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYDATE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:EmptyDate)
  })
_sym_db.RegisterMessage(EmptyDate)

_SHOWTIME = DESCRIPTOR.services_by_name['Showtime']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATE._serialized_start=18
  _DATE._serialized_end=38
  _TIMESDATA._serialized_start=40
  _TIMESDATA._serialized_end=81
  _EMPTYDATE._serialized_start=83
  _EMPTYDATE._serialized_end=94
  _SHOWTIME._serialized_start=96
  _SHOWTIME._serialized_end=189
# @@protoc_insertion_point(module_scope)
