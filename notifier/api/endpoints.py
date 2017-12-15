import os
from celery import Celery

BROKER_URL = os.environ.get("NOTIFIER_BROKER_URL")
QUEUE = os.environ.get("NOTIFIER_QUEUE")

if not BROKER_URL:
    raise RuntimeError("No broker URL set")

if not QUEUE:
    raise RuntimeError("No queue set")

app = Celery("notifier", broker=BROKER_URL, backend="rpc://")


@app.task(name="Notifier.list", queue=QUEUE)
def list():
    pass


@app.task(name="Notifier.info", queue=QUEUE)
def info(name):
    pass


@app.task(name="Notifier.run", queue=QUEUE)
def run(plugin_name, **kwargs):
    pass
