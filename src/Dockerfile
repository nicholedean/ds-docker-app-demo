FROM python:3
LABEL maintainer="nicholedean, yimkh92@gmail.com"

# Add and install Python modules
ADD requirements.txt /python/src/requirements.txt
RUN cd /python/src; pip install -r requirements.txt

# Environment variables
ENV APP_ENV=dev
ENV PYTHONPATH=/python
ENV APP_ENV_CONFIG=${PYTHONPATH}/src/config/env.cfg

# Bundle app source
ADD . /python/src

# Expose the port for API
EXPOSE 5000

# Run the API
CMD [ "python", "/python/src/app.py" ]