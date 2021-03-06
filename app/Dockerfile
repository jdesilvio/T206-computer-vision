FROM python:2.7

ENV HOME /root

# Install dependencies
RUN apt-get update \
    && apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install -y gcc
RUN apt-get install -y build-essential
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y cmake
RUN apt-get install -y gfortran 
RUN apt-get install -y libatlas-base-dev 
RUN apt-get install -y python-pip 
RUN apt-get install -y python-dev
RUN apt-get install -y subversion
RUN apt-get install -y supervisor
RUN apt-get install -y nginx
RUN apt-get install -y cython
RUN apt-get clean

# Install Python packages
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install bottleneck
RUN pip install boto3
RUN pip install scipy
RUN pip install Flask
RUN pip install uwsgi

# Build OpenCV and dependencies
RUN cd \
    && git clone https://github.com/Itseez/opencv.git \
    && cd opencv \
    && git checkout tags/3.1.0 \
    && cd \
    && git clone https://github.com/Itseez/opencv_contrib.git \
    && cd opencv_contrib \
    && git checkout tags/3.1.0 \
    && cd ~/opencv \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE \
             -D CMAKE_INSTALL_PREFIX=/usr/local \
             -D INSTALL_C_EXAMPLES=OFF \
             -D INSTALL_PYTHON_EXAMPLES=ON \
             -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
             -D BUILD_EXAMPLES=ON .. \
    && make -j4 && make install \
    && cd

# Build HDF5
RUN cd ; wget https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8.16/src/hdf5-1.8.16.tar.gz
RUN cd ; tar zxf hdf5-1.8.16.tar.gz
RUN cd ; mv hdf5-1.8.16 hdf5-setup
RUN cd ; cd hdf5-setup ; ./configure --prefix=/usr/local/
RUN cd ; cd hdf5-setup ; make && make install

# Cleanup
RUN cd ; rm -rf hdf5-setup
RUN apt-get -yq autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python packages with dependencies on HDF5
RUN pip install tables
RUN pip install h5py
RUN pip install -U scikit-image

RUN rm -fr /root/.cache

# Update environment and working directories
ENV PYTHONUNBUFFERED 1
#WORKDIR /app
#ADD . /app
COPY app /app
#RUN mv config ../config

# Setup config
#RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
#RUN rm /etc/nginx/sites-enabled/default

#RUN ln -s /config/nginx.conf /etc/nginx/sites-enabled/
#RUN ln -s /config/supervisor.conf /etc/supervisor/conf.d/

#EXPOSE 80
#CMD ["python", "app.py"]

COPY app /app
COPY uwsgi.ini /etc/uwsgi.ini
COPY shared_libs/* /lib/

CMD uwsgi --ini /etc/uwsgi.ini
