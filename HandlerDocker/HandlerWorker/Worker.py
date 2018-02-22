#This defines a worker that receives result msgs from other workers
#Will run on local computer and put together the result 
#Runs on its own handler_gueue
import os
from celery import Celery
import numpy as np
from celery.signals import worker_shutting_down
from celery.signals import worker_init

user = os.environ['REBBIT_USERNAME_SET']
userpass = os.environ['REBBIT_USERPASS_SET']
ip = os.environ['REBBIT_IP_SET']


app = Celery('Worker', broker=('amqp://' + user + ':' + userpass + '@' + ip + '/'))

l = [[1,2,3]]





@app.task()
def result_handler(n_estimators, min_samples_leaf, result):
	new_row = [n_estimators, min_samples_leaf, result]
	l = np.load("/opt/volume/save.npy")
	l = np.vstack([l, new_row])
	np.save("/opt/volume/save.npy", l)
	np.savetxt("/opt/volume/list.csv", l, delimiter=",")

	return result

@worker_init.connect
def worker_init(**kwargs):
	np.save("/opt/volume/save.npy", l)

@worker_shutting_down.connect
def worker_shutting_down(sig, how, exitcode, **kwargs):
	l = np.load("/opt/volume/save.npy")
	np.savetxt("/opt/volume/list.csv", l, delimiter=",")