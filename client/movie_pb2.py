# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmovie.proto\"\x15\n\x07MovieID\x12\n\n\x02id\x18\x01 \x01(\t\"\x16\n\x05Title\x12\r\n\x05title\x18\x01 \x01(\t\"H\n\tMovieData\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\x02\x12\x10\n\x08\x64irector\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\"=\n\x0f\x46\x65\x65\x64\x62\x61\x63kMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x19\n\x05movie\x18\x02 \x01(\x0b\x32\n.MovieData\"L\n\x0cRatingUpdate\x12\x0c\n\x02id\x18\x02 \x01(\tH\x00\x12\x0f\n\x05title\x18\x03 \x01(\tH\x00\x12\x0e\n\x06rating\x18\x01 \x01(\x02\x42\r\n\x0bid_or_title\"\x07\n\x05\x45mpty2\x95\x02\n\x05Movie\x12&\n\x0cGetMovieByID\x12\x08.MovieID\x1a\n.MovieData\"\x00\x12\'\n\rGetListMovies\x12\x06.Empty\x1a\n.MovieData\"\x00\x30\x01\x12\'\n\x0fGetMovieByTitle\x12\x06.Title\x1a\n.MovieData\"\x00\x12-\n\x0b\x43reateMovie\x12\n.MovieData\x1a\x10.FeedbackMessage\"\x00\x12\x36\n\x11UpdateMovieRating\x12\r.RatingUpdate\x1a\x10.FeedbackMessage\"\x00\x12+\n\x0bRemoveMovie\x12\x08.MovieID\x1a\x10.FeedbackMessage\"\x00\x62\x06proto3')



_MOVIEID = DESCRIPTOR.message_types_by_name['MovieID']
_TITLE = DESCRIPTOR.message_types_by_name['Title']
_MOVIEDATA = DESCRIPTOR.message_types_by_name['MovieData']
_FEEDBACKMESSAGE = DESCRIPTOR.message_types_by_name['FeedbackMessage']
_RATINGUPDATE = DESCRIPTOR.message_types_by_name['RatingUpdate']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
MovieID = _reflection.GeneratedProtocolMessageType('MovieID', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEID,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieID)
  })
_sym_db.RegisterMessage(MovieID)

Title = _reflection.GeneratedProtocolMessageType('Title', (_message.Message,), {
  'DESCRIPTOR' : _TITLE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:Title)
  })
_sym_db.RegisterMessage(Title)

MovieData = _reflection.GeneratedProtocolMessageType('MovieData', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEDATA,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieData)
  })
_sym_db.RegisterMessage(MovieData)

FeedbackMessage = _reflection.GeneratedProtocolMessageType('FeedbackMessage', (_message.Message,), {
  'DESCRIPTOR' : _FEEDBACKMESSAGE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:FeedbackMessage)
  })
_sym_db.RegisterMessage(FeedbackMessage)

RatingUpdate = _reflection.GeneratedProtocolMessageType('RatingUpdate', (_message.Message,), {
  'DESCRIPTOR' : _RATINGUPDATE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:RatingUpdate)
  })
_sym_db.RegisterMessage(RatingUpdate)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_MOVIE = DESCRIPTOR.services_by_name['Movie']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOVIEID._serialized_start=15
  _MOVIEID._serialized_end=36
  _TITLE._serialized_start=38
  _TITLE._serialized_end=60
  _MOVIEDATA._serialized_start=62
  _MOVIEDATA._serialized_end=134
  _FEEDBACKMESSAGE._serialized_start=136
  _FEEDBACKMESSAGE._serialized_end=197
  _RATINGUPDATE._serialized_start=199
  _RATINGUPDATE._serialized_end=275
  _EMPTY._serialized_start=277
  _EMPTY._serialized_end=284
  _MOVIE._serialized_start=287
  _MOVIE._serialized_end=564
# @@protoc_insertion_point(module_scope)