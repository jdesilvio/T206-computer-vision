#[cv.T206.io](http://cv.t206.io/)

## A computer vision app for [T206.io](http://www.t206.io/)  

### Made with:

* Python 2.7
* OpenCV
* HDF5
* Docker
* Hosted on Digital Ocean
* https://github.com/jdesilvio/py-opencv-hdf5-docker as a starting point for Docker environment
* https://github.com/realpython/flask-image-search as a starting point for the Flask app
* https://github.com/OrangeTux/minimal-docker-python-setup for NGINX support

### Setup
    # Import NGINX image during initial setup
    docker import - jdesilvio/nginx < nginx/rootfs.tar

    # Build
    docker-compose build &&
    docker-compose up -d &&
    docker exec t206cv_app_1 mkdir app/dbdata &&
    docker cp ~/Desktop/dbdata/data.h5 t206cv_app_1:app/dbdata/data.h5

    # Re-build from scratch
    docker-compose stop &&
    docker-compose rm -f --all &&
    docker-compose pull &&
    docker-compose build --no-cache &&
    docker-compose up -d --force-recreate --remove-orphans

### If errors appear...

And it sounds like a memory issue:

 * Create a (swapfile)[https://gist.github.com/jdesilvio/20665f75779e092bcd6a69351cd21e66]
 * It could be that there is a bunch of junk in your `docker-machine`. Check the size of a file called `disk.vmdk`. If it's large and you are ok with deleting all images and containers and starting from scratch, run:
    docker-machine rm default


---

### Setup without Docker Compose (keeping for reference)
    docker build --rm --build-arg ACCESS_KEY='access key' --build-arg SECRET_KEY='secret key' -t t206cv-data .
    docker build --rm -t t206cv .
    docker run -d -t -v /app/dbdata --name data t206cv-data
    docker run -p 80:5000 --volumes-from data --name app t206cv


