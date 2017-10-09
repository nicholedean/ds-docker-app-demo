FROM ubuntu:14.04
MAINTAINER nicholedean, yimkh92@gmail.com

# Get python-setuptools and pip
RUN apt-get -qq update --fix-missing
RUN apt-get install -y --force-yes python-setuptools
RUN easy_install pip

# Get numpy, scipy, scikit-learn and flask
RUN apt-get install -y --force-yes python-numpy python-scipy
RUN pip install scikit-learn
RUN pip install flask-restful

# PYTHONPATH
ENV PYTHONPATH=/python

# Expose the port for API
EXPOSE 5000

# Run the API
CMD [ "python", "/python/src/app.py" ]