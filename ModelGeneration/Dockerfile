#Setting the base image for this image to be based off of
FROM python:3.6
#Setting the working directory
WORKDIR /app
#Copy all files to working directory
COPY . /app
#Installing libraries in requirements file
RUN pip3 install -r requirements.txt
#Running python file
CMD python ModelGeneration.py
