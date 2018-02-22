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
RUN pip3 install celery

VOLUME "/opt/volume"

#Copy script into docker
COPY HandlerWorker/run.sh /opt
COPY HandlerWorker/Worker.py /opt
COPY Scheduler.py /opt

RUN echo "Creating vars"
ENV REBBIT_USERNAME_SET=test2
ENV REBBIT_USERPASS_SET=test2
ENV REBBIT_IP_SET=192.168.0.100

RUN chmod +x ./opt/run.sh
EXPOSE 5672

#Set script as entry point 
ENTRYPOINT ["./opt/run.sh"]
