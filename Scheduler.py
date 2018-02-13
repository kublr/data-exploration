from celery import Celery

app = Celery('Worker', broker='pyamqp://guest@localhost//', backend='rpc://')

@app.task
def predict(n_estimators, min_samples_leaf):
    return 1

res = predict.delay(343, 50)

print(res.get())