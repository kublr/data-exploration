from celery import Celery
from celery.signals import task_success
import time


app = Celery('Worker', broker='pyamqp://guest@localhost//', backend='rpc://')

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
