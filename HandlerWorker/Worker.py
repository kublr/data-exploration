#This defines a worker that receives result msgs from other workers
#Will run on local computer and put together the result 
#Runs on its own handler_gueue
from celery import Celery
import numpy as np
from celery.signals import worker_shutting_down
from celery.signals import worker_init


app = Celery('Worker', broker='pyamqp://guest@localhost/')

l = [[1,2,3]]





@app.task()
def result_handler(n_estimators, min_samples_leaf, result):
	new_row = [n_estimators, min_samples_leaf, result]
	l = np.load("save.npy")
	l = np.vstack([l, new_row])
	np.save("save.npy", l)

	return result

@worker_init.connect
def worker_init(**kwargs):
	np.save("save.npy", l)

@worker_shutting_down.connect
def worker_shutting_down(sig, how, exitcode, **kwargs):
	l = np.load("save.npy")
	np.savetxt("list.csv", l, delimiter=",")