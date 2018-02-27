#This defines a worker that receives result msgs from other workers
#Will run on local computer and put together the result 
#Runs on its own handler_gueue
import os
from celery import Celery
import pandas as pd
from celery.signals import worker_shutting_down
from celery.signals import worker_init

user = os.environ['RABBIT_USERNAME_SET']
userpass = os.environ['RABBIT_USERPASS_SET']
ip = os.environ['RABBIT_IP_SET']


app = Celery('Worker', broker=('amqp://' + user + ':' + userpass + '@' + ip + '/'))



@app.task()
def result_handler(n_estimators, min_samples_leaf, result):
	df = pd.DataFrame([[n_estimators, min_samples_leaf, result]], columns=["n_estimators", "min_samples_leaf", "accuracy"])
	df_open = pd.read_csv("/opt/volume/Results.csv")
	df_open = df_open.append(df)
	df_open.to_csv("/opt/volume/Results.csv", index=False, columns=["n_estimators", "min_samples_leaf", "accuracy"])
	return result

@worker_init.connect
def worker_init(**kwargs):
	df = pd.DataFrame(columns=["n_estimators", "min_samples_leaf", "accuracy"])
	df.to_csv("/opt/volume/Results.csv", columns=["n_estimators", "min_samples_leaf", "accuracy"], index=False)
