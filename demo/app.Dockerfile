FROM ubuntu:14.04
MAINTAINER nicholedean, yimkh92@gmail.com

# Get up pip, vim, etc.
RUN apt-get -qq update --fix-missing
RUN apt-get install -y --force-yes python-pip python-dev libev4 libev-dev gcc libxslt-dev libxml2-dev libffi-dev vim curl
RUN pip install --upgrade pip

# Get numpy, scipy, scikit-learn and flask
RUN apt-get install -y --force-yes python-numpy python-scipy
RUN pip install scikit-learn
RUN pip install flask-restful

# Add the project repository
ADD . /

# Expose the port for API
EXPOSE 5000

# Run the API
CMD [ "python", "/app.py" ]