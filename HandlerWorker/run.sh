#!/bin/bash
echo "Running in Celery"
celery -A Worker worker -Q handler_queue --loglevel=info -n handler@%n
