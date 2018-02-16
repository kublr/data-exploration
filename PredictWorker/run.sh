#!/bin/bash
echo "Running in Celery"
cd opt/
celery -A Worker worker --loglevel=info -n worker$((1 + RANDOM % 1000000))@%n

