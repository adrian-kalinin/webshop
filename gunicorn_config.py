from pathlib import Path


command = '/usr/bin/gunicorn'
pythonpath = str(Path(__file__).resolve())
bind = '0.0.0.0:8080'

workers = 3
worker_connections = 1000
timeout = 1200
limit_request_fields = 32000
limit_request_field_size = 0

worker_class = 'gevent'
raw_env = 'DJANGO_SETTINGS_MODULE=webshop.settings'
