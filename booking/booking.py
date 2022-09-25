import grpc
from concurrent import futures
import booking_pb2
import booking_pb2_grpc
import json

EMPTY_BOOKING_DATA = booking_pb2.BookingData(userId="",
                                             dates="")


class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["bookings"]

    def GetListBookings(self, request, context):
        for booking in self.db:
            yield booking_pb2.BookingData(userId=booking['userid'],
                                          dates=booking['dates'])

    def GetBookingByUserId(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.userId:
                print("Booking found!")
                return booking_pb2.BookingData(userId=booking['userid'],
                                               dates=booking['dates'])
        return EMPTY_BOOKING_DATA


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
