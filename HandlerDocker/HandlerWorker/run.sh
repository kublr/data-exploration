#!/bin/bash
echo "Creating vars"
# export RABBIT_USERNAME_SET="test2"
# export RABBIT_USERPASS_SET="test2"
# export RABBIT_IP_SET="192.168.50.132"

echo "Running in Celery"
cd opt/
python3 Scheduler.py
celery -A Worker worker -Q handler_queue --loglevel=info -n handler@%n

