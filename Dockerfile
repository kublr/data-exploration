#run docker with this command
#docker run -d -v /home/dennisfedorchuk/Desktop/Tables:/opt/volume data_e

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
RUN pip3 install celery

VOLUME "/opt/volume"

#Copy script into docker
COPY run.sh /opt
COPY Worker.py /opt
 
# To run a worker use this line
# RUN celery -A Worker worker --loglevel=info

RUN chmod +x ./opt/run.sh

#Set script as entry point 
ENTRYPOINT ["/opt/run.sh"]
