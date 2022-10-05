# UE-AD-A1-GRPC

The project is composed of 4 services each one with its own folder. The services are:
* `movie`
* `showtime`
* `booking`
* `user` (the only one accessed through a REST API)

Each service runs using Python 3.10

Inside each folder you will find:
* Main server file (`*.py`)
* Dockerfile to build service image
* Python library requirements (`requirements.txt`)
* `data` folder with the `.json` file that holds the service data
* `protos` folder with the `.proto` file of the service describing its stubs

And a client folder that is a tester for each request in each service. It also contains the main python file and a `requirements.txt`.

### Running locally

```
make
cd movie
python3.10 movie.py
cd showtime
python3.10 showtime.py
cd booking
python3.10 booking.py
cd user
python3.10 user.py [-H HOST] -p PORT
```

### Testing gRPC Services

```
make
cd client
python3.10 client.py
```

### Running with Docker

```
make
docker-compose up [--build] ${SERVICE}
```
