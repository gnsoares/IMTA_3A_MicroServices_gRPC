import grpc

import movie_pb2
import movie_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc
import booking_pb2
import booking_pb2_grpc


def get_list_movies(stub):
    allmovies = stub.GetListMovies(movie_pb2.Empty())
    for movie in allmovies:
        print("Movie called %s" % (movie.title))


def get_movie_by_id(stub, id):
    movie = stub.GetMovieByID(id)
    print(movie)


def get_movie_by_title(stub, title):
    movie = stub.GetMovieByTitle(title)
    print(movie)


def create_movie(stub, movie):
    result = stub.CreateMovie(movie)
    print(result.message)
    print(result.movie)


def update_movie_rating(stub, rating_update):
    result = stub.UpdateMovieRating(rating_update)
    print(result.message)
    print(result.movie)


def remove_movie(stub, id):
    result = stub.RemoveMovie(id)
    print(result.message)
    print(result.movie)


#-------Showtime ---------------
def get_list_times(stub):
    alltimes = stub.GetListTimes(showtime_pb2.EmptyDate())
    for time in alltimes:
        print("Times %s" % (time))


def get_times_by_date(stub, date):
    times = stub.GetTimesByDate(date)
    print(times)

#-------Booking ---------------
def get_list_bookings(stub):
    allBookings = stub.GetListBookings(booking_pb2.EmptyBooking())
    for booking in allBookings:
        print("Bookings %s" % (booking))


def get_booking_by_userId(stub, userId):
    bookings = stub.GetBookingByUserId(userId)
    print(bookings)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = movie_pb2_grpc.MovieStub(channel)
        print("-------------- GetListMovies --------------")
        get_list_movies(stub)
        print("-------------- GetMovieByID --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452aaaae")
        get_movie_by_id(stub, movieid)
        print("-------------- GetMovieByTitle --------------")
        title = movie_pb2.Title(title="The Martian")
        get_movie_by_title(stub, title)
        print("-------------- CreateMovie --------------")
        movie = movie_pb2.MovieData(id="a8034f44-aee4-44cf-b32c-74cf452ae",
                                    title="Knives Out",
                                    rating=7.9,
                                    director="Rian Johnson")
        create_movie(stub, movie)
        print("-------------- UpdateMovieRatingById --------------")
        rating_update = movie_pb2.RatingUpdate(
            id="a8034f44-aee4-44cf-b32c-74cf452ae", rating=9.9)
        update_movie_rating(stub, rating_update)
        print("-------------- UpdateMovieRatingByTitle --------------")
        rating_update = movie_pb2.RatingUpdate(title="Knives Out", rating=9.9)
        update_movie_rating(stub, rating_update)
        print("-------------- RemoveMovie --------------")
        movieid = movie_pb2.MovieID(id="a8034f44-aee4-44cf-b32c-74cf452ae")
        remove_movie(stub, movieid)

    with grpc.insecure_channel('localhost:3002') as channel:
        stub = showtime_pb2_grpc.ShowtimeStub(channel)
        print("-------------- GetListTimes --------------")
        get_list_times(stub)
        print("-------------- GetMovieByID --------------")
        date = showtime_pb2.Date(date="20151203")
        get_times_by_date(stub, date)

    with grpc.insecure_channel('localhost:3003') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)
        print("-------------- GetListBookings --------------")
        get_list_bookings(stub)
        print("-------------- GetBookingByUserId --------------")
        userId = booking_pb2.UserId(userId="garret_heaton")
        get_booking_by_userId(stub, userId)

    channel.close()


if __name__ == '__main__':
    run()
