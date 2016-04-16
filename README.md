# A multi-container `Docker` microservice

###Built with:
* https://github.com/jdesilvio/py-opencv-hdf5-docker as a starting point for Docker environment
* https://github.com/realpython/flask-image-search as a starting point for the Flask app

### Setup
    docker build --rm -t t206cv-data .
    docker build --rm -t t206cv .
    docker run -d -t -v /app/dbdata --name data t206cv-data
    docker run -p 80:5000 --volumes-from data --name app t206cv
