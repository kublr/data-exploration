FROM ubuntu:latest
LABEL maintainer dfedorchuk@eastbanctech.com

# Update ubuntu and install the required packages
RUN apt-get update && apt-get install -y make ant

# Install essentials
RUN apt-get -y install python3-pip
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install scipy

VOLUME "/opt/volume"

#Copy script into docker
COPY runner.py /opt
 
#Set script as entry point 
ENTRYPOINT ["python3", "/opt/runner.py"]