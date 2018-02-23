# data-exploration

There are two dockers. 
1. WORKER DOCKER - creates a worker which accepts parameters and runs a random forest with those parameters. The worker then sends the accuracy result to a handler worker.

To build worker:
```
docker build -t data-exploration:latest
```
To run worker:
```
docker run -i -v mountFolderFromLocal:/opt/volume data-exploration:latest

or

sudo docker run -i -v /home/dennisfedorchuk/Desktop/Tables:/opt/volume -e RABBIT_IP_SET=LINK -e RABBIT_USERPASS_SET=USER -e RABBIT_USERNAME_SET=PASS data-exploration:latest 

Replace: LINK, USER, PASS
```
The worker needs the following args to be set:
```
RABBIT_USERNAME_SET= "admin user name of rabbitmq"
RABBIT_USERPASS_SET= "Password to the user name"
RABBIT_IP_SET= "IP or link on which rabbit server is running"
```
Random forest will train using the dataset which is located in the mounted folder and is called:
```
ToTrainDataset.csv
```


2. HANDLER WORKER - receives the results from workers and puts them in a list. 
To build worker:
```
docker build -t data-exploration-handler:latest
```
To run worker:
```
docker run -i -v mountFolderFromLocal:/opt/volume data-exploration-handler:latest

or 

sudo docker run -i -v /home/dennisfedorchuk/Desktop/Tables:/opt/volume -e RABBIT_IP_SET=LINK -e RABBIT_USERPASS_SET=USER -e RABBIT_USERNAME_SET=PASS data-exploration-handler:latest 
Replace: LINK, USER, PASS
```
The worker needs the following args to be set:
```
RABBIT_USERNAME_SET= "admin user name of rabbitmq"
RABBIT_USERPASS_SET= "Password to the user name"
RABBIT_IP_SET= "IP or link on which rabbit server is running"
```
Worker will create a list.csv in the mounted folder which contains all the results