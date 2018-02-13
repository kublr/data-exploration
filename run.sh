#!/bin/bash
echo "Running in Celery"
celery -A Worker worker --loglevel=info &
