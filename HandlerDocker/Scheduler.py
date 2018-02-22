import os
from celery import Celery
from celery.signals import task_success
import time


user = os.environ['REBBIT_USERNAME_SET']
userpass = os.environ['REBBIT_USERPASS_SET']
ip = os.environ['REBBIT_IP_SET']


app = Celery('Worker', broker=('amqp://' + user + ':' + userpass + '@' + ip + '/'))
@app.task
def predict(n_estimators, min_samples_leaf):
    return 1

# @task_success.connect(sender='tasks.predict')
# def task_success(result, **args):
# 	print(result.get())

listOfResponces = []
for i in range(10):
	n_estimators = 100 + i*20
	min_samples_leaf = 20 + i*10
	res = predict.delay(n_estimators, min_samples_leaf)
	listOfResponces.append(res)
	#print(res.get())
