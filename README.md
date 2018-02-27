# data-exploration

There are two dockers. 
1. WORKER DOCKER - creates a worker which accepts parameters and runs a random forest with those parameters. The worker then sends the accuracy result to a handler worker.
Random forest will train using the dataset which is located in the mounted folder and is called:
```
ToTrainDataset.csv
```
The dataset that was used is located in this repo.


Building worker:
```
docker build -t kublr/data-exploration:latest
```
Here kublr/data-exploration:latest is a tag that is used to run the worker and commit to docker hub


Running worker:
The worker needs the following args to be set:
```
RABBIT_USERNAME_SET= "admin user name of rabbitmq"
RABBIT_USERPASS_SET= "Password to the user name"
RABBIT_IP_SET= "IP or link on which rabbit server is running"
```
You can set them either in the docker file or pass them as parameters.

If you set them in docker file use this command to run: 
```
docker run -i -v mountFolderFromLocal:/opt/volume data-exploration:latest
```
If you wish to pass them use this command:
```
sudo docker run -i -v mountFolderFromLoca:/opt/volume -e RABBIT_IP_SET=LINK -e RABBIT_USERPASS_SET=USER -e RABBIT_USERNAME_SET=PASS data-exploration:latest 
```
Replace: LINK, USER, PASS
Make sure that mount folder starts from root of the computer. Ex: /home/user/Desktop/MountFolder


2. HANDLER WORKER - receives the results from workers and puts them in a list in the mounted folder.


Building worker:
```
docker build -t kublr/data-exploration-handler:latest
```
Here kublr/data-exploration:latest is a tag that is used to run the worker and commit to docker hub

Running worker:
The worker needs the following args to be set:
```
RABBIT_USERNAME_SET= "admin user name of rabbitmq"
RABBIT_USERPASS_SET= "Password to the user name"
RABBIT_IP_SET= "IP or link on which rabbit server is running"
```
You can set them either in the docker file or pass them as parameters.

If you set them in docker file use this command to run: 
```
docker run -i -v mountFolderFromLocal:/opt/volume data-exploration-handler:latest
```
If you wish to pass them use this command:
```
sudo docker run -i -v mountFolderFromLoca:/opt/volume -e RABBIT_IP_SET=LINK -e RABBIT_USERPASS_SET=USER -e RABBIT_USERNAME_SET=PASS data-exploration-handler:latest 
```
Replace: LINK, USER, PASS
Make sure that mount folder starts from root of the computer. Ex: /home/user/Desktop/MountFolder

Handler worker will create a Results.csv in the mounted folder. This file will show which variables were used to run the random forest and it will show the accuracy of the random forest run.
