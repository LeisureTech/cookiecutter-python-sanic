FROM ubuntu:impish
WORKDIR /app

# To make sure that our versions are up-to-date
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# copy the dependencies file to the working directory
COPY requirements.txt /app

# install dependencies
RUN pip3 install -r requirements.txt  --no-cache-dir

# copy the content of the local {{cookiecutter.project_slug}} directory to the working directory
COPY . /app
EXPOSE 8000
CMD ["sanic", "server.app"]
