# A multi-container `Docker` microservice

###Built with:
* Python3
* Flask
* OpenCV3
* HDF5

### Setup
    docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
    docker build --rm -t h5data-only ./data-only
    docker build --rm -t t206cv ./code
    docker run -d -t -v /h5data --name data h5data-only
    docker run -p 80:5000 --volumes-from data --name app t206cv

### Refresh
    docker stop app && docker rm app
    docker build --rm -t t206cv ./code
    docker run -p 80:5000 --volumes-from data --name app t206cv

### Images used
https://s3.amazonaws.com/t206/images/loc/fronts/095_0938_ty_cobb_portrait-green_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/097_0939_ty_cobb_portrait-red_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/234_1047_walter_johnson_portrait_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/268_0926_nap_lajoie_portrait_front.jpg
https://s3.amazonaws.com/t206/images/loc/fronts/520_0936_cy_young_cleveland-portrait_front.jpg
