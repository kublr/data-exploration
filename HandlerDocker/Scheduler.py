import os
from celery import Celery
from celery.signals import task_success
import time


user = os.environ['RABBIT_USERNAME_SET']
userpass = os.environ['RABBIT_USERPASS_SET']
ip = os.environ['RABBIT_IP_SET']


app = Celery('Worker', broker=('amqp://' + user + ':' + userpass + '@' + ip + '/'))
@app.task
def predict(n_estimators, min_samples_leaf):
    return 1

# @task_success.connect(sender='tasks.predict')
# def task_success(result, **args):
# 	print(result.get())

listOfResponces = []
for i in range(100):
	for j in range(50):
		n_estimators = 10 + i
		min_samples_leaf = 5 + j
		res = predict.delay(n_estimators, min_samples_leaf)
		listOfResponces.append(res)

	#print(res.get())
