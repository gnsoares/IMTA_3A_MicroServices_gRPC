
.PHONY: all movie booking showtime
MKFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
BASE_DIR := $(patsubst %/,%,$(dir $(MKFILE_PATH)))
MOVIE=$(BASE_DIR)/movie
SHOWTIME=$(BASE_DIR)/showtime
BOOKING=$(BASE_DIR)/booking

all: movie showtime booking

movie:
	python -m grpc_tools.protoc -I=$(MOVIE)/protos --python_out=$(MOVIE) --grpc_python_out=$(MOVIE) movie.proto
	cp $(MOVIE)/movie_pb2_grpc.py client
	cp $(MOVIE)/movie_pb2.py client
	cp $(MOVIE)/movie_pb2_grpc.py user
	cp $(MOVIE)/movie_pb2.py user

showtime:
	python -m grpc_tools.protoc -I=$(SHOWTIME)/protos --python_out=$(SHOWTIME) --grpc_python_out=$(SHOWTIME) showtime.proto
	cp $(SHOWTIME)/showtime_pb2_grpc.py client
	cp $(SHOWTIME)/showtime_pb2.py client
	cp $(SHOWTIME)/showtime_pb2_grpc.py booking
	cp $(SHOWTIME)/showtime_pb2.py booking

booking:
	python -m grpc_tools.protoc -I=$(BOOKING)/protos --python_out=$(BOOKING) --grpc_python_out=$(BOOKING) booking.proto
	cp $(BOOKING)/booking_pb2_grpc.py client
	cp $(BOOKING)/booking_pb2.py client
	cp $(BOOKING)/booking_pb2_grpc.py user
	cp $(BOOKING)/booking_pb2.py user
