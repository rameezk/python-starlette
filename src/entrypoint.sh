#!/usr/bin/sh

gunicorn -w 4 -k uvicorn.workers.UvicornWorker --log-level info app:app -b "0.0.0.0:5000"
