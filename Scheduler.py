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
	res = predict.delay(343, 50)
	listOfResponces.append(res)
	#print(res.get())

# while(True):
# 	if len(listOfResponces) > 0:
# 		for i in listOfResponces:
# 			if i.ready():
# 				print(i.get())
# 				listOfResponces.remove(i)
# 	else:
# 		break;
# 	time.sleep(1)