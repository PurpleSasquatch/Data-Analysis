#Setting the base image for this image to be based off of
FROM python:3-alpine3.15
#Creating arguments for Environment variables
ARG username
ARG key
#Creating Environment variables needed for kaggle
ENV KAGGLE_USERNAME=username
ENV KAGGLE_KEY=key
#Setting the working directory
WORKDIR /app
#Copy all files to working directory
COPY . /app
#Installing libraries in requirements file
RUN pip3 install -r requirements.txt
#Running python file
RUN kaggle config set -n path -v /app/download
RUN kaggle config view
#exit code is set to always ignore error as details are only passed by compose file
#This keeps login details secure
RUN kaggle datasets download -d iarunava/cell-images-for-detecting-malaria; exit 0
CMD python DownloadingDataset.py
