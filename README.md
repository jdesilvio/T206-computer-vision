# A multi-container `Docker` microservice

###Built with:
* https://github.com/jdesilvio/py-opencv-hdf5-docker as a starting point for Docker environment
* https://github.com/realpython/flask-image-search as a starting point for the Flask app

### Setup
    docker build --rm -t h5data-only ./data-only
    docker build --rm -t t206cv ./app
    docker run -d -t -v /h5data --name data h5data-only
    docker run -p 80:5000 --volumes-from data --name app t206cv

### Refresh
    docker stop app && docker rm app
    docker build --rm -t t206cv ./code
    docker run -p 80:5000 --volumes-from data --name app t206cv

### Images used
https://s3.amazonaws.com/t206/images/loc/fronts/097_0939_ty_cobb_portrait-red_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/234_1047_walter_johnson_portrait_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/268_0926_nap_lajoie_portrait_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/520_0936_cy_young_cleveland-portrait_front.jpg
