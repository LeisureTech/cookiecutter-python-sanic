FROM .
WORKDIR /app

# copy the dependencies file to the working directory
COPY src/requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local {{cookiecutter.module_name}} directory to the working directory
COPY / /app/src
EXPOSE 5000
CMD ["python", "/app/src/app.py"]
